"""Li et al. 2023, Ecotoxicology and Environmental Safety 266: 115585。页码为 PDF 页码。图1数值按页面图估读。"""
from .common import NOTRACER
PAPER = {"文件名": "EES_限氧稻田土壤中的微生物群落功能与甲基汞产生.pdf", "第一作者": "Zihao Li", "年份": "2023",
         "期刊": "Ecotoxicology and Environmental Safety", "DOI": "10.1016/j.ecoenv.2023.115585",
         "文献核心问题": "淹水稻田土壤中微量氧气输入（限氧 vs 缺氧）对微生物介导的 MeHg 生成及微生物群落功能的影响。",
         "文献主要结论": "限氧土壤（O24）MeHg 高于缺氧土壤；氧气输入改变了 16S rRNA 群落结构，但对 hgcA 群落影响小，并提高了与甲基化可能相关的代谢通路丰度。"}
T1 = [{**NOTRACER,
    "实验编号": "Li2023_EES_Exp1", "实验名称": "soil resuspension microcosms（2.2 Experimental design）", "实验类型": "A",
    "实验目的": "比较不同通气方式（N2/合成空气组合）下加汞稻田土泥浆 24 h 内的 MeHg 生成和微生物群落。",
    "采样地点": "湖南省长沙市某稻田；具体地点和坐标未报道", "土壤数量": "1", "污染背景": "一般农田（本底 THg 0.062 mg/kg）+ 人为加汞",
    "土样状态": "风干、粉碎、过 2 mm 筛；保存条件未报道", "总汞": "0.062 mg/kg（加汞前）",
    "处理组": "N24：N2 吹扫 24 h；N12：合成空气 12 h 后 N2 12 h；O12：N2 12 h 后合成空气 12 h；O24：合成空气 24 h（合成空气为 20.9% O2 + 79.1% N2；气流 500 mL/min）",
    "外加汞形态": "Hg(NO3)2（原文 mercury nitrate）", "外加汞剂量": "每个微宇宙加 0.15 mL 1 g/mL 硝酸汞溶液，使土壤 THg 达 3 mg/kg",
    "相对本底倍数": "约 48 倍（3 / 0.062，按原文数值计算）", "加汞后平衡": "未报道",
    "其他添加物": "乳酸钠 10 g/微宇宙（碳源），加入时间未明确", "抑制剂": "无", "灭菌对照": "无",
    "土量g": "50（风干土）", "水量mL": "400", "土水比": "1:8（原文 mass ratio of 1:8）", "容器": "未报道",
    "密封方式": "未报道", "气氛": "持续吹扫 N2 或合成空气（按处理），未在手套箱中", "预培养": "未报道",
    "温度": "28 ± 1 °C（原文 room temperature）", "避光": "是", "振荡": "磁力搅拌 300 rpm", "重复数": "3",
    "取样方式": "不确定（原文未说明；只有培养结束一个时间点）",
    "总培养时长d": "1（24 h）", "取样时间点": "24 h",
    "各时间点指标": "24 h：土壤 THg、MeHg、%MeHg；泥浆 ORP、pH、DO（原位）、溶解态硫酸盐、Fe3+（ferric）；16S rRNA 和 hgcA 扩增子测序；PICRUSt 功能预测",
    "MeHg方法": "约 1 g 冻干土加 15.0 mL 25% KOH/CH3OH，60 °C 消解 3 h（HJ 977–2018），乙基化-吹扫捕集，CVAFS（Brooks Rand Model III）测定；THg：王水（HCl:HNO3 1:1）90 °C 消解 2 h，原子荧光测定（GB/T 22105.1–2008）",
    "质控": "未报道",
    "Q_测t0": "否", "Q_灭菌对照": "否", "Q_严格厌氧": "否（按处理持续通入 N2 或空气）", "Q_透氧容器": "未报道",
    "原文摘录": ("【土量/水量/汞剂量】“The microcosms were filled with 50 g of air-dried soil and 400 mL of water at a mass ratio of 1:8. 0.15 mL 1 g/mL of dissolve mercury nitrate was added to each microcosm to simulate moderate Hg pollution of farmland soil, resulting in a soil THg concentration of 3 mg/kg.”（p.2）\n"
              "【培养时长】“We investigated Hg methylation in the paddy soils via a short-term (24 h) incubation experiment”（p.2）\n"
              "【条件】“The soil resuspension microcosms were incubated in the dark at room temperature (28 ± 1 ◦C) on a magnetic mixer at 300 rpm.”（p.2）\n"
              "【取样时间点】只有 24 h 终点（同上）。\n【Km/Kd 公式】无。"),
    "需查SI字段": "无",
    "备注": "不确定：正文写 %MeHg 为 2.92%–4.27%，但图1C 纵轴单位为‰，且 MeHg/THg（132.6 μg/kg ÷ 3.34 mg/kg）约为 4.0‰，正文“%”可能是笔误。不确定：正文写土壤 MeHg 范围为 83.2–173.2 μg/kg，但 N24 组均值为 74.9 μg/kg，低于该范围下限。容器类型未报道。",
}]
_m = {"N24": "74.9", "N12": "(73)", "O12": "(81)", "O24": "132.6"}
_t = {"N24": "(2.6)", "N12": "(2.7)", "O12": "(2.0)", "O24": "3.34"}
_p = {"N24": "(2.9)", "N12": "(2.75)", "O12": "(4.25)", "O24": "(4.0)"}
T2 = []
for k in _m:
    T2.append(("Li2023_EES_Exp1", "长沙稻田土", k, "24 h", "MeHg", _m[k], "μg/kg", "SD" + ("（未估读）" if _m[k][0] == "(" else "：未在正文给出"), "3",
               "Fig. 1A（p.4）" + ("，图中估读" if _m[k][0] == "(" else "；数值见正文 p.3"), ""))
    T2.append(("Li2023_EES_Exp1", "长沙稻田土", k, "24 h", "THg", _t[k], "mg/kg", "SD" + ("（未估读）" if _t[k][0] == "(" else "：未在正文给出"), "3",
               "Fig. 1B（p.4）" + ("，图中估读" if _t[k][0] == "(" else "；数值见正文 p.3"), ""))
    T2.append(("Li2023_EES_Exp1", "长沙稻田土", k, "24 h", "%MeHg", _p[k], "‰（图）/%（正文）", "SD（未估读）", "3",
               "Fig. 1C（p.4），图中估读", "单位不确定：图为‰，正文为%"))
T2.append(("Li2023_EES_Exp1", "长沙稻田土", "全部处理（范围）", "24 h", "MeHg", "83.2–173.2", "μg/kg", "未报道", "12", "正文 p.3", "平均 121.4 μg/kg；不确定：与 N24 均值 74.9 矛盾"))
T2.append(("Li2023_EES_Exp1", "长沙稻田土", "全部处理（范围）", "24 h", "THg", "2.37–3.66", "mg/kg", "未报道", "12", "正文 p.3", "平均 2.83 mg/kg"))
EXCLUDED = []
