"""Du et al. 2019, Environmental Pollution 253: 424–428。
原文摘录中的 μ、°、– 等符号已按页面渲染图核对（PDF 文字层把 μg 识别成 mg，见备注）。"""

SRC = "05_环境驱动因子与汞生物有效性/EP_稻田土壤甲基汞生成的动力学特征及预测模型.pdf"

PAPER = {
    "文件名": "EP_稻田土壤甲基汞生成的动力学特征及预测模型.pdf",
    "第一作者": "Shuyang Du",
    "年份": "2019",
    "期刊": "Environmental Pollution",
    "DOI": "10.1016/j.envpol.2019.07.050",
    "文献核心问题": "外源无机汞加入不同性质的稻田土壤后，淹水条件下 MeHg 生成的动力学特征是什么，能否用常规土壤性质和淹水时间预测汞甲基化效率。",
    "文献主要结论": "汞甲基化效率（kME，即 MeHg/THg）随淹水时间增加，约30 d 达到相对稳定；Elovich 方程能较好描述 MeHg 生成；用原位 pH、Eh，或用有机质含量加淹水时间建立的模型分别解释78%和68%的变异。",
}

T1 = [{
    "实验编号": "Du2019_EP_Exp1",
    "实验名称": "未单独命名（2.1 节 Soil description and experimental design）",
    "实验类型": "A",
    "实验目的": "研究外源 Hg(II) 在18种稻田土淹水90 d 过程中的甲基化动力学，建立 kME 预测模型。",
    "采样地点": "中国主要水稻产区；原文未给出省、市和坐标（各土壤信息见 Table S1，需查 SI）",
    "土壤数量": "18",
    "污染背景": "人为加汞（HgCl2，5 mg/kg）；各土壤的本底汞污染情况：需查 SI",
    "采样深度": "0–20 cm",
    "土样状态": "风干、均质、过 2 mm 筛；保存温度和时长：未报道",
    "pH": "需查 SI（Table S1）",
    "有机质": "需查 SI（Table S1；原文测的是 organic matter，重铬酸钾油浴法）",
    "总汞": "需查 SI",
    "MeHg": "需查 SI",
    "硫酸盐": "需查 SI（Table S1）",
    "铁": "需查 SI（Table S1，游离 Fe/Mn/Al，DCB 法）",
    "处理组": "每种土只有一个处理：加 HgCl2（Hg(II) 5 mg/kg）后淹水培养；未设不加汞对照",
    "外加汞形态": "HgCl2",
    "外加汞剂量": "5 mg/kg（以 Hg(II) 计）",
    "相对本底倍数": "需查 SI（各土本底 THg 未在正文给出）",
    "加汞后平衡": "未报道",
    "其他添加物": "无",
    "抑制剂": "无",
    "灭菌对照": "无",
    "土量g": "1000（每种土 1 kg）",
    "水量mL": "未报道（只说明加去离子水形成 2 cm 水层）",
    "土水比": "未报道",
    "容器": "玻璃烧杯（glass beaker），体积未报道",
    "密封方式": "未报道",
    "气氛": "未报道（未提及手套箱或充气）",
    "预培养": "未报道",
    "温度": "25 °C",
    "避光": "是",
    "振荡": "未报道",
    "重复数": "3",
    "取样方式": "不确定（原文只说在各时间点采集土样；每种土只有3个烧杯却有7个时间点，但没有明确是否在同一烧杯分次取样）",
    "示踪剂种类": "无",
    "示踪剂剂量": "无",
    "示踪剂预平衡": "无",
    "示踪培养时长": "无",
    "是否测t0": "无",
    "Km公式": "无（文中 kME = MeHgsoil / THgsoil，是甲基化比例，不是速率常数）",
    "Kd公式": "无",
    "同位素测定": "无",
    "总培养时长d": "90",
    "取样时间点": "1, 3, 7, 14, 30, 60, 90 d",
    "各时间点指标": "培养前（风干土）：pH、CEC、OM、硫酸盐、黏粒、游离 Fe/Mn/Al、THg、Se、hgcA qPCR；d1/3/7/14/30/60/90：原位 pH、原位 Eh、MeHg（并计算 kME）；THg 测定时间点：未报道",
    "MeHg方法": "25% KOH/methanol（w/w）65 °C 振荡 4 h 消解；GC-CVAFS（Brooks Rand）测定，USEPA Method 1630",
    "质控": "标准物质 GBW07407（THg、Se）测得 THg 716 ± 11 μg/kg（认证值 740 ± 110 μg/kg）；ERM-CC580（MeHg）测得 73 ± 5.7 μg/kg（认证值 75.5 ± 4 μg/kg）；加标回收率：未报道；检出限：不确定（原文写“LOD and LOQ … were 2.0 μg/kg and 0.2 pg, respectively”，指代有歧义）",
    "Q_测t0": "否",
    "Q_示踪剂超本底": "不适用（无同位素）",
    "Q_示踪超24h": "不适用（无同位素）",
    "Q_灭菌对照": "否",
    "Q_严格厌氧": "未报道",
    "Q_透氧容器": "未报道",
    "原文摘录": (
        "【土量/汞剂量】“One kilogram of each soil type was spiked with Hg(II) (5 mg/kg) using HgCl2 solution to ensure sufficient MeHg production (Peng et al., 2012) and placed into a glass beaker; each soil type was evaluated in triplicate.”（p.2）\n"
        "【水量】“Deionized water was added to form a 2 cm water layer on the soil surface.”（p.2）\n"
        "【培养时长】“All beakers were incubated in the dark at 25 °C for 90 d.”（p.2）\n"
        "【取样时间点】“The soil pH and Eh were measured in situ at time intervals of 1, 3, 7, 14, 30, 60, and 90 d during the incubation period. In the meantime, soil samples were collected to determine the MeHg concentration.”（p.2）\n"
        "【Km/Kd 公式】无 Km/Kd；甲基化效率：“The Hg methylation efficiency (kME) was calculated by Eq. (1): kME = MeHgsoil/THgsoil”（p.2）"
    ),
    "需查SI字段": "采样地点、各土壤理化性质（Table S1）、本底 THg/MeHg、相对本底倍数、动力学方程参数 a、b（Table S2）",
    "备注": "PDF 文字层把 μg/kg 错误识别为 mg/kg，已按页面渲染图核对为 μg/kg。摘要写 30 d 时甲基化效率为 0.08%–2.52%，正文写最终值为 0.08%–2.31%（平均 0.82%），两者不一致，表2中都已记录并标注。",
}]

# 表2：(实验编号, 土壤, 处理, 时间点, 指标, 数值原文, 原单位, SD/SE, n, 出处, 备注)
_fig1 = [("1 d", "(0.02)"), ("3 d", "(0.06)"), ("7 d", "(0.12)"), ("14 d", "(0.28)"),
         ("30 d", "(0.86)"), ("60 d", "(0.88)"), ("90 d", "(0.72)")]
T2 = [("Du2019_EP_Exp1", "18种土（中位数）", "HgCl2 5 mg/kg", t, "%MeHg", v, "%", "未报道", "18种土",
       "Fig. 1（p.2），图中估读", "箱线图中位线；kME = MeHg/THg") for t, v in _fig1]
T2 += [
    ("Du2019_EP_Exp1", "18种土（范围）", "HgCl2 5 mg/kg", "终点（原文“final”，未明确天数）", "%MeHg", "0.08–2.31", "%", "未报道", "18种土",
     "正文 p.2", "平均值 0.82%"),
    ("Du2019_EP_Exp1", "18种土（平均）", "HgCl2 5 mg/kg", "终点（原文“final”，未明确天数）", "%MeHg", "0.82", "%", "未报道", "18种土",
     "正文 p.2", ""),
    ("Du2019_EP_Exp1", "18种土（范围）", "HgCl2 5 mg/kg", "30 d（原文 “reached a relatively steady state at 30 d”）", "%MeHg", "0.08–2.52", "%", "未报道", "18种土",
     "摘要 p.1", "不确定：与正文的最终范围 0.08%–2.31% 不一致"),
]

EXCLUDED = []  # 本文没有被排除的实验
