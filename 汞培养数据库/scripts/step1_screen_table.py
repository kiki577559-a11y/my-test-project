"""生成“筛选结果”工作表：合并清单、人工判断、自动抽取的原文依据（带页码）。"""
import json, re, sys
from pathlib import Path
from openpyxl import Workbook, load_workbook
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from openpyxl.styles import Alignment, Font, PatternFill
sys.path.insert(0, str(Path(__file__).parent))
from screening_judgments import J

B = Path(__file__).resolve().parents[1]; W = B / "_work"
inv = json.load(open(W / "inventory.json"))["docs"]
mloc = json.load(open(W / "methods_loc.json"))
REF = re.compile(r"^(■\s*)?(references?|literature cited)\b", re.I)

def evidence(i, pat):
    bl = json.load(open(W / "blocks" / f"{i}.json"))
    rx = re.compile(pat)
    for k, (p, t) in enumerate(bl):
        if REF.match(t) and k > len(bl) * 0.4: break
        for s in re.split(r"(?<=[.;])\s+(?=[A-Z(])", t):
            if rx.search(s):
                s = ILLEGAL_CHARACTERS_RE.sub('□', s.strip())  # 无法识别的字形（多为°等符号）以□标记
                return f"“{s[:350]}{'…' if len(s) > 350 else ''}”（p.{p}）"
    return None

mains = [d for d in inv if not d["is_si"]]
missing = [d["id"] for d in mains if d["id"] not in J]
assert not missing, f"缺少判断: {missing}"
rows = []
order = {"纳入": 0, "存疑": 1, "存疑(仅因方法未识别)": 2, "排除": 3}
for d in mains:
    cat, nexp, why, pat = J[d["id"]]
    ev = evidence(d["id"], pat)
    if ev is None:
        print("未抽到原文依据:", d["id"], pat)
        ev = "（自动抽取失败）"
    ml = mloc.get(d["id"])
    if ml:
        mstat = f"是（p.{ml[0]}）"
    elif "综述" in why or "Meta" in why or "规程" in why:
        mstat = "否（无方法部分，非原始研究）"
    else:
        mstat = "否"
    si = Path(d["si"]).name if d.get("si") else "无"
    copies = "；".join(c.split("/")[0] for c in d["copies"])
    rows.append([d["name"], copies, si, cat, nexp, why, ev, mstat])
rows.sort(key=lambda r: (order[r[3]], r[1], r[0]))

out = B / "稻田汞培养数据库.xlsx"
wb = load_workbook(out) if out.exists() else Workbook()
if "筛选结果" in wb.sheetnames: del wb["筛选结果"]
ws = wb.create_sheet("筛选结果", 0)
for n in list(wb.sheetnames):
    if n == "Sheet": del wb[n]
hdr = ["文件名", "所在文件夹（含重复副本）", "配对 SI", "类别", "符合标准的实验数及类型", "判断理由", "判断依据的原文片段及页码", "方法部分是否识别成功"]
ws.append(hdr)
for r in rows: ws.append(r)
widths = [42, 26, 22, 14, 20, 60, 70, 18]
for c, w in enumerate(widths, 1):
    ws.column_dimensions[ws.cell(1, c).column_letter].width = w
fills = {"纳入": "C6EFCE", "存疑": "FFEB9C", "存疑(仅因方法未识别)": "FCE4D6", "排除": "EDEDED"}
for row in ws.iter_rows():
    for cell in row:
        cell.alignment = Alignment(wrap_text=True, vertical="top")
for c in ws[1]:
    c.font = Font(bold=True); c.fill = PatternFill("solid", fgColor="BDD7EE")
for r in range(2, ws.max_row + 1):
    ws.cell(r, 4).fill = PatternFill("solid", fgColor=fills[ws.cell(r, 4).value])
ws.freeze_panes = "A2"
ws.auto_filter.ref = ws.dimensions
wb.save(out)
from collections import Counter
print(Counter(r[3] for r in rows), "共", len(rows))
json.dump(rows, open(W / "screening_rows.json", "w"), ensure_ascii=False, indent=0)
