"""Hao et al. 2024, Science of the Total Environment 906: 167601。页码为 PDF 页码。"""
PAPER = {"文件名": "STOTEN_乙酸营养型与氢营养型产甲烷菌对稻田汞甲基化和甲基汞去甲基化的相对重要性.pdf", "第一作者": "Zhengdong Hao", "年份": "2024",
         "期刊": "Science of the Total Environment", "DOI": "10.1016/j.scitotenv.2023.167601",
         "文献核心问题": "乙酸营养型和氢营养型产甲烷菌对稻田土壤 HgII 甲基化和 MeHg 去甲基化的相对重要性。",
         "文献主要结论": "在背景区土壤中，刺激乙酸营养型产甲烷菌（NaAc）使 Km 升高；在汞矿区土壤中，H2/CO2 和 CH3F 处理使 Km 升高；两种产甲烷菌都参与 MeHg 去甲基化，矿区土壤中各处理的 Kd 都显著高于对照。"}
T1 = [{
    "实验编号": "Hao2024_STOTEN_Exp1", "实验名称": "Incubation experiments（2.2 节）", "实验类型": "B",
    "实验目的": "用 NaAc、H2/CO2 刺激或用 CH3F 抑制不同类型产甲烷菌，结合 202HgII/Me198Hg 示踪测 Km、Kd。",
    "采样地点": "贵州省：MM（万山废弃汞矿区，109°12′10.08″E，27°30′38.88″N）；BK（贵阳附近农村背景区，106°31′0.48″E，26°24′58.32″N）",
    "土壤数量": "2", "污染背景": "矿区污染（MM）+ 对照（BK）", "采样深度": "1–10 cm（土-水界面以下），2021年8月插秧后 50–60 d",
    "土样状态": "鲜土；装入无顶空的 1 L 气密棕色玻璃瓶，冷藏运输，4 °C 避光保存；MM 土保存30 d，BK 土保存5 d 后开始培养",
    "总汞": "需查 SI（Table S1）", "MeHg": "需查 SI（Table S1、S4）", "pH": "需查 SI", "有机质": "需查 SI", "硫酸盐": "需查 SI", "铁": "需查 SI",
    "处理组": "Control（未处理）；NaAc 5 mM（刺激乙酸营养型产甲烷菌）；H2/CO2（4:1，1.5 kPa，刺激氢营养型产甲烷菌）；CH3F 2%（抑制乙酸营养型产甲烷菌）；Abiotic（16 kGy γ 辐照）；所有处理均加 1 mM Na2MoO4",
    "外加汞形态": "仅示踪剂：202Hg(NO3)2、Me198HgNO3", "外加汞剂量": "202HgII 约为本底 THg 的10%；Me198Hg 约为本底 MeHg 的100%",
    "相对本底倍数": "202HgII 约 0.1 倍；Me198Hg 约 1 倍", "加汞后平衡": "未报道",
    "其他添加物": "NaAc 5 mM；H2/CO2（4:1，1.5 kPa）", "抑制剂": "Na2MoO4 1 mM（全部处理）；CH3F 2%", "灭菌对照": "有：γ 辐照 16 kGy",
    "土量g": "未报道（每瓶 30 mL 泥浆）", "水量mL": "未报道（泥浆含水率约 55%）", "土水比": "不确定（只报道含水率约 55%）",
    "容器": "100 mL 气密硼硅玻璃瓶", "密封方式": "未报道（原文称 gas-tight）", "气氛": "在充 N2 的无氧手套箱中进行",
    "预培养": "有：25 °C 避光预培养1周（手套箱内）", "温度": "25 °C（室温）", "避光": "是", "振荡": "未报道", "重复数": "3",
    "取样方式": "破坏性：先测顶空 CH4，再在手套箱中随机取3瓶",
    "示踪剂种类": "202Hg(NO3)2；Me198HgNO3", "示踪剂剂量": "202HgII 约为本底 THg 的10%；Me198Hg 约为本底 MeHg 的100%", "示踪剂预平衡": "未报道",
    "示踪培养时长": "12 h（实际 MeHg 取样时间为 4 h 和 16 h）", "是否测t0": "是（原文：“evaluated initially (t0) and after 4 or 16 h (ti)”）",
    "Km公式": "Km = ([Me202Hg]ti − [Me202Hg]t0) / ([202HgII] × (ti − t0))", "Kd公式": "Kd = (ln([Me198Hg]t0) − ln([Me198Hg]ti)) / (ti − t0)",
    "同位素测定": "GC-ICP-MS（Agilent 7700×），乙基化-吹扫捕集",
    "总培养时长d": "约 7.5（预培养 7 d + 示踪 12 h）", "取样时间点": "名义 0、12 h；实际 MeHg 为 4、16 h",
    "各时间点指标": "4/16 h：Me202Hg、Me198Hg（Km、Kd）；16 h：顶空 CH4；另测 S(−II)、FeII、FeIII、DOM、16S rRNA",
    "MeHg方法": "冷冻干燥、过 200 目筛后用 GC-ICP-MS 测同位素 MeHg；提取方法：需查 SI",
    "质控": "ERM-CC580 测得 MeHg 75.8 ± 6.6 μg⋅kg−1（n = 16），认证值 75.5 ± 3.7 μg⋅kg−1；同位素 MeHg 方法检出限（3σ）0.013 ng g−1；三个平行样偏差一般 < 15%",
    "Q_测t0": "是", "Q_示踪剂超本底": "否", "Q_示踪超24h": "否", "Q_灭菌对照": "是", "Q_严格厌氧": "是", "Q_透氧容器": "否",
    "原文摘录": ("【土量/水量】“The moisture content of the prepared slurries (BK and MM) was around 55 %. The prepared soil slurries (30 mL) were divided into 100 mL gas-tight borosilicate glass bottles for further incubation.”（p.2）\n"
              "【汞剂量】“The amounts of spiked 202HgII and Me198Hg tracers were ~ 10 % and ~ 100 % of soil ambient total Hg (THg) and MeHg, respectively”（p.3）\n"
              "【培养时长/取样】“The incubation was conducted in the dark at room temperature (25 ◦C) for 12 h … Two specific subsampling periods were set at the 0th and the 12th h during the incubation. However, due to the periods of incubation, bottle preparation, and subsampling, the actual time series for MeHg was 4, 16 h.”（p.3）\n"
              "【Km/Kd 公式】“Km = ([Me202Hg]ti − [Me202Hg]t0) / ([202HgII] × (ti − t0)) (1)；Kd = (ln([Me198Hg]t0) − ln([Me198Hg]ti)) / (ti − t0) (2)”（p.3）"),
    "需查SI字段": "本底 THg/MeHg（Table S1）、培养中 MeHg（Table S4）、示踪剂制备（Text S1）、计算细节（Text S2）、16 h 的 Km/Kd（Fig. S6）",
    "备注": "MM 土 Km（约 54 × 10−3 day−1）高于 BK，作者认为可能与 MM 土保存30 d 加预培养1周有关。正文只讨论第4 h 的数值。原文称示踪培养“for 12 h”，但实际取样到第16 h（不确定）。",
}]
_V = [("BK", "Km", ["7.48", "13.03", "7.14", "7.86", "(4.4)"], ["0.18", "0.84", "1.67", "1.32", None], "×10−3 day−1", "3a"),
      ("MM", "Km", ["54.1", "53.76", "(69)", "(90)", "(188)"], ["1.80", "0.86", None, None, None], "×10−3 day−1", "3b"),
      ("BK", "Kd", ["1.55", "1.96", "2.20", "2.55", "(4.3)"], ["0.19", "0.51", "0.05", "0.04", None], "day−1", "3c"),
      ("MM", "Kd", ["2.34", "3.76", "5.01", "5.41", "(13.6)"], ["0.10", "0.08", "0.12", "0.30", None], "day−1", "3d")]
T2 = []
for site, ind, vals, sds, unit, fig in _V:
    for trt, v, sd in zip(["Control", "NaAc", "H2/CO2", "CH3F", "Abiotic（γ 辐照）"], vals, sds):
        est = v.startswith("(")
        T2.append(("Hao2024_STOTEN_Exp1", site, trt, "4 h", ind, v, unit, "未估读" if est else f"± {sd}（SD/SE 未说明）", "3",
                   f"Fig. {fig}（p.6）" + ("，图中估读" if est else "；数值见正文 p.6–7"), "所有处理均含 1 mM Na2MoO4"))
EXCLUDED = []
