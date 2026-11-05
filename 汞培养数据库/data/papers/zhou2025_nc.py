"""Zhou et al. 2025, Nature Communications（DOI 10.1038/s41467-025-60458-1）。页码为 PDF 页码。SI 已提供（未逐项摘录）。"""
from .common import NOTRACER
PAPER = {"文件名": "NC_微生物缓解农田及水稻中神经毒性甲基汞积累的潜力.pdf", "第一作者": "Xin-Quan Zhou", "年份": "2025",
         "期刊": "Nature Communications", "DOI": "10.1038/s41467-025-60458-1",
         "文献核心问题": "农田土壤中哪些微生物类群和生化途径参与 CH3Hg+ 降解。",
         "文献主要结论": "13CH3Hg+ DNA-SIP 结合宏基因组鉴定出 Pseudarthrobacter、Methylophilaceae（MM2）和 Dechloromonas 是最主要的潜在降解类群；纯培养证实 Dechloromonas denitrificans 和 Methylovorus menthalis 能降解 CH3Hg+。"}
T1 = [{**NOTRACER,
    "实验编号": "Zhou2025_NC_Exp1", "实验名称": "Microcosm incubation（13CH3Hg+-DNA-SIP）", "实验类型": "A",
    "实验目的": "以 13CH3Hg+ 为代谢示踪剂，鉴定稻田土和旱地土中参与 CH3Hg+ 降解的微生物类群。",
    "采样地点": "贵州万山（27.52°N，109.21°E，高汞）；湖北咸宁（29.90°N，114.23°E，低汞）；2018年9–11月采样",
    "土壤数量": "2个稻田土（High-P、Low-P）+ 2个旱地土（High-U、Low-U，不符合标准，只作为对比）",
    "污染背景": "矿区污染（万山）+ 一般农田（咸宁）；人为加 CH3Hg+", "采样深度": "0 ~ 15 cm",
    "土样状态": "鲜土；冰盒运输，4 °C 保存至培养；保存时长未报道",
    "pH": "需查 SI（Supplementary Table 1，SI 已提供，未逐项摘录）", "有机质": "需查 SI", "总汞": "需查 SI", "MeHg": "本底 CH3Hg+ 为 0.45–3.48 μg kg−1（Supplementary Table 1）",
    "硫酸盐": "需查 SI", "铁": "需查 SI",
    "处理组": "High-P、High-U、Low-P、Low-U（各分 12CH3Hg+ 和 13CH3Hg+ 两组）；γ 辐照灭菌对照 High-SP、High-SU、Low-SP、Low-SU；共12个处理",
    "外加汞形态": "CH3Hg+（12C 和 13C 标记，13CH3Hg+ 由 13CH4I 与 HgO 自制，溶于甲醇）", "外加汞剂量": "50 μg kg−1",
    "相对本底倍数": "约 14–111 倍本底 CH3Hg+（50 / 3.48 至 50 / 0.45，按原文数值计算）", "加汞后平衡": "未报道",
    "其他添加物": "无（CH3Hg+ 溶于甲醇，甲醇的加入量未报道）", "抑制剂": "无", "灭菌对照": "有：γ 射线辐照（剂量未在正文给出）",
    "土量g": "10（干重）", "水量mL": "未报道（只说明定期称重补加 ddH2O 以保持含水量恒定）", "土水比": "未报道",
    "容器": "50 mL 血清瓶", "密封方式": "未报道", "气氛": "未报道", "预培养": "未报道", "温度": "25 °C", "避光": "是", "振荡": "未报道",
    "重复数": "3", "取样方式": "不确定（未说明是否破坏性取样）", "总培养时长d": "28", "取样时间点": "0, 3, 7, 14, 28 d",
    "各时间点指标": "0/3/7/14/28 d：CH3Hg+；7/14/28 d：DNA-SIP（CsCl 梯度、16S rRNA 定量和 PacBio 长读长测序）；宏基因组",
    "MeHg方法": "约 0.50 g 干土加 1.5 mL CuSO4（2 mol L−1）和 7.5 mL 25% HNO3 消解，用 CH2Cl2 萃取，水浴去除 CH2Cl2，Brooks Rand 自动 MeHg 分析系统测定",
    "质控": "未报道（原文只引用文献称标准物质回收率一般为 75%–115%）；第0 d 实测 CH3Hg+ 约 45 μg kg−1，与理论值不完全一致",
    "Q_测t0": "是", "Q_灭菌对照": "是", "Q_严格厌氧": "未报道", "Q_透氧容器": "未报道",
    "原文摘录": ("【土量/汞剂量】“10 g soil (dry weight) was spiked with CH3Hg+ solutions (both 12CH3Hg+ and 13CH3Hg+ were used in parallel for microbial comparison) to give a fixed concentration of 50 μg kg–1.”（p.8）\n"
              "【水量】“During the incubation, water content was kept constant by checking the weight of the bottles regularly and adding ddH2O”（p.8）\n"
              "【培养时长】“All treatments in this study were conducted in triplicate and incubated for 28 days at 25 °C in the dark.”（p.8）\n"
              "【取样时间点】“CH3Hg+ concentration was measured at days 0, 3, 7, 14, and 28 in both the 13CH3Hg+ and 12CH3Hg+ treatments.”（p.8）\n【Km/Kd 公式】无（只报道降解效率和降解速率 μg kg−1 d−1）。"),
    "需查SI字段": "土壤性质（Supplementary Table 1，SI 已提供）",
    "备注": "不确定：原文没有说明培养时土壤是否淹水或处于厌氧状态，本实验可能不完全符合纳入标准中的“淹水或厌氧”，请复核。旱地土处理不符合标准，未列入表2。纯培养降解实验已排除。",
}]
T2 = [("Zhou2025_NC_Exp1", "High-P（万山稻田）", "CH3Hg+ 50 μg/kg", "28 d", "MeHg", "5.16", "μg kg−1", "未报道", "3", "正文 p.2；Fig. 1C", "原文为“mean concentrations”；降解效率 86%"),
      ("Zhou2025_NC_Exp1", "Low-P（咸宁稻田）", "CH3Hg+ 50 μg/kg", "28 d", "MeHg", "28.05", "μg kg−1", "未报道", "3", "正文 p.2；Fig. 1D", "原文为“mean concentrations”；降解效率 40%"),
      ("Zhou2025_NC_Exp1", "全部处理", "CH3Hg+ 50 μg/kg", "0 d", "MeHg", "45", "μg kg−1", "未报道", "未报道", "Methods p.8", "原文“around 45 μg kg−1”")]
EXCLUDED = [("Zhou2025_NC", "旱地土（High-U、Low-U）处理", "非稻田土壤"),
            ("Zhou2025_NC", "Dechloromonas denitrificans、Methylovorus menthalis 纯培养降解实验", "纯培养")]
