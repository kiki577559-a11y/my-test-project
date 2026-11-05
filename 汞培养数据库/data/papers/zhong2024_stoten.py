"""Zhong et al. 2024, Science of the Total Environment 927: 172335。页码为 PDF 页码。
km/kd 公式按页面渲染图核对；图1插图、图4a 中的数值为估读。"""

SRC = "05_环境驱动因子与汞生物有效性/STOTEN_汞供应限制稻田土壤甲基汞的产生.pdf"

PAPER = {
    "文件名": "STOTEN_汞供应限制稻田土壤甲基汞的产生.pdf",
    "第一作者": "Huan Zhong",
    "年份": "2024",
    "期刊": "Science of the Total Environment",
    "DOI": "10.1016/j.scitotenv.2024.172335",
    "文献核心问题": "在秸秆还田情景下，稻田土壤汞甲基化的限制因素是微生物活性，还是无机汞的供应。",
    "文献主要结论": "无机汞供应是稻田汞甲基化的限制因素：秸秆添加使溶解态 THg 提高 336%–747%；SRB 是非污染稻田的主要甲基化菌，但 SRB 活性本身不限制甲基化；FeRB 通过调节汞的迁移性影响甲基化。",
}

_COMMON = dict(
    采样地点="12个省份（各省稻田面积合计占全国 83%）；具体地点和坐标见 Fig. S1（需查 SI）",
    污染背景="一般农田（原文称 uncontaminated paddy soils）；未加汞",
    采样深度="1–13 cm",
    土样状态="鲜土；冰盒运回，研磨、过 2 mm 筛，4 °C 冷藏保存；保存时长：未报道",
    pH="需查 SI（Fig. S3 为培养后上覆水 pH）",
    有机质="需查 SI",
    总汞="需查 SI；正文讨论中提到 Experiment II 的8个土壤 THg 为 41–373 μg/kg（p.6）",
    MeHg="未加秸秆培养21 d 后为 0.44–0.92 μg/kg（省级尺度，见表2）；初始值：需查 SI",
    硫酸盐="需查 SI",
    铁="需查 SI",
    外加汞形态="无（未外加汞；仅在测 km/kd 时加同位素示踪剂）",
    外加汞剂量="无",
    相对本底倍数="无",
    加汞后平衡="无",
    其他添加物="稻草粉 1%（过 150 μm 筛；秸秆 THg 30.9 ± 0.2 μg/kg，MeHg 2.7 ± 0.1 μg/kg），培养开始时加入",
    灭菌对照="无",
    土量g="5（干重）",
    水量mL="30",
    土水比="1:6（5 g : 30 mL，按原文数值计算）",
    容器="50 mL 聚丙烯离心管（Corning）",
    预培养="未报道",
    温度="28 °C",
    避光="是",
    振荡="未报道",
    重复数="3",
    MeHg方法="0.5–0.8 g 湿土加 2 mL 25%（w/w）KOH-CH3OH，70 °C、230 rpm 避光提取 4 h；用 Brooks Rand model III 测定（EPA Method 1630）",
    质控="ERM-CC580（MeHg 75 ± 4 μg/kg）回收率 87%–104%；同位素分析中 ERM-CC580 回收率 86.5% ± 6.7%（n = 15，77.6%–98.1%）；MeHg 检出限 0.05 pg；加标回收率：未报道",
)

_KM_EXC = ("【Km/Kd 公式】“km = [Me202Hg+]tx / ([202Hg2+]t0 · t) (1)”；“kd = (ln[Me199Hg+]t0 − ln[Me199Hg+]tx) / t (2)”；"
           "“Where [MeHg+] and [Hg+] represent the concentration of MeHg and IHg; t0 refers to the start time, tx is referred to as the end time, and t is the incubation time (24 h).”（p.3；公式按页面图像核对）\n"
           "【示踪剂】“On each sampling day, 20–50 μL of 202Hg and Me199Hg were added at concentrations of 10–80 % of ambient THg and MeHg levels, and then the soils were mixed and incubated for 24 h.”（p.3）")

_TRACER = dict(
    示踪剂种类="202Hg（无机）、Me199Hg",
    示踪剂剂量="每管加 20–50 μL，浓度为本底 THg 和 MeHg 的 10%–80%",
    示踪剂预平衡="未报道",
    示踪培养时长="24 h",
    是否测t0="不确定（公式用 [202Hg2+]t0，未说明是否实测 t0 样品）",
    Km公式="km = [Me202Hg+]tx / ([202Hg2+]t0 · t)",
    Kd公式="kd = (ln[Me199Hg+]t0 − ln[Me199Hg+]tx) / t",
    同位素测定="GC-ICP-MS（PerkinElmer NexION300）；Me201Hg 作内标，Me200Hg 用于计算本底 MeHg",
    Q_测t0="不确定",
    Q_示踪剂超本底="否（10%–80% 本底）",
    Q_示踪超24h="否（24 h）",
)
_NOTRACER = dict(示踪剂种类="无", 示踪剂剂量="无", 示踪剂预平衡="无", 示踪培养时长="无", 是否测t0="无",
                 Km公式="无", Kd公式="无", 同位素测定="无",
                 Q_测t0="不适用（无同位素）", Q_示踪剂超本底="不适用（无同位素）", Q_示踪超24h="不适用（无同位素）")

T1 = [
    {**_COMMON, **_TRACER,
     "实验编号": "Zhong2024_STOTEN_Exp1",
     "实验名称": "Incubation experiment I-Spatial variations",
     "实验类型": "A+B",
     "实验目的": "在全国尺度上量化秸秆添加对 MeHg 生成及 km、kd 的影响。",
     "土壤数量": "63",
     "处理组": "CK（不加秸秆）；RS（加 1% 稻草）",
     "抑制剂": "无",
     "密封方式": "未报道（原文只写“the tubes were sealed”）",
     "气氛": "未报道（在人工气候箱中培养；培养结束后在厌氧手套箱中开盖分离上覆水和土）",
     "取样方式": "破坏性：第21 d 整管离心分离",
     "总培养时长d": "21",
     "取样时间点": "21 d（km、kd 示踪培养另在第21 d 加入示踪剂后再培养 24 h）",
     "各时间点指标": "d21：上覆水 pH、Eh、DOC、硫酸盐；土壤含水量、MeHg、HCl 提取态 Fe(II)、hgcA qPCR（Deltaproteobacteria、Archaea）、km、kd",
     "Q_灭菌对照": "否",
     "Q_严格厌氧": "否（培养在人工气候箱中进行，未报道充气；仅分离步骤在手套箱内）",
     "Q_透氧容器": "是（聚丙烯离心管）",
     "原文摘录": ("【土量/水量】“Specifically, 5 g of soil (dry weight) with or without straw powder was put into a 50-mL polypropylene centrifuge tube (Corning, USA). Then 30 mL of deionized water was added to each tube.”（p.2）\n"
              "【培养时长】“After thorough mixing, the tubes were sealed and subjected to a 21-d incubation in an artificial climate chamber (28 ◦C in the dark).”（p.2）\n"
              "【汞剂量】未外加汞。\n" + _KM_EXC),
     "需查SI字段": "采样地点（Fig. S1）、土壤理化性质、初始 THg/MeHg、各省份的具体数值",
     "备注": "原文 km 单位写作“%/d”（正文）或“*10−2, /d”（图1），两者等价。图1的分省份箱线图（12个省 × CK/RS × MeHg/km/kd）未逐一估读，只记录了正文数值和全国插图的中位数。",
     },
    {**_COMMON, **_TRACER,
     "实验编号": "Zhong2024_STOTEN_Exp2",
     "实验名称": "Incubation experiment II-Temporal variations",
     "实验类型": "A+B",
     "实验目的": "在8个土壤中追踪秸秆添加后 MeHg、km/kd、溶解态 THg、铁还原和 DOM 组成的时间动态。",
     "土壤数量": "8（CZ、HK、HY、HZ、NC、MDJ、TR、YA）",
     "处理组": "CK；RS（1% 稻草）",
     "抑制剂": "无",
     "密封方式": "未报道（“as described above”，同 Exp1）",
     "气氛": "未报道（同 Exp1）",
     "取样方式": "破坏性：每个时间点随机取3管离心",
     "总培养时长d": "35",
     "取样时间点": "7, 14, 21, 35 d（DOM 光谱另含 0 d）",
     "各时间点指标": "d0/7/14/21：DOM 荧光光谱；d7/14/21/35：上覆水溶解态 THg、土壤 HCl 提取态 Fe(II)、MeHg、km、kd（结果见 Fig. S8–S9）；d21：16S rRNA 测序（338F/806R）",
     "Q_灭菌对照": "否",
     "Q_严格厌氧": "否（同 Exp1）",
     "Q_透氧容器": "是（聚丙烯离心管）",
     "原文摘录": ("【土量/水量/处理】“Two treatments, CK (soil without rice straw) and RS (soil +1 % rice straw amendment), were set as described above.”（p.3）\n"
              "【取样时间点】“After incubation for 7, 14, 21, and 35 days, three tubes from each treatment were randomly selected and centrifuged to separate soil particles from the overlying water.”（p.3）\n"
              "【汞剂量】未外加汞。\n" + _KM_EXC),
     "需查SI字段": "各时间点 MeHg、km、kd、溶解态 THg 的数值（Fig. S7–S10）；土壤性质",
     "备注": "正文只给出相对变化（如 MeHg 在第7/14/21/35 d 分别增加 13.5%–189%、18.4%–113.1%、2.7%–163%、20.1%–709.5%），这些不是表2规定的指标，未列入表2。km/kd 是否在每个时间点都测定：不确定（方法写“On each sampling day”，结果写“during the 35-day incubation period (Figs. S8–9)”）。",
     },
    {**_COMMON, **_NOTRACER,
     "实验编号": "Zhong2024_STOTEN_Exp3",
     "实验名称": "Incubation experiment III-Metabolism inhibition assays",
     "实验类型": "A",
     "实验目的": "用代谢抑制剂区分 SRB 和产甲烷菌对秸秆促进 MeHg 生成的贡献。",
     "土壤数量": "8（同 Exp2）",
     "处理组": "CK（不加抑制剂和秸秆）；RS（1% 稻草）；RS-SRB（1% 稻草 + 20 mM 钼酸盐）；RS-Meth（1% 稻草 + 30 mM BES）",
     "抑制剂": "钼酸盐 20 mM（抑制 SRB）；bromoethanesulfonate（BES）30 mM（抑制产甲烷菌）",
     "密封方式": "离心管盖预先打孔，孔用硅橡胶密封（用于抽取顶空气体测 CH4）",
     "气氛": "未报道",
     "取样方式": "破坏性：第21 d 先测顶空 CH4，再整管离心",
     "总培养时长d": "21",
     "取样时间点": "21 d",
     "各时间点指标": "d21：顶空 CH4（GC）、土壤 MeHg、HCl 提取态 Fe(II)、上覆水硫酸盐",
     "Q_灭菌对照": "否",
     "Q_严格厌氧": "未报道",
     "Q_透氧容器": "是（聚丙烯离心管 + 硅橡胶密封）",
     "原文摘录": ("【土量/水量】“Specifically, 5 g of soil (dry weight) was re-suspended in 30 mL deionized water in a 50 mL centrifuge tube, with the additions of specific inhibitors described above.”（p.3）\n"
              "【密封】“The caps of the centrifuge tubes were pre-punched, and then the hole was sealed with silicone rubber, from which air was sampled using an injection syringe for CH4 determination”（p.3）\n"
              "【培养时长】“After 21 days of incubation, all tubes were used to measure the methane production in the air (indicating methanogen activities) first and then centrifuged (4000 rpm, 20 min) to separate the soil and the overlying water.”（p.3）\n"
              "【汞剂量】未外加汞。\n【Km/Kd 公式】本实验未测。"),
     "需查SI字段": "硫酸盐、Fe(II)、CH4 的结果（Fig. S14）；土壤性质",
     "备注": "Exp3 的方法中没有单独写培养温度和是否避光，因此这两项填“不确定”（Exp1 为 28 °C 避光）。",
     "温度": "不确定（Exp3 未单独写明；Exp1 为 28 °C）",
     "避光": "不确定（Exp3 未单独写明）",
     },
]

T2 = [
    ("Zhong2024_STOTEN_Exp1", "63种土（省级尺度范围）", "CK", "21 d", "MeHg", "0.44–0.92", "μg/kg", "未报道", "未报道", "正文 p.4；Fig. 1a", "原文“on a provincial scale”"),
    ("Zhong2024_STOTEN_Exp1", "63种土（省级尺度范围）", "RS", "21 d", "MeHg", "0.93–2.57", "μg/kg", "未报道", "未报道", "正文 p.4；Fig. 1a", "原文“on a provincial scale”"),
    ("Zhong2024_STOTEN_Exp1", "63种土（全国平均）", "CK", "21 d", "Km", "0.21", "%/d", "未报道", "未报道", "正文 p.4", ""),
    ("Zhong2024_STOTEN_Exp1", "63种土（全国平均）", "RS", "21 d", "Km", "0.38", "%/d", "未报道", "未报道", "正文 p.4", ""),
    ("Zhong2024_STOTEN_Exp1", "63种土（全国平均）", "CK", "21 d", "Kd", "0.64", "/d", "未报道", "未报道", "正文 p.4", ""),
    ("Zhong2024_STOTEN_Exp1", "63种土（全国平均）", "RS", "21 d", "Kd", "0.99", "/d", "未报道", "未报道", "正文 p.4", ""),
    ("Zhong2024_STOTEN_Exp1", "63种土（全国中位数）", "CK", "21 d", "MeHg", "(0.55)", "μg/kg", "未报道", "未报道", "Fig. 1a 插图（p.4），图中估读", "箱线图中位线"),
    ("Zhong2024_STOTEN_Exp1", "63种土（全国中位数）", "RS", "21 d", "MeHg", "(1.3)", "μg/kg", "未报道", "未报道", "Fig. 1a 插图（p.4），图中估读", "箱线图中位线"),
    ("Zhong2024_STOTEN_Exp1", "63种土（全国中位数）", "CK", "21 d", "Km", "(0.15)", "×10−2 /d", "未报道", "未报道", "Fig. 1b 插图（p.4），图中估读", "箱线图中位线"),
    ("Zhong2024_STOTEN_Exp1", "63种土（全国中位数）", "RS", "21 d", "Km", "(0.30)", "×10−2 /d", "未报道", "未报道", "Fig. 1b 插图（p.4），图中估读", "箱线图中位线"),
    ("Zhong2024_STOTEN_Exp1", "63种土（全国中位数）", "CK", "21 d", "Kd", "(0.5)", "/d", "未报道", "未报道", "Fig. 1c 插图（p.4），图中估读", "箱线图中位线"),
    ("Zhong2024_STOTEN_Exp1", "63种土（全国中位数）", "RS", "21 d", "Kd", "(0.9)", "/d", "未报道", "未报道", "Fig. 1c 插图（p.4），图中估读", "箱线图中位线"),
]
_F4 = {  # μg/kg，均为图中估读（mean）
    "CZ":  ["(1.4)", "(3.9)", "(1.1)", "(4.4)"],
    "HK":  ["(0.75)", "(1.8)", "(0.55)", "(4.0)"],
    "HY":  ["(0.8)", "(2.95)", "(1.25)", "(2.7)"],
    "HZ":  ["(1.0)", "(1.75)", "(0.75)", "(2.25)"],
    "MDJ": ["(0.65)", "(1.4)", "(0.55)", "(2.9)"],
    "NC":  ["(1.0)", "(2.25)", "(1.2)", "(2.45)"],
    "TR":  ["(1.3)", "(6.5)", "(1.7)", "(1.25)"],
    "YA":  ["(0.65)", "(2.35)", "(1.3)", "(3.55)"],
}
for soil, vals in _F4.items():
    for trt, v in zip(["CK", "RS", "RS-SRB", "RS-Meth"], vals):
        T2.append(("Zhong2024_STOTEN_Exp3", soil, trt, "21 d", "MeHg", v, "μg/kg", "SD（未估读）", "3",
                   "Fig. 4a（p.5），图中估读", "图注：mean ± SD"))

EXCLUDED = []
