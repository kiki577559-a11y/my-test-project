"""Hu et al. 2024, Environmental Pollution 345: 123471。页码为 PDF 页码。"""
from .common import NOTRACER
PAPER = {"文件名": "EP_汞污染碱性稻田土壤淹水-排水过程中汞的转化与迁移.pdf", "第一作者": "Shiwen Hu", "年份": "2024",
         "期刊": "Environmental Pollution", "DOI": "10.1016/j.envpol.2024.123471",
         "文献核心问题": "汞污染碱性稻田土壤在淹水-排水过程中汞的形态转化、甲基化、生物积累及风险，以及与关键元素生物地球化学循环的耦合。",
         "文献主要结论": "微宇宙和盆栽中有机-硫化物结合态汞和残渣态汞占总汞98%以上，汞的迁移性和风险较低；Fe(III)、SO4 2−、NO3− 还原引起 pH 下降，促进汞活化，而 Fe(II)、S2−、NH4+ 氧化使 pH 升高，降低汞活性。"}
T1 = [{**NOTRACER,
    "实验编号": "Hu2024_EP_Exp1", "实验名称": "Microcosm experiments（2.2 节）", "实验类型": "A",
    "实验目的": "在恒定振荡的微宇宙中模拟淹水 40 d、排水 20 d，追踪汞形态和 MeHg 的变化。",
    "采样地点": "贵州省铜仁市某汞污染稻田（27°32′57.52″N，109°12′47.38″E）", "土壤数量": "1", "污染背景": "矿区污染（汞污染稻田）",
    "采样深度": "0–20 cm", "土样状态": "风干、均质、过 2 mm 筛；保存条件未报道",
    "pH": "7.90 (0.18)", "有机质": "OM 31.5 (0.67) g kg−1", "总汞": "51.14 (0.78) mg kg−1", "MeHg": "未报道（初始 TMeHg 见表2）",
    "硫酸盐": "未报道", "铁": "全铁 26.30 (0.73) g kg−1",
    "处理组": "单一处理：淹水 40 d 后排水 20 d", "外加汞形态": "无（原位污染土，未外加汞）", "外加汞剂量": "无", "相对本底倍数": "无", "加汞后平衡": "无",
    "其他添加物": "5 mM NaCl 溶液（作为培养液）", "抑制剂": "无", "灭菌对照": "无",
    "土量g": "6（干土）", "水量mL": "30（5 mM NaCl）", "土水比": "1:5", "容器": "50 mL 血清瓶",
    "密封方式": "淹水期：丁基胶塞（压盖）；排水期：换成 0.45 μm 透气膜", "气氛": "N2 吹扫 30 min 后密封；在手套箱外的摇床上培养",
    "预培养": "未报道", "温度": "25 °C", "避光": "是", "振荡": "是：水平摇床 220 rpm", "重复数": "3",
    "取样方式": "破坏性：每个时间点取3瓶，在厌氧箱（H2/N2 2/98）中开盖", "总培养时长d": "60（淹水 40 d + 排水 20 d）",
    "取样时间点": "淹水 0, 2, 5, 10, 20, 40 d；排水 2, 7, 15, 20 d",
    "各时间点指标": "各时间点：Eh、pH；滤液 F0-Hg、WMeHg、DOC、NH4+、NO3−、Fe(II)、SO4 2−；湿土 Fe(II)HCl、IHg、TMeHg、EMeHg、汞形态（F1–F7）",
    "MeHg方法": "TMeHg、EMeHg、WMeHg 均乙基化后用 MERX CVAFS（Brooks Rand）测定，US EPA 1630；具体提取方法正文引自文献",
    "质控": "ERM-CC580（MeHg）、GBW07453（GSS-24，THg）；回收率：未报道",
    "Q_测t0": "是（0 d）", "Q_灭菌对照": "否", "Q_严格厌氧": "否（N2 吹扫后密封，在手套箱外培养）", "Q_透氧容器": "否（淹水期）",
    "原文摘录": ("【土量/水量】“Microcosm experiments were conducted in 50 mL serum bottles containing 6 g dry paddy soil and 30 mL 5 mM NaCl. Soil suspension were flushed with nitrogen for 30 min and sealed with butyl rubber stoppers”（p.2–3）\n"
              "【培养时长】“a total of 30 serum bottles were placed in a horizontal shaker and shake with a speed of 220 rpm min−1 at 25 ◦C in the dark. After 40 d of flooding, all butyl rubber stoppers were replaced with a 0.45 μm porous film to allow gas exchange with air for 20 d of drainage under continuous shaking”（p.3）\n"
              "【取样时间点】“At flooding intervals (0, 2, 5, 10, 20, and 40 d) and drainage intervals (2, 7, 15, and 20 d), three serum bottles were obtained … and all sampling processes are destructive.”（p.3）\n"
              "【汞剂量】未外加汞。\n【Km/Kd 公式】无。"),
    "需查SI字段": "无",
    "备注": "原文写排水期为 20 d，但后文又写“flooding and drainage periods were set to 40 and 15 d”（不确定）。共30个血清瓶，但10个时间点 × 3个重复需要30瓶，与此一致。同文的盆栽实验已排除。",
}]
T2 = [("Hu2024_EP_Exp1", "铜仁汞污染碱性稻田土", "淹水", "0 d（不确定，原文为“first increased from”）", "MeHg", "1.23", "μg kg−1", "未报道", "3", "正文 p.5；Fig. 2c", "TMeHg"),
      ("Hu2024_EP_Exp1", "铜仁汞污染碱性稻田土", "淹水", "10 d", "MeHg", "2.67", "μg kg−1", "未报道", "3", "正文 p.5；Fig. 2c", "TMeHg"),
      ("Hu2024_EP_Exp1", "铜仁汞污染碱性稻田土", "淹水", "不确定（原文“then decreased to”）", "MeHg", "1.21", "μg kg−1", "未报道", "3", "正文 p.5；Fig. 2c", "TMeHg"),
      ("Hu2024_EP_Exp1", "铜仁汞污染碱性稻田土", "原土", "培养前", "THg", "51.14", "mg kg−1", "0.78（括号内，未说明 SD/SE）", "未报道", "Table 1（p.2）", "")]
EXCLUDED = [("Hu2024_EP", "盆栽实验（种植水稻 105 d）", "盆栽，有植物")]
