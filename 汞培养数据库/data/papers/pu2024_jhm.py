"""Pu et al. 2024, Journal of Hazardous Materials 480: 136481。页码为 PDF 页码。"""
PAPER = {"文件名": "JHM_稻田土壤关键活性汞甲基化微生物及其对甲基汞产生的协同作用.pdf", "第一作者": "Qiang Pu", "年份": "2024",
         "期刊": "Journal of Hazardous Materials", "DOI": "10.1016/j.jhazmat.2024.136481",
         "文献核心问题": "稻田土壤中哪些是活性汞甲基化微生物，它们之间是否存在协同作用。",
         "文献主要结论": "DNA-SIP 结合汞同位素标记鉴定出 Geobacter 和 Anaerolinea 是稻田关键活性汞甲基化菌；二者共同添加时 Me198Hg 生成量是单独添加 Geobacter 的2.8倍、单独添加 Anaerolinea 的5.2倍。"}
_site = dict(采样地点="贵州省万山汞矿区：AM（废弃汞矿区）、AS（土法炼汞区）；贵阳市对照区 BG；坐标见 SI Text S1（需查 SI）",
             污染背景="矿区污染（AM、AS）+ 对照（BG）", 采样深度="10–20 cm（根区），2021年插秧后 60 d",
             土样状态="鲜土（分为两份：一份用于 SIP 微宇宙，另一份测理化、hgcA 和汞）；保存条件：需查 SI",
             pH="需查 SI", 有机质="需查 SI", 硫酸盐="需查 SI", 铁="需查 SI",
             MeHg方法="同位素 MeHg：GC-ICP-MS（Agilent 7700×），乙基化-吹扫捕集；本底 MeHg 提取方法：需查 SI",
             质控="需查 SI", Q_灭菌对照="否", Q_透氧容器="未报道")
T1 = [
 {**_site, "实验编号": "Pu2024_JHM_Exp1", "实验名称": "Experiment 1（SIP microcosm experiment）", "实验类型": "A+B",
  "实验目的": "用 202Hg 同位素标记结合 13C-乙酸 DNA-SIP，鉴定活性汞甲基化微生物。",
  "土壤数量": "9（3个区域 × 3块稻田）",
  "总汞": "BG 0.28 ± 0.03，AS 25.96 ± 2.09，AM 672.05 ± 30.26 μg/g（p.5）", "MeHg": "BG 0.79 ± 0.07，AS 2.68 ± 0.45，AM 4.61 ± 0.78 ng/g（p.5）",
  "处理组": "202Hg-13C[acetate]（202Hg + 10 mM 13C-乙酸）；202Hg-12C[acetate]（202Hg + 10 mM 12C-乙酸）；对照组的设置：不确定（结果中提到“higher in the acetate treatments than in the control”，但方法部分未描述对照）",
  "外加汞形态": "202Hg(NO3)2（富集同位素）", "外加汞剂量": "202Hg 为土壤本底 THg 的 10%", "相对本底倍数": "0.1 倍",
  "加汞后平衡": "未报道", "其他添加物": "13C 或 12C 标记乙酸 10 mM（甲基供体）", "抑制剂": "无", "灭菌对照": "无（非生物作用的排除方法见 SI Text S2）",
  "土量g": "未报道（30 mL 泥浆，含水率调到 75%）", "水量mL": "未报道", "土水比": "不确定（只报道含水率 75%）",
  "容器": "未报道", "密封方式": "未报道", "气氛": "通 N2 营造缺氧环境", "预培养": "未报道", "温度": "25 °C", "避光": "是",
  "振荡": "未报道", "重复数": "3", "取样方式": "未报道", "总培养时长d": "3", "取样时间点": "3 d（培养结束）",
  "各时间点指标": "3 d：Me202Hg（km-202Hg2+）、DNA（CsCl 密度梯度分层、hgcA 定量和测序）",
  "示踪剂种类": "202Hg(NO3)2", "示踪剂剂量": "本底 THg 的 10%", "示踪剂预平衡": "未报道", "示踪培养时长": "3 d",
  "是否测t0": "未报道", "Km公式": "需查 SI（正文提到 km-202Hg2+，未给出公式）", "Kd公式": "无", "同位素测定": "GC-ICP-MS（Agilent 7700×），乙基化-吹扫捕集",
  "Q_测t0": "未报道", "Q_示踪剂超本底": "否（10%）", "Q_示踪超24h": "是（3 d）", "Q_严格厌氧": "否（只说明通 N2，未提手套箱）",
  "原文摘录": ("【土量/水量】“30 mL of paddy slurry (prepared by adjusting the moisture content of paddy soils to 75 %, ref Liu et al. [20]) was purged with nitrogen to create an anoxic environment.”（p.3）\n"
            "【汞剂量】“The 202Hg treatment was added with enriched 202Hg(NO3)2 stable isotope (with a spiked concentration of 202Hg at 10 % of the background THg in soil”（p.3）\n"
            "【培养时长】“All the treatments were performed in triplicate and incubated in the dark at 25 ◦C for 3 days.”（p.3）\n"
            "【取样时间点】培养结束（3 d）。\n【Km/Kd 公式】正文未给出。"),
  "需查SI字段": "样点信息（Text S1）、非生物对照（Text S2）、km 公式及数值", "备注": "km 和 Me202Hg 结果只以图引用，正文没有给出数值。"},
 {**_site, "实验编号": "Pu2024_JHM_Exp3", "实验名称": "Experiment 3（anaerobic microbial incubation experiment）", "实验类型": "A",
  "实验目的": "验证 Geobacter 与 Anaerolinea 共同添加对稻田泥浆 MeHg 生成的协同作用。",
  "土壤数量": "1（BG 对照区土）", "总汞": "BG 0.28 ± 0.03 μg/g（p.5）", "MeHg": "BG 0.79 ± 0.07 ng/g（p.5）",
  "处理组": "Control；Geobacter-added；Anaerolinea-added；Geobacter + Anaerolinea（接种 G. sulfurreducens PCA、Anaerolinea sp. P10，各 10^6 CFU/g）",
  "外加汞形态": "198Hg(NO3)2（富集同位素）", "外加汞剂量": "与 SIP 实验相同（本底 THg 的 10%）", "相对本底倍数": "0.1 倍",
  "加汞后平衡": "未报道", "其他添加物": "纯培养菌液 10^6 CFU/g", "抑制剂": "无", "灭菌对照": "无",
  "土量g": "未报道（每瓶 30 mL 泥浆）", "水量mL": "未报道", "土水比": "未报道",
  "容器": "血清瓶（serum bottles），材质和体积未报道", "密封方式": "未报道（原文只写“sealed”）",
  "气氛": "在无氧手套箱中操作和培养", "预培养": "未报道", "温度": "25 °C", "避光": "是（铝箔包裹）", "振荡": "加示踪剂后轻摇混匀",
  "重复数": "未报道", "取样方式": "未报道", "总培养时长d": "2（48 h）", "取样时间点": "48 h",
  "各时间点指标": "48 h：Me198Hg",
  "示踪剂种类": "198Hg(NO3)2", "示踪剂剂量": "与 SIP 实验相同（本底 THg 的 10%）", "示踪剂预平衡": "未报道", "示踪培养时长": "48 h",
  "是否测t0": "未报道", "Km公式": "无（只报道 Me198Hg 浓度）", "Kd公式": "无", "同位素测定": "GC-ICP-MS，乙基化-吹扫捕集",
  "Q_测t0": "未报道", "Q_示踪剂超本底": "否", "Q_示踪超24h": "是（48 h）", "Q_严格厌氧": "是",
  "原文摘录": ("【土量/水量】“Each homogenized slurry (30 mL) was placed in a serum bottle with four treatments”（p.3）\n"
            "【汞剂量】“All the bottles were spiked with 198Hg(NO3)2 tracer, at a dosage matching that used in the SIP experiment.”（p.3）\n"
            "【培养时长】“Incubation lasted 48 h at 25 ◦C in the glovebox.”（p.3）\n【取样时间点】48 h。\n【Km/Kd 公式】无。"),
  "需查SI字段": "菌株培养方法（Text S3）", "备注": "表2中的 Me198Hg 是示踪剂生成的 MeHg，不是总 MeHg。"},
 ]
T2 = [("Pu2024_JHM_Exp1", s, "野外原样", "培养前", "THg", v, "μg/g", "SD " + sd, "3", "正文 p.5；Fig. 1a", "") for s, v, sd in
      (("BG", "0.28", "0.03"), ("AS", "25.96", "2.09"), ("AM", "672.05", "30.26"))]
T2 += [("Pu2024_JHM_Exp1", s, "野外原样", "培养前", "MeHg", v, "ng/g", "SD " + sd, "3", "正文 p.5", "") for s, v, sd in
       (("BG", "0.79", "0.07"), ("AS", "2.68", "0.45"), ("AM", "4.61", "0.78"))]
T2 += [("Pu2024_JHM_Exp3", "BG", "Control", "48 h", "MeHg", "(0.3)", "ng/g", "未估读", "未报道", "Fig. 4（p.7），图中估读", "Me198Hg（示踪剂来源）；图中单位为 pg/g，约 300 pg/g"),
       ("Pu2024_JHM_Exp3", "BG", "Geobacter", "48 h", "MeHg", "2.77", "ng/g", "未报道", "未报道", "正文 p.7；Fig. 4", "Me198Hg（示踪剂来源）"),
       ("Pu2024_JHM_Exp3", "BG", "Anaerolinea", "48 h", "MeHg", "1.50", "ng/g", "未报道", "未报道", "正文 p.7；Fig. 4", "Me198Hg（示踪剂来源）"),
       ("Pu2024_JHM_Exp3", "BG", "Geobacter + Anaerolinea", "48 h", "MeHg", "7.80", "ng/g", "未报道", "未报道", "正文 p.7；Fig. 4", "Me198Hg（示踪剂来源）")]
EXCLUDED = [("Pu2024_JHM", "Experiment 2（野外样品宏转录组）", "不是培养实验"),
            ("Pu2024_JHM", "G. sulfurreducens PCA、Anaerolinea sp. P10 的纯培养（SI Text S3）", "纯培养")]
