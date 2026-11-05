"""Zhang et al. 2024, Science of the Total Environment 930: 172832。页码为 PDF 页码。图4为小提琴图，只估读了散点范围。"""
PAPER = {"文件名": "STOTEN_增温抑制稻田土壤HgII甲基化但促进甲基汞去甲基化.pdf", "第一作者": "Qianshuo Zhang", "年份": "2024",
         "期刊": "Science of the Total Environment", "DOI": "10.1016/j.scitotenv.2024.172832",
         "文献核心问题": "温度升高如何影响稻田土壤 HgII 甲基化和 MeHg 去甲基化。",
         "文献主要结论": "6个样点的 Km-202HgII 都随温度升高（15→35 °C）显著下降，而 Kd-Me198Hg 显著上升；增温通过改变微生物群落（如 Geobacter、Anaerolineae 丰度降低）以及铁硫循环抑制净甲基化。"}
T1 = [{
    "实验编号": "Zhang2024_STOTEN_Exp1", "实验名称": "Incubation experiments（2.2 节，温度梯度）", "实验类型": "B",
    "实验目的": "在 15、25、35 °C 下用 202HgII/Me198Hg 示踪，测定全国6个稻田土的 Km、Kd。",
    "采样地点": "江西（JX）、浙江（ZJ）、湖南（HN）、贵州（GZ）、黑龙江（HLJ）、陕西（SX）；具体位置见 Table S1/Text S1（需查 SI）",
    "土壤数量": "6", "污染背景": "JX、HLJ、HN 为背景土；ZJ、GZ、SX 有不同程度汞污染",
    "采样深度": "1–10 cm（土-水界面以下），2022年8月插秧后 50–60 d",
    "土样状态": "鲜土；4个点混合；装入无顶空的 500 mL 无菌 PP 瓶，用 Parafilm 封口，4 °C 冰盒保存；保存时长未报道",
    "MeHg": "HN 0.29，HLJ 0.74，JX 0.77，ZJ 1.34，SX 2.53，GZ 2.91 ng/g（p.3）", "总汞": "需查 SI（Table S1）",
    "pH": "需查 SI", "有机质": "需查 SI", "硫酸盐": "需查 SI", "铁": "需查 SI",
    "处理组": "3个温度（15、25、35 °C）× 2个处理（未灭菌、γ 辐照灭菌对照）；6个样点 × 3个重复，共108个样品",
    "外加汞形态": "仅示踪剂：202Hg(NO3)2、Me198Hg(NO3)2", "外加汞剂量": "202HgII 约为本底 THg 的10%；Me198Hg 约为本底 MeHg 的100%（Table S2）",
    "相对本底倍数": "202HgII 约 0.1 倍；Me198Hg 约 1 倍", "加汞后平衡": "未报道", "其他添加物": "无", "抑制剂": "无",
    "灭菌对照": "有：γ 辐照（0.6 kGy h−1，48 h）",
    "土量g": "未报道（每瓶 40–60 mL 泥浆）", "水量mL": "未报道（含水率 50%–60%，用通 N2 的 Milli-Q 水调配）", "土水比": "不确定（只报道含水率 50%–60%）",
    "容器": "100 mL 气密硼硅玻璃血清瓶", "密封方式": "未报道", "气氛": "在充 N2 的手套箱中配制泥浆和取样；加示踪剂后封瓶，移到手套箱外培养",
    "预培养": "有：分别在 15、25、35 °C 避光预培养1周", "温度": "15、25、35 °C", "避光": "是（预培养）；示踪培养期间：未报道", "振荡": "未报道",
    "重复数": "3", "取样方式": "破坏性：24 h 后在手套箱中取3瓶",
    "示踪剂种类": "202Hg(NO3)2；Me198Hg(NO3)2", "示踪剂剂量": "202HgII 约为本底 THg 的10%；Me198Hg 约为本底 MeHg 的100%", "示踪剂预平衡": "未报道",
    "示踪培养时长": "24 h", "是否测t0": "是（原文：“evaluated initially (t0) and after 24 h (ti)”）",
    "Km公式": "Km = ([Me202Hg]ti − [Me202Hg]t0) / ([202HgII] × (ti − t0))", "Kd公式": "Kd = (ln([Me198Hg]t0) − ln([Me198Hg]ti)) / (ti − t0)",
    "同位素测定": "GC-ICP-MS（文中未写型号，同研究组其他文献为 Agilent 7700x）",
    "总培养时长d": "8（预培养 7 d + 示踪 24 h）", "取样时间点": "t0、24 h",
    "各时间点指标": "24 h：Me202Hg、Me198Hg（Km、Kd）、DOM、S2−、Fe2+、Fe3+、16S rRNA；宏基因组",
    "MeHg方法": "需查 SI", "质控": "硫化物检出限 0.13 μM；汞质控：需查 SI",
    "Q_测t0": "是", "Q_示踪剂超本底": "否", "Q_示踪超24h": "否", "Q_灭菌对照": "是",
    "Q_严格厌氧": "不确定（在手套箱中配制和取样，但在手套箱外的密封瓶中培养）", "Q_透氧容器": "否",
    "原文摘录": ("【土量/水量】“The resulting soil slurry (40–60 mL, 50 %–60 % moisture) was then transferred into 100 mL serum bottles (gas-tight borosilicate glass bottles) for incubation.”（p.2）\n"
              "【汞剂量】“The amounts of spiked 202HgII and Me198Hg tracers were ~10 % and ~100 % (Table S2), respectively, of the soil ambient total Hg (THg) and MeHg concentrations”（p.3）\n"
              "【培养时长】“To activate anaerobic microorganisms, the paddy soils were preincubated at 15 ◦C, 25 ◦C, and 35 ◦C in the dark for one week”（p.2）；“Three bottles were destructively sampled in the glovebox after 24 h of incubation”（p.3）\n"
              "【Km/Kd 公式】“Km = ([Me202Hg]ti − [Me202Hg]t0) / ([202HgII] × (ti − t0))；Kd = (ln([Me198Hg]t0) − ln([Me198Hg]ti)) / (ti − t0) (2)”；“which were evaluated initially (t0) and after 24 h (ti)”（p.3）"),
    "需查SI字段": "样点信息和 THg（Table S1、Text S1）、示踪剂剂量（Table S2）、各样点 Km/Kd（Fig. S6、S7）",
    "备注": "正文只用全部样点合并的小提琴图（Fig. 4）表示 Km、Kd，各样点数值在 SI 中；表2中只记录了按图中散点估读的范围。",
}]
T2 = [("Zhang2024_STOTEN_Exp1", "6个样点（散点范围）", "未灭菌", t, "Km", v, "day−1", "未报道", "6个样点", "Fig. 4a（p.6），图中估读", "小提琴图散点范围")
      for t, v in (("15 °C，24 h", "(0.000–0.019)"), ("25 °C，24 h", "(0.000–0.010)"), ("35 °C，24 h", "(0.000–0.004)"))]
T2 += [("Zhang2024_STOTEN_Exp1", "6个样点（散点范围）", "未灭菌", t, "Kd", v, "day−1", "未报道", "6个样点", "Fig. 4b（p.6），图中估读", "小提琴图散点范围")
       for t, v in (("15 °C，24 h", "(0.25–1.1)"), ("25 °C，24 h", "(0.6–1.4)"), ("35 °C，24 h", "(0.45–3.3)"))]
T2 += [("Zhang2024_STOTEN_Exp1", s, "野外原样", "培养前", "MeHg", v, "ng/g", "未报道", "未报道", "正文 p.3", "")
       for s, v in (("HN", "0.29"), ("HLJ", "0.74"), ("JX", "0.77"), ("ZJ", "1.34"), ("SX", "2.53"), ("GZ", "2.91"))]
EXCLUDED = []
