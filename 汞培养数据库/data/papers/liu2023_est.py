"""Liu et al. 2023, Environ. Sci. Technol. 57: 8149−8160。页码为 PDF 页码。图1数值为估读。"""
PAPER = {"文件名": "EST_汞与硫的氧化还原循环影响污染梯度稻田土壤甲基汞水平.pdf", "第一作者": "Jiang Liu", "年份": "2023",
         "期刊": "Environmental Science & Technology", "DOI": "10.1021/acs.est.3c02676",
         "文献核心问题": "在汞污染梯度稻田土壤中，硫输入（硫酸盐、硫代硫酸盐）如何影响汞的甲基化、去甲基化、氧化和还原等转化过程。",
         "文献主要结论": "多化合物同位素标记显示，暗条件下存在微生物介导的 HgII 还原、Hg0 甲基化和 MeHg 氧化去甲基化-还原；在低、中污染样点，加硫促进甲基化、抑制 HgII 还原；在高污染样点 SK，加硫抑制甲基化和还原、促进去甲基化。"}
T1 = [{
    "实验编号": "Liu2023_EST_Exp1", "实验名称": "Incubation Experiment（2.3 Incubation Experiment Design）", "实验类型": "B",
    "实验目的": "用 200HgII、Me198Hg、202Hg0 三种示踪剂，同时追踪不同硫处理下汞甲基化、去甲基化、还原和氧化过程。",
    "采样地点": "贵州省：SK（废弃汞矿区，E 109°12′38″，N 27°31′2″）；GX（土法炼汞区，E 109°11′30″，N 27°33′50″）；HX（贵阳附近农村对照，E 106°31′28″，N 26°25′20″）",
    "土壤数量": "3", "污染背景": "矿区污染（SK、GX）+ 对照（HX）", "采样深度": "1−5 cm（表层土）",
    "土样状态": "鲜土，与上覆水一起采集；保存条件见 Text S3（需查 SI）",
    "总汞": "HX 0.15 ± 0.003，GX 17.2 ± 1.7，SK 609 ± 7 mg kg−1（p.5）", "MeHg": "需查 SI",
    "pH": "需查 SI", "有机质": "需查 SI", "硫酸盐": "需查 SI", "铁": "需查 SI",
    "处理组": "control；Na2SO4；Na2S2O3（两种硫处理每瓶都加 2 mg S）；autoclaved（121 °C，30 min）",
    "外加汞形态": "仅示踪剂：200HgII、Me198Hg、202Hg0", "外加汞剂量": "按各样点本底汞浓度确定（Table S1，需查 SI）",
    "相对本底倍数": "需查 SI", "加汞后平衡": "无（加示踪剂后立即密封）",
    "其他添加物": "Na2SO4 或 Na2S2O3（每瓶 2 mg S，与示踪剂同时加入）", "抑制剂": "无", "灭菌对照": "有：高压灭菌 121 °C，30 min",
    "土量g": "未报道（每瓶 30 mL 泥浆）", "水量mL": "未报道（泥浆含水率约 75%）", "土水比": "不确定（只报道含水率约 75%）",
    "容器": "100 mL 硼硅玻璃血清瓶", "密封方式": "未报道（原文只写“immediately sealed”）",
    "气氛": "在无氧手套箱中配制泥浆和培养", "预培养": "未报道", "温度": "25 °C", "避光": "是（铝箔包裹）", "振荡": "加示踪剂后轻摇混匀",
    "重复数": "3", "取样方式": "破坏性：每个时间点随机取3瓶",
    "示踪剂种类": "200HgII、Me198Hg、202Hg0", "示踪剂剂量": "需查 SI（Table S1）", "示踪剂预平衡": "无", "示踪培养时长": "48 h",
    "是否测t0": "不确定（名义上在 0 h 取样，但原文说明 MeHg 的实际取样时间为 4、18、28、52 h）",
    "Km公式": "需查 SI（用不可逆准一级模型计算，见 Text S6）", "Kd公式": "需查 SI（Text S6）",
    "同位素测定": "需查 SI（Text S4）；ICP-MS 汞检出限 10 pg",
    "总培养时长d": "2（48 h）", "取样时间点": "名义 0、12、24、48 h；实际 MeHg 为 4、18、28、52 h，可吹扫 Hg0 为 2、14、26、50 h",
    "各时间点指标": "各时间点：同位素 Hg0（198/200/202Hg0）、同位素 MeHg（Me198/200/202Hg）；培养后：HS−/SO4 2−、NO3−/NH4+、Fe2+/Fe3+、DOM 浓度和光谱、hgcA/merA/merB/dsrB/soxB qPCR、hgcA 扩增子测序和宏基因组",
    "MeHg方法": "需查 SI（Text S4）",
    "质控": "ERM-CC580 的 MeHg 回收率为 76.2%–108.4%（平均 85.2% ± 9.07%，n = 26）；每10个样品做平行样，RSD < 10%；ICP-MS 汞检出限 10 pg",
    "Q_测t0": "不确定", "Q_示踪剂超本底": "需查 SI", "Q_示踪超24h": "是（48 h）", "Q_灭菌对照": "是", "Q_严格厌氧": "是", "Q_透氧容器": "否",
    "原文摘录": ("【土量/水量】“Each homogenized slurry (30 mL) was weighed into a serum bottle. The moisture content of the prepared slurries (SK, GX and HX) was around 75% (Text S3).”（p.2）\n"
              "【汞剂量】“Isotope-enriched 200HgII, Me198Hg, and 202Hg0 tracers were spiked into all incubation bottles; the spiking dosage of Hg tracers depended on the ambient Hg concentration at each site (Table S1).”（p.2）\n"
              "【培养时长/取样】“The total period of incubation was 48 h (at 25 °C in the glovebox), and three random bottles (triplicates for each site and each treatment) were destructively sampled at 0 h, 12, 24, and 48 h. However, due to the periods of incubation, bottle preparation, and subsampling, the actual time series for purgeable Hg0 was 2, 14, 26, and 50 h, and for MeHg, it was 4, 18, 28, and 52 h (see Text S4.1).”（p.2）\n"
              "【Km/Kd 公式】“…were calculated from [MeiHg], [iHg0] (i = 198, 200, and 202), and the amounts of spiked Hg tracers using an irreversible pseudo-first-order model. … The calculation details and assumptions made for the irreversible pseudo-first-order model are shown in Text S6.”（p.3）"),
    "需查SI字段": "示踪剂剂量（Table S1）、泥浆制备（Text S3）、测定方法（Text S4）、Km/Kd 公式（Text S6）",
    "备注": "图1横轴标为 4、16、28、52 h，但正文写 MeHg 实际取样时间为 4、18、28、52 h（不确定）；表2按图上的标签记录。Km-202Hg0（Hg0 甲基化）和挥发速率常数 Kv 没有列入表2（不属于规定的5项指标）。",
}]
_T = ["4 h", "16 h（正文为18 h）", "28 h", "52 h"]
_KM = {"HX": {"autoclaved": ["(0.004)", "(0.001)", "(0.012)", "(0.005)"], "control": ["(0.176)", "(0.04)", "(0.015)", "(0.089)"],
              "Na2SO4": ["0.29", "(0.057)", "(0.012)", "(0.008)"], "Na2S2O3": ["(0.233)", "(0.06)", "(0.012)", "(0.01)"]},
       "GX": {"autoclaved": ["(0.0025)", "(0.0008)", "(0.0002)", "(0.0002)"], "control": ["(0.036)", "(0.0065)", "(0.008)", "(0.005)"],
              "Na2SO4": ["0.048", "(0.015)", "(0.011)", "(0.006)"], "Na2S2O3": ["0.048", "(0.0155)", "(0.0135)", "(0.007)"]},
       "SK": {"autoclaved": ["(0.00055)", "(0.00013)", "(0.00008)", "(0.00004)"], "control": ["0.0015", "(0.00027)", "(0.00025)", "(0.00014)"],
              "Na2SO4": ["(0.00087)", "(0.00035)", "(0.00027)", "(0.00012)"], "Na2S2O3": ["(0.00104)", "(0.00036)", "(0.00026)", "(0.0001)"]}}
_SD = {("HX", "Na2SO4"): "SE 0.01", ("GX", "Na2SO4"): "SE 0.006", ("GX", "Na2S2O3"): "SE 0.006", ("SK", "control"): "SE 0.00002"}
_KD = {"HX": {"autoclaved": ["(0.0)", "(0.08)", "(0.12)", "(0.25)"], "control": ["4.03", "(1.32)", "(1.53)", "(0.78)"],
              "Na2SO4": ["(1.78)", "(1.0)", "(1.52)", "(0.72)"], "Na2S2O3": ["(2.63)", "(1.1)", "(1.6)", "(0.85)"]},
       "GX": {"autoclaved": ["(0.0)", "(0.03)", "(0.1)", "(0.08)"], "control": ["(1.38)", "(1.15)", "(0.45)", "(0.36)"],
              "Na2SO4": ["(2.65)", "(0.65)", "(0.65)", "(0.52)"], "Na2S2O3": ["(0.73)", "(0.42)", "(0.38)", "(0.4)"]},
       "SK": {"autoclaved": ["(2.2)", "(0.3)", "(0.25)", "(0.15)"], "control": ["(6.9)", "(1.5)", "(1.25)", "(0.65)"],
              "Na2SO4": ["(9.3)", "(2.8)", "(1.4)", "(0.9)"], "Na2S2O3": ["(9.0)", "(2.4)", "(1.2)", "(0.75)"]}}
T2 = []
for ind, D, panel in (("Km", _KM, "a–c"), ("Kd", _KD, "g–i")):
    for site, trts in D.items():
        for trt, vals in trts.items():
            for t, v in zip(_T, vals):
                est = v.startswith("(")
                sd = "SE（未估读）" if est else (_SD.get((site, trt), "SE 0.62") if t == "4 h" else "未报道")
                T2.append(("Liu2023_EST_Exp1", site, trt, t, ind, v, "d−1", sd, "3",
                           f"Fig. 1{panel}（p.3）" + ("，图中估读" if est else "；数值见正文 p.5"),
                           "Km-200HgII" if ind == "Km" else "Kd-Me198Hg"))
for site, v, sd in (("HX", "0.15", "0.003"), ("GX", "17.2", "1.7"), ("SK", "609", "7")):
    T2.append(("Liu2023_EST_Exp1", site, "野外原样", "培养前", "THg", v, "mg/kg", "± " + sd + "（SD/SE 未说明）", "未报道", "正文 p.5", ""))
EXCLUDED = []
