"""根据 data/papers/*.py 中已完成的文献，生成/更新 Excel 数据库（保留“筛选结果”工作表）、
质控清单、单位换算记录，并更新 progress.json。

用法：
  python3 scripts/build_db.py            # 处理 data/registry.py 中登记的全部文献
  断点续跑：progress.json 记录已完成的文献；每完成一篇即重写 Excel 并更新 progress.json。
"""
import importlib, json, re, sys
from datetime import datetime
from pathlib import Path
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Alignment, Font, PatternFill

B = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(B))
from data.registry import PAPERS  # 有序列表：模块名

XLSX = B / "稻田汞培养数据库.xlsx"
PROG = B / "progress.json"

T1_COLS = [
    ("实验编号", "实验编号"), ("文件名", "文件名"), ("第一作者", "第一作者"), ("年份", "年份"), ("期刊", "期刊"), ("DOI", "DOI"),
    ("文献核心问题", "文献核心问题"), ("文献主要结论", "文献主要结论"),
    ("实验名称", "实验名称"), ("实验类型", "实验类型"), ("实验目的", "实验目的"),
    ("采样地点", "采样地点"), ("土壤数量", "土壤数量"), ("污染背景", "污染背景"), ("采样深度", "采样深度"), ("土样状态", "土样状态"),
    ("pH", "pH"), ("有机质", "有机质（SOM/SOC）"), ("总汞", "总汞"), ("MeHg", "MeHg"), ("硫酸盐", "硫酸盐"), ("铁", "铁"),
    ("处理组", "处理组列表及说明"), ("外加汞形态", "外加汞形态"), ("外加汞剂量", "外加汞剂量"), ("相对本底倍数", "相对本底总汞倍数"),
    ("加汞后平衡", "加汞后平衡及时长"), ("其他添加物", "其他添加物（种类、剂量、时间）"), ("抑制剂", "抑制剂（种类、浓度）"), ("灭菌对照", "灭菌对照"),
    ("土量g", "土量（g）"), ("水量mL", "水量（mL）"), ("土水比", "土水比"), ("容器", "容器（材质、体积）"), ("密封方式", "密封方式"),
    ("气氛", "气氛（手套箱/充气）"), ("预培养", "预培养"), ("温度", "培养温度"), ("避光", "是否避光"), ("振荡", "是否振荡"),
    ("重复数", "每处理重复数"), ("取样方式", "取样方式"),
    ("示踪剂种类", "示踪剂种类"), ("示踪剂剂量", "示踪剂剂量及相对本底比例"), ("示踪剂预平衡", "示踪剂是否预平衡"),
    ("示踪培养时长", "示踪培养时长"), ("是否测t0", "是否测 t0"), ("Km公式", "Km 计算公式"), ("Kd公式", "Kd 计算公式"), ("同位素测定", "同位素测定方法与仪器"),
    ("总培养时长d", "总培养时长（d）"), ("取样时间点", "全部取样时间点"), ("各时间点指标", "各时间点测定指标"),
    ("MeHg方法", "MeHg 提取与测定方法"), ("质控", "质控（标准物质/回收率/检出限）"),
    ("Q_测t0", "【质量】测了 t0"), ("Q_示踪剂超本底", "【质量】示踪剂剂量超过本底汞"), ("Q_示踪超24h", "【质量】同位素示踪培养超过 24 h"),
    ("Q_灭菌对照", "【质量】设有灭菌对照"), ("Q_严格厌氧", "【质量】手套箱/严格厌氧"), ("Q_透氧容器", "【质量】使用透氧容器或密封材料"),
    ("原文摘录", "原文摘录（英文原句+页码）"), ("需查SI字段", "需查 SI 的字段"), ("备注", "备注"),
]
T2_COLS = ["实验编号", "土壤名称或编号", "处理", "时间点", "指标", "数值（原文）", "原文单位", "统一单位数值", "统一单位",
           "SD 或 SE", "重复数 n", "数据出处", "备注"]
KEY_FIELDS = ["土量g", "水量mL", "外加汞剂量", "总培养时长d", "取样时间点"]

FILL = {"不确定": "FFEB9C", "需查 SI": "F8CBAD", "未报道": "D9D9D9", "估读": "DDEBF7"}


def num(s):
    """解析原文数值，支持括号估读、范围、×10²。返回 [float...]"""
    s = s.strip().strip("()")
    s = s.replace("−", "-")
    m = re.fullmatch(r"([\d.]+)\s*[×x]\s*10([²³⁻\-\d]+)", s)
    sup = {"²": "2", "³": "3", "⁻": "-"}
    if m:
        e = "".join(sup.get(c, c) for c in m.group(2))
        return [float(m.group(1)) * 10 ** int(e)]
    parts = re.split(r"\s*[–~]\s*", s)
    try:
        return [float(p) for p in parts]
    except ValueError:
        return None


# 原单位 -> (指标集合, 统一单位, 系数, 换算方式说明)
CONV = {
    "×10−3 day−1": ("Km Kd", "d⁻¹", 1e-3, "乘以 10⁻³"),
    "×10−2 /d": ("Km Kd", "d⁻¹", 1e-2, "乘以 10⁻²"),
    "%/d": ("Km", "d⁻¹", 1e-2, "%/d 除以 100"),
    "day−1": ("Km Kd", "d⁻¹", 1, "单位同义，不变"),
    "/d": ("Km Kd", "d⁻¹", 1, "单位同义，不变"),
    "d−1": ("Km Kd", "d⁻¹", 1, "单位同义，不变"),
    "h−1": ("Km Kd", "d⁻¹", 24, "h⁻¹ 乘以 24"),
    "μg·g−1": ("MeHg THg", "ng/g 干重", 1000, "μg/g 乘以 1000"),
    "μg/g": ("MeHg THg", "ng/g 干重", 1000, "μg/g 乘以 1000"),
    "mg/kg": ("MeHg THg", "ng/g 干重", 1000, "mg/kg 乘以 1000"),
    "μg/kg": ("MeHg THg", "ng/g 干重", 1, "μg/kg = ng/g，数值不变"),
    "ng·g−1": ("MeHg THg", "ng/g 干重", 1, "单位同义，不变"),
    "ng/g": ("MeHg THg", "ng/g 干重", 1, "单位同义，不变"),
    "%": ("%MeHg", "%", 1, "不变"),
}


def fmt(x):
    """保留4位有效数字，不用科学计数法"""
    return "{:f}".format(float("%.4g" % x)).rstrip("0").rstrip(".")


def convert(row, log):
    exp, soil, trt, t, ind, val, unit, sd, n, src, note = row
    est = val.strip().startswith("(")
    c = CONV.get(unit)
    if c is None or ind not in c[0].split():
        return "", "不可换算", note + ("；" if note else "") + f"原单位“{unit}”未定义换算"
    vals = num(val)
    if vals is None:
        return "", "不可换算", note + ("；" if note else "") + "数值无法解析"
    out = "–".join(fmt(v * c[2]) for v in vals)
    if est:
        out = f"({out})"
    log.append([exp, soil, trt, t, ind, val, unit, c[3], out, c[1]])
    return out, c[1], note


def fill_for(text):
    if not isinstance(text, str):
        return None
    if "不确定" in text:
        return FILL["不确定"]
    if "需查 SI" in text or "需查SI" in text:
        return FILL["需查 SI"]
    if text.startswith("未报道"):
        return FILL["未报道"]
    return None


def style(ws, widths, est_col=None):
    for c in ws[1]:
        c.font = Font(bold=True)
        c.fill = PatternFill("solid", fgColor="BDD7EE")
        c.alignment = Alignment(wrap_text=True, vertical="center")
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            f = fill_for(cell.value)
            if f:
                cell.fill = PatternFill("solid", fgColor=f)
        if est_col:
            v = row[est_col - 1].value
            if isinstance(v, str) and v.startswith("("):
                for k in (est_col, est_col + 2):
                    row[k - 1].fill = PatternFill("solid", fgColor=FILL["估读"])
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[ws.cell(1, i).column_letter].width = w
    ws.freeze_panes = "B2" if ws.title.startswith("表1") else "A2"
    ws.auto_filter.ref = ws.dimensions


def qc_rows(mod):
    rows = []
    stem = mod.PAPER["文件名"]
    for e in mod.T1:
        miss = [k for k in KEY_FIELDS if str(e.get(k, "")).startswith("未报道")]
        if "B" in e["实验类型"]:
            miss += [k for k in ("Km公式", "Kd公式") if str(e.get(k, "")).startswith("未报道")]
        sis = [k for k, _ in T1_COLS if "需查 SI" in str(e.get(k, ""))]
        unc = [f"{k}：{str(e.get(k))[:60]}" for k, _ in T1_COLS if "不确定" in str(e.get(k, ""))]
        ests = [r for r in mod.T2 if r[0] == e["实验编号"] and r[5].strip().startswith("(")]
        rows.append([stem, e["实验编号"], "；".join(miss) or "无",
                     ("；".join(sis) + ("｜" if sis else "") + e.get("需查SI字段", "")) or "无",
                     "\n".join(unc) or "无", f"{len(ests)} 个（见表2 中带括号的数值）" if ests else "无", ""])
    for ex in getattr(mod, "EXCLUDED", []):
        rows.append([stem, ex[0] + "（已排除）", "", "", "", "", f"{ex[1]}：{ex[2]}"])
    return rows


def main():
    prog = json.loads(PROG.read_text()) if PROG.exists() else {"done": [], "log": []}
    wb = load_workbook(XLSX) if XLSX.exists() else Workbook()
    for n in ["表1_培养条件", "表2_结果数值", "质控清单", "单位换算记录", "Sheet"]:
        if n in wb.sheetnames:
            del wb[n]
    w1 = wb.create_sheet("表1_培养条件"); w1.append([h for _, h in T1_COLS])
    w2 = wb.create_sheet("表2_结果数值"); w2.append(T2_COLS)
    wq = wb.create_sheet("质控清单"); wq.append(["文件名", "实验编号", "缺失的关键字段", "需查 SI 项", "不确定项", "图中估读的数值", "已排除的实验及原因"])
    wc = wb.create_sheet("单位换算记录"); wc.append(["实验编号", "土壤", "处理", "时间点", "指标", "原值", "原单位", "换算方式", "换算后数值", "统一单位"])
    conv_log = []
    for name in PAPERS:
        mod = importlib.import_module(f"data.papers.{name}")
        for e in mod.T1:
            full = {**mod.PAPER, **e}
            w1.append([full.get(k, "") for k, _ in T1_COLS])
        for r in mod.T2:
            u, uu, note = convert(r, conv_log)
            w2.append(list(r[:7]) + [u, uu] + list(r[7:10]) + [note])
        for q in qc_rows(mod):
            wq.append(q)
        if name not in prog["done"]:
            prog["done"].append(name)
            prog["log"].append({"paper": name, "file": mod.PAPER["文件名"], "time": datetime.now().isoformat(timespec="seconds")})
        # 每篇处理完即保存 Excel 与进度（断点续跑）
        wb.save(XLSX)
        PROG.write_text(json.dumps(prog, ensure_ascii=False, indent=1))
    for c in conv_log:
        wc.append(c)
    style(w1, [22] + [16] * 5 + [36, 36] + [22, 8, 30] + [30, 10, 20, 14, 30] + [20] * 6 + [40, 16, 18, 18, 16, 26, 20, 16]
          + [12, 14, 12, 20, 22, 26, 12, 10, 8, 8, 8, 24] + [20, 24, 14, 12, 18, 30, 30, 26] + [10, 30, 45, 40, 50]
          + [12] * 6 + [80, 30, 40])
    style(w2, [22, 24, 18, 14, 8, 12, 14, 12, 12, 14, 8, 26, 30], est_col=6)
    style(wq, [36, 24, 30, 40, 50, 24, 50])
    style(wc, [22, 24, 18, 12, 8, 10, 14, 18, 12, 12])
    order = ["筛选结果", "表1_培养条件", "表2_结果数值", "质控清单", "单位换算记录"]
    wb._sheets = [wb[n] for n in order if n in wb.sheetnames] + [s for s in wb._sheets if s.title not in order]
    wb.save(XLSX)
    PROG.write_text(json.dumps(prog, ensure_ascii=False, indent=1))
    print(f"表1 {w1.max_row - 1} 行；表2 {w2.max_row - 1} 行；换算 {len(conv_log)} 条；已完成 {len(prog['done'])} 篇")


if __name__ == "__main__":
    main()
