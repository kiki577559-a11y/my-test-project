"""Wu et al. 2020, Environmental Science & Technology（ASAP 版）。页码为 PDF 页码。
公式按页面渲染图核对；图3、图4、图2中的数值为估读。"""

SRC = "04_甲基化-去甲基化过程与微生物代谢/EST_产甲烷作用是控制采矿影响稻田土壤甲基汞浓度的重要过程.pdf"

PAPER = {
    "文件名": "EST_产甲烷作用是控制采矿影响稻田土壤甲基汞浓度的重要过程.pdf",
    "第一作者": "Qingqing Wu",
    "年份": "2020",
    "期刊": "Environmental Science & Technology",
    "DOI": "10.1021/acs.est.0c00268",
    "文献核心问题": "在汞污染梯度下（对照区、土法炼汞区、废弃汞矿区），不同微生物代谢途径（硫酸盐还原、产甲烷、铁还原）对稻田土壤汞甲基化和 MeHg 去甲基化的相对贡献。",
    "文献主要结论": "对照区 MeHg 生成主要由硫酸盐还原驱动；随汞浓度升高，产甲烷作用的作用变得重要且复杂；在汞矿区抑制产甲烷会使 MeHg 生成最多增加16.6倍、降解最多减少77%，说明产甲烷作用与 MeHg 降解有关。",
}

_EXC = (
    "【土量/水量】“Approximately 15 mL of slurries were dispensed into 100 mL serum bottles with three replicate samples for each treatment (triplicate reactions)”（p.4）；"
    "“…combined to prepare the slurry (water contents were 50−60%) in a 2-L beaker for each of the sampling sites.”（p.3）\n"
    "【汞剂量】“The addition of Hg isotopes increased THg and MeHg in soils by 10% and 100% of the ambient concentrations, respectively.”（p.3）\n"
    "【培养时长/取样】“After incubations for 24 h in the dark, samples were frozen at −20 °C immediately and then freeze-dried for isotopic Hg species analysis.”（p.4）\n"
    "【Km/Kd 公式】“km = ([Me202Hg]t2 − [Me202Hg]t0) / ([202Hg2+] × t) (1)”；“kd = (In([Me198Hg]t0) − In([Me198Hg]t2)) / t (2)”；"
    "“where [Me202Hg]t0 and [Me198Hg]t0 represent Me202Hg and Me198Hg concentrations at 0 h (initial concentration); [Me202Hg]t2 and [Me198Hg]t2 represent Me202Hg and Me198Hg concentrations in soils after incubation for 24 h; [202Hg2+] was the 202 Hg2+ concentration in the spike added to the soils; and [t] was the incubation time after spiking with isotopes.”（p.4–5；公式按页面图像核对，原文写作“In”）"
)

T1 = [{
    "实验编号": "Wu2020_EST_Exp1",
    "实验名称": "Incubation Experiment（原文 “Incubation Experiment Design”）",
    "实验类型": "B",
    "实验目的": "用代谢抑制剂/促进剂结合 202Hg(II)、Me198Hg 示踪，量化不同微生物代谢途径对稻田土壤甲基化和去甲基化的贡献。",
    "采样地点": "贵州省。Sikeng（废弃汞矿区，万山，E 109°12′18.36″，N 27°30′38.12″）；Gouxi（土法炼汞区，万山，E 109°13′30.86″，N 27°33′56.91″）；Huaxi（对照区，贵阳西南，E 106°32′1.46″，N 26°24′40.46″）",
    "土壤数量": "6（3个样点 × 表层土/根际土）",
    "污染背景": "矿区污染（Sikeng 废弃汞矿、Gouxi 土法炼汞）+ 对照（Huaxi）",
    "采样深度": "表层土 0−2 cm（土-水界面以下）；根际土 10−15 cm（附着在稻根上的土）",
    "土样状态": "鲜土；每样点3个独立样品与上覆水混合制成泥浆（去除根系和石子，未提及过筛）；4 °C 运输（24 h 内），4 °C 避光保存至培养，保存时长：未报道",
    "pH": "未报道",
    "有机质": "未报道",
    "总汞": "表层：Huaxi 0.46 ± 0.01，Gouxi 2.7 ± 1.5，Sikeng 57 ± 52 μg·g−1；根际：0.46 ± 0.02，3.2 ± 0.18，1.1 × 10² ± 1.4 × 10² μg·g−1（p.5）",
    "MeHg": "表层：1.2 ± 0.23，2.7 ± 0.84，0.9 ± 0.22 ng·g−1；根际：0.98 ± 0.29，3.0 ± 0.78，1.7 ± 1.4 ng·g−1（p.6）",
    "硫酸盐": "未报道",
    "铁": "未报道",
    "处理组": "7个处理（Table 1）：A Na2MoO4 1 mM（抑制硫酸盐还原）；B BES 5 mM（抑制产甲烷）；C Na2MoO4 + BES（1 + 5 mM）；D Na2SO4 1 mM（促进硫酸盐还原）；E FeOOH 1 mM（促进铁还原）；F control（不添加）；G autoclaved（121 °C，30 min，非生物对照）。Table 1 还列出抑制剂浓度梯度（Mo 1/5/10/20/50 mM；BES 5/10/20/50 mM），其结果见 Figure S1（需查 SI）",
    "外加汞形态": "仅同位素示踪剂：202Hg(NO3)2、CH3198HgNO3",
    "外加汞剂量": "示踪剂使 THg 增加本底的 10%，MeHg 增加本底的 100%",
    "相对本底倍数": "202Hg(II)：0.1 倍本底 THg；Me198Hg：1 倍本底 MeHg",
    "加汞后平衡": "未报道",
    "其他添加物": "Na2SO4 1 mM、FeOOH 1 mM（与示踪剂同时加入）",
    "抑制剂": "Na2MoO4 1 mM；BES 5 mM；Na2MoO4 + BES 1 + 5 mM",
    "灭菌对照": "有：高压灭菌 121 °C，30 min",
    "土量g": "未报道（每瓶约 15 mL 泥浆）",
    "水量mL": "未报道（泥浆含水率 50−60%）",
    "土水比": "不确定（只报道含水率 50−60%）",
    "容器": "100 mL 血清瓶（serum bottles），材质未报道",
    "密封方式": "丁基胶塞 + 铝盖压封（butyl rubber septa and aluminum crimp caps）",
    "气氛": "全程在厌氧箱内操作和培养（25 °C，90% Ar + 10% H2）",
    "预培养": "未报道",
    "温度": "25 °C",
    "避光": "是",
    "振荡": "未报道",
    "重复数": "3",
    "取样方式": "破坏性：24 h 后整瓶立即 −20 °C 冷冻并冻干",
    "示踪剂种类": "202Hg(NO3)2（ISOFLEX）；CH3198HgNO3（methylcobalamin 法自制）",
    "示踪剂剂量": "202Hg：本底 THg 的 10%；Me198Hg：本底 MeHg 的 100%",
    "示踪剂预平衡": "未报道",
    "示踪培养时长": "24 h",
    "是否测t0": "不确定（公式用 t0 浓度，原文称其为“initial concentration”，但未说明是否单独设 t0 样品实测）",
    "Km公式": "km = ([Me202Hg]t2 − [Me202Hg]t0) / ([202Hg2+] × t)",
    "Kd公式": "kd = (In([Me198Hg]t0) − In([Me198Hg]t2)) / t",
    "同位素测定": "GC-ICP-MS（Agilent 7700x），乙基化-吹扫捕集（ethylation−purge−trap）；测定 CH3198Hg+、CH3199Hg+、CH3200Hg+（内标）、CH3201Hg+、CH3202Hg+",
    "总培养时长d": "1（24 h）",
    "取样时间点": "0 h（不确定，见“是否测t0”）、24 h",
    "各时间点指标": "野外采样时（另取样品）：THg、MeHg；24 h：Me202Hg、Me198Hg（计算 km、kd）",
    "MeHg方法": "约 0.1 g 干土加 7.5 mL 25% HNO3 和 1.5 mL 饱和 CuSO4 消解，经萃取和反萃取后用 CVAFS（Brooks Rand Model III）测定；THg：王水 + BrCl 消解，CVAFS（Tekran 2500）测定",
    "质控": "标准物质 GBW07405（GSS-5）和 ERM-CC580；回收率 MeHg 75%–114%，THg 116%–118%；MeHg 同位素方法检出限（3σ）0.013 ng·L−1；平行样差异 MeHg <8.8%、THg <0.73%；加标回收率：未报道",
    "Q_测t0": "不确定",
    "Q_示踪剂超本底": "否（202Hg 为本底 THg 的 10%；Me198Hg 等于本底 MeHg）",
    "Q_示踪超24h": "否（24 h）",
    "Q_灭菌对照": "是",
    "Q_严格厌氧": "是",
    "Q_透氧容器": "否",
    "原文摘录": _EXC,
    "需查SI字段": "抑制剂浓度梯度测试结果（Figure S1）",
    "备注": "Huaxi km 在正文中给出的范围（10–80 × 10−3 day−1）与对照值 32 ± 3.3 × 10−3 一致。Gouxi kd 0.57 ± 0.33 / 0.21 ± 0.2 day−1 原文未写明是对照组，但与图3e、图4e 对照柱一致，按对照组记录。",
}]

S, R = "表层土 0–2 cm", "根际土 10–15 cm"
TRT = ["control", "Na2MoO4 1 mM", "BES 5 mM", "Na2MoO4+BES", "Na2SO4 1 mM", "FeOOH 1 mM", "autoclaved"]
# 图估读数值（control 用正文数值，其余为括号估读）
KM = {  # ×10−3 day−1
    (S, "Huaxi"):  ["32", "(12)", "(37)", "(19)", "(90)", "(29)", "(5)"],
    (S, "Gouxi"):  ["2.0", "(2.3)", "(4.8)", "(3.7)", "(10.5)", "(1.5)", "(1.1)"],
    (S, "Sikeng"): ["0.075", "(0.06)", "(1.25)", "(0.88)", "(0.06)", "(0.08)", "(0.15)"],
    (R, "Huaxi"):  ["15", "(16)", "(27)", "(15)", "(43)", "(18)", "(2.5)"],
    (R, "Gouxi"):  ["1.2", "(0.7)", "(1.2)", "(0.9)", "(2.8)", "(0.9)", "(0.3)"],
    (R, "Sikeng"): ["0.11", "(0.07)", "(0.76)", "(0.96)", "(0.18)", "(0.11)", "(0.27)"],
}
KM_SD = {(S, "Huaxi"): "3.3", (S, "Gouxi"): "1.37", (S, "Sikeng"): "0.0072",
         (R, "Huaxi"): "2.2", (R, "Gouxi"): "0.87", (R, "Sikeng"): "0.014"}
KD = {  # day−1
    (S, "Huaxi"):  ["0.82", "(0.48)", "(0.28)", "(0.28)", "(0.47)", "(0.80)", "(0.32)"],
    (S, "Gouxi"):  ["0.57", "(0.46)", "(0.13)", "(0.17)", "(0.58)", "(0.82)", "(0.47)"],
    (S, "Sikeng"): ["0.81", "(0.87)", "(0.57)", "(0.65)", "(0.99)", "(0.79)", "(0.55)"],
    (R, "Huaxi"):  ["0.80", "(0.54)", "(0.40)", "(0.45)", "(0.85)", "(0.72)", "(0.30)"],
    (R, "Gouxi"):  ["0.21", "(0.38)", "(0.11)", "(0.20)", "(0.76)", "(0.38)", "(0.49)"],
    (R, "Sikeng"): ["0.70", "(1.01)", "(0.44)", "(0.40)", "(0.47)", "(0.45)", "(0.85)"],
}
KD_SD = {(S, "Huaxi"): "0.13", (S, "Gouxi"): "0.33", (S, "Sikeng"): "0.08",
         (R, "Huaxi"): "0.14", (R, "Gouxi"): "0.2", (R, "Sikeng"): "0.19"}

T2 = []
for (layer, site), vals in KM.items():
    fig = "Fig. 3a–c（p.5）" if layer == S else "Fig. 4a–c（p.6）"
    for t, v in zip(TRT, vals):
        est = v.startswith("(")
        T2.append(("Wu2020_EST_Exp1", f"{site} {layer}", t, "24 h", "Km", v, "×10−3 day−1",
                   "未估读" if est else f"SD {KM_SD[(layer, site)]}", "3",
                   fig + ("，图中估读" if est else "；数值见正文 p.7"), ""))
for (layer, site), vals in KD.items():
    fig = "Fig. 3d–f（p.5）" if layer == S else "Fig. 4d–f（p.6）"
    for t, v in zip(TRT, vals):
        est = v.startswith("(")
        note = "原文未明确是对照组，与图中对照柱一致" if (not est and site == "Gouxi") else ""
        T2.append(("Wu2020_EST_Exp1", f"{site} {layer}", t, "24 h", "Kd", v, "day−1",
                   "未估读" if est else f"SD {KD_SD[(layer, site)]}", "3",
                   fig + ("，图中估读" if est else "；数值见正文 p.7"), note))

# 野外原样（培养前）THg、MeHg、%MeHg
AMB = [
    (S, "Huaxi", "0.46", "0.01", "1.2", "0.23", "(0.27)"),
    (S, "Gouxi", "2.7", "1.5", "2.7", "0.84", "(0.077)"),
    (S, "Sikeng", "57", "52", "0.9", "0.22", "(0.0022)"),
    (R, "Huaxi", "0.46", "0.02", "0.98", "0.29", "(0.22)"),
    (R, "Gouxi", "3.2", "0.18", "3.0", "0.78", "(0.097)"),
    (R, "Sikeng", "1.1 × 10²", "1.4 × 10²", "1.7", "1.4", "(0.0025)"),
]
for layer, site, thg, thg_sd, mehg, mehg_sd, pct in AMB:
    soil = f"{site} {layer}"
    T2.append(("Wu2020_EST_Exp1", soil, "野外原样（培养前）", "培养前", "THg", thg, "μg·g−1", f"SD {thg_sd}", "3", "正文 p.5；Fig. 2a/d", ""))
    T2.append(("Wu2020_EST_Exp1", soil, "野外原样（培养前）", "培养前", "MeHg", mehg, "ng·g−1", f"SD {mehg_sd}", "3", "正文 p.6；Fig. 2b/e", ""))
    T2.append(("Wu2020_EST_Exp1", soil, "野外原样（培养前）", "培养前", "%MeHg", pct, "%", "未估读", "3", "Fig. 2c/f（p.4），图中估读", "Sikeng 读自放大插图"))

EXCLUDED = [("Wu2020_EST", "抑制剂浓度梯度预实验（Table 1 中 Mo 5–50 mM、BES 10–50 mM）",
             "结果只在 Figure S1（SI）中，SI 未提供；且属于确定抑制剂浓度的预实验，未单独记录")]
