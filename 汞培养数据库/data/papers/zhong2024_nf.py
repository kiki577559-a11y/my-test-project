"""Zhong et al. 2024, Nature Food 5: 301–311。页码为 PDF 页码。正文未给出逐土数值（结果为相关关系和变化百分比），表2未记录数值。"""
PAPER = {"文件名": "NF_土壤地杆菌科是水稻神经毒性甲基汞生物积累的关键预测因子.pdf", "第一作者": "Huan Zhong", "年份": "2024",
         "期刊": "Nature Food", "DOI": "10.1038/s43016-024-00954-7",
         "文献核心问题": "农田土壤中哪类汞甲基化微生物是水稻 MeHg 积累的关键预测因子。",
         "文献主要结论": "对全国67个农田生态系统的研究和稻田生物地球化学模型表明，Geobacteraceae 是稻田 MeHg 生物积累的关键预测因子；水稻 MeHg 对 Geobacteraceae 相对丰度变化的敏感度是对汞输入变化的1.3–1.7倍。"}
_s = dict(采样地点="中国12个省份67个稻田，水稻收获后采样（2017年11月）；坐标见 Supplementary Table 1（需查 SI）",
          污染背景="一般农田（全国调查）", 采样深度="1–13 cm",
          土样状态="鲜土，每个样点5个土柱混合，冰盒运回实验室；过筛及保存条件：未报道",
          pH="需查 SI（Supplementary Table 1/6）", 有机质="需查 SI", 总汞="需查 SI", MeHg="需查 SI", 硫酸盐="需查 SI", 铁="需查 SI",
          MeHg方法="约 0.5 g 土加 2 mL 25%（w/w）KOH-CH3OH，70 °C 提取 4 h；在 pH 4.1–4.5 柠檬酸缓冲液中用 NaBEt4 乙基化，CVAFS（Brooks Rand model III）测定，EPA 1630；THg：DMA-80（EPA 7473）",
          质控="标准物质 GBW07423（GSS-9，THg 32 ± 3 μg/kg）、GBW07405（GSS-5，THg 290 ± 30 μg/kg）、ERM-CC580（MeHg 75 ± 4 μg/kg）；汞回收率 91.5%–109.8%；加标 MeHg 回收率 81.4%–114.6%，人为生成 MeHg 低于本底的10%（14个土，用 202Hg 示踪评估）；检出限 THg 0.1 μg/kg、MeHg 0.05 μg/kg",
          Q_灭菌对照="否")
_iso = dict(示踪剂种类="无", 示踪剂剂量="无", 示踪剂预平衡="无", 示踪培养时长="无", 是否测t0="无", Km公式="无", Kd公式="无", 同位素测定="无",
            Q_测t0="不适用（无同位素）", Q_示踪剂超本底="不适用（无同位素）", Q_示踪超24h="不适用（无同位素）")
_KM = ("【Km/Kd 公式】“km = [Me202Hg+]tf / ([202Hg2+]t0 · t) (1)；kd = (ln[Me199Hg+]t0 − ln[Me199Hg+]tf) / t (2)”；"
       "“Where [MeHg+] and [Hg+] represent the concentration of MeHg and IHg; t0 and tf refer to the start time and the end time and t is the incubation duration (day).”（p.8；公式按文字层整理，分式结构未逐一按页面图核对）")
T1 = [
 {**_s, "实验编号": "Zhong2024_NF_Exp1", "实验名称": "km and kd 测定（Methods）", "实验类型": "B",
  "实验目的": "测定67个稻田土壤的汞甲基化速率常数 km 和去甲基化速率常数 kd。", "土壤数量": "67",
  "处理组": "单一处理（无添加）", "外加汞形态": "仅示踪剂：202HgCl2、CH3199HgBr", "外加汞剂量": "为本底 THg 或 MeHg 的 10%–80%",
  "相对本底倍数": "0.1–0.8 倍", "加汞后平衡": "未报道", "其他添加物": "无", "抑制剂": "无", "灭菌对照": "无",
  "土量g": "2", "水量mL": "2（厌氧水：去离子水通 N2 1 h）", "土水比": "1:1（2 g : 2 mL）", "容器": "玻璃瓶（glass bottle），体积未报道",
  "密封方式": "未报道（原文只写“sealed”）", "气氛": "在厌氧工作站内培养", "预培养": "有：28 °C 避光预培养 7 d（厌氧工作站内），之后离心去除上覆水再加示踪剂",
  "温度": "28 °C", "避光": "是", "振荡": "未报道", "重复数": "未报道", "取样方式": "未报道（24 h 后取 0.7 g 土消解）",
  "示踪剂种类": "202HgCl2；CH3199HgBr", "示踪剂剂量": "为本底 THg 或 MeHg 的 10%–80%", "示踪剂预平衡": "未报道", "示踪培养时长": "24 h",
  "是否测t0": "不确定（公式用 t0，未说明是否实测）", "Km公式": "km = [Me202Hg+]tf / ([202Hg2+]t0 · t)", "Kd公式": "kd = (ln[Me199Hg+]t0 − ln[Me199Hg+]tf) / t",
  "同位素测定": "GC-ICP-MS（NexION300，PerkinElmer）；Me201Hg 作内标，KOH-甲醇消解",
  "总培养时长d": "8（预培养 7 d + 示踪 24 h）", "取样时间点": "加示踪剂后 24 h", "各时间点指标": "24 h：Me202Hg、Me199Hg（km、kd）",
  "Q_测t0": "不确定", "Q_示踪剂超本底": "否（10%–80%）", "Q_示踪超24h": "否", "Q_严格厌氧": "是（厌氧工作站）", "Q_透氧容器": "否（玻璃瓶）",
  "原文摘录": ("【土量/水量】“Specifically, 2 g of soil was resuspended in 2 ml of anaerobic water (obtained via bubbling nitrogen gas in deionized water for 1 h) in a glass bottle.”（p.8）\n"
            "【培养时长】“The bottles were sealed and incubated at 28 °C in the dark for seven days within the anaerobic workstation.”（p.8）\n"
            "【汞剂量】“The soils were then added with 202HgCl2 and CH3 199HgBr at 10–80% of the ambient THg or MeHg concentrations in soils, mixed thoroughly and further incubated for 24 h.”（p.8）\n" + _KM),
  "需查SI字段": "各土壤的 km、kd 数值及土壤性质（Supplementary Table 1）", "备注": "正文没有列出 km、kd 的具体数值，表2未记录。"},
 {**_s, **_iso, "实验编号": "Zhong2024_NF_Exp2", "实验名称": "Metabolism inhibition assays – Assay I", "实验类型": "A",
  "实验目的": "用钼酸盐/BES 抑制剂评估 SRB、产甲烷菌和 FeRB 对 MeHg 生成的贡献。", "土壤数量": "17（FeRB 优势9个、SRB 优势4个、产甲烷菌优势4个）",
  "处理组": "Control；20 mM Na2MoO4；30 mM BES；20 mM Na2MoO4 + 30 mM BES", "外加汞形态": "无（未外加汞）", "外加汞剂量": "无", "相对本底倍数": "无", "加汞后平衡": "无",
  "其他添加物": "无", "抑制剂": "Na2MoO4 20 mM；BES 30 mM", "灭菌对照": "无",
  "土量g": "5（湿重）", "水量mL": "30", "土水比": "1:6（湿土）", "容器": "50 mL 聚丙烯离心管（Corning）", "密封方式": "未报道（原文只写“sealed”）",
  "气氛": "在厌氧工作站（AW300SG）内培养", "预培养": "未报道", "温度": "28 °C", "避光": "是", "振荡": "未报道", "重复数": "3",
  "取样方式": "破坏性：7 d 后整管离心", "总培养时长d": "7", "取样时间点": "7 d",
  "各时间点指标": "7 d：土壤 MeHg、HCl 提取态 Fe(II)；上覆水 SO4 2−",
  "Q_严格厌氧": "是", "Q_透氧容器": "是（聚丙烯离心管）",
  "原文摘录": ("【土量/水量】“Specifically, 5 g of soil (wet weight, the same below) was resuspended in 30 ml of deionized water in a 50 ml polypropylene centrifuge tube (Corning), with Na2MoO4 and/or BES added or not.”（p.8）\n"
            "【培养时长】“The tubes were then sealed and incubated at 28 °C in the dark under anoxic conditions in the anaerobic workstation (AW300SG, Electrotek)… After 7 days, all tubes were centrifuged (2,950 × g, 20 min)”（p.8）\n"
            "【汞剂量】未外加汞。\n【Km/Kd 公式】无。"),
  "需查SI字段": "各土壤信息（Supplementary Tables 1、6）", "备注": "MeHg 结果只以图（Fig. 2、Extended Data）中的变化和相关关系呈现，表2未记录。"},
 {**_s, **_iso, "实验编号": "Zhong2024_NF_Exp3", "实验名称": "Metabolism inhibition assays – Assay II（Se amendment）", "实验类型": "A",
  "实验目的": "用加 Se 抑制 Geobacteraceae 活性，观察 Fe(II) 和 MeHg 的变化。", "土壤数量": "10（Geobacteraceae 低丰度4个、高丰度6个）",
  "处理组": "Control；Se（Na2SeO3 0.4 mg/kg）；所有处理均加 10 mM 乙酸", "外加汞形态": "Hg(NO3)2", "外加汞剂量": "第7 d 加到 100 μg/kg，再培养 24 h",
  "相对本底倍数": "需查 SI（本底 THg 见 Supplementary Table 6）", "加汞后平衡": "无（加汞后培养 24 h 即取样）",
  "其他添加物": "乙酸 10 mM（培养开始时）；Na2SeO3 0.4 mg/kg（培养开始时）", "抑制剂": "无（以 Se 作为 FeRB 活性的调控手段）", "灭菌对照": "无",
  "土量g": "5", "水量mL": "15", "土水比": "1:3", "容器": "50 mL 离心管（材质未报道）", "密封方式": "未报道",
  "气氛": "未报道（在人工气候箱中培养；离心分离在厌氧条件下进行）", "预培养": "加汞前已培养 7 d", "温度": "25 °C", "避光": "是",
  "振荡": "未报道", "重复数": "3", "取样方式": "破坏性：第8 d 整管离心", "总培养时长d": "8（7 d + 加汞后 24 h）", "取样时间点": "8 d（加汞后 24 h）",
  "各时间点指标": "8 d：土壤 MeHg、HCl 提取态 Fe(II)；上覆水硫酸盐",
  "Q_严格厌氧": "否（在人工气候箱中培养）", "Q_透氧容器": "未报道",
  "原文摘录": ("【土量/水量】“Specifically, 5 g of soil was resuspended in 15 ml of deionized water in a 50-ml tube.”（p.8）\n"
            "【汞剂量/培养时长】“After being thoroughly mixed, the soils were incubated in an artificial chamber (25 °C, dark). On the seventh day of incubation, IHg, in the form of Hg(NO3)2, was spiked to 100 μg kg−1, and the Hg-spiked soils were subjected to further incubation for 24 h.”（p.8）\n"
            "【取样时间点】加汞后 24 h（同上）。\n【Km/Kd 公式】无。"),
  "需查SI字段": "各土壤信息（Supplementary Table 6）", "备注": "MeHg 和 Fe(II) 结果只以变化量的图（Fig. 2a）呈现，表2未记录。"},
]
T2 = []
EXCLUDED = [("Zhong2024_NF", "全国67个土样的野外调查和 RPBM 模型模拟", "不是培养实验")]
