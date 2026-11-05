"""Zhou et al. 2020（EST 已接受稿件，Just Accepted）。页码为 PDF 页码。图1a数值为估读。"""
PAPER = {"文件名": "EST_稻田土壤中与甲基汞降解相关的微生物群落.pdf", "第一作者": "Xin-Quan Zhou", "年份": "2020",
         "期刊": "Environmental Science & Technology", "DOI": "10.1021/acs.est.0c00181",
         "文献核心问题": "稻田土壤中参与 MeHg 降解的微生物类群有哪些，水分条件和氮添加如何影响 MeHg 降解。",
         "文献主要结论": "3个稻田土在48 h 内 MeHg 降解30.5%–33.9%，灭菌土无明显变化，说明以微生物降解为主；淹水使湖南土 MeHg 降解加快（60 d 时 CTW 为72.71%，CT 为55.44%）；鉴定出了与 MeHg 降解相关的潜在微生物类群。"}
_s = dict(采样地点="湖南桃源、贵州万山、湖北恩施的稻田；其他样点信息见 Table S1（需查 SI）", 污染背景="不确定（正文未说明，Table S1）",
          采样深度="0~20 cm", 土样状态="鲜土；过 5.0 mm 筛；一份 −20 °C 保存（微生物分析），一份 4 °C 保存（培养）；保存时长未报道",
          pH="需查 SI（Table S1）", 有机质="需查 SI", 总汞="需查 SI", MeHg="需查 SI", 硫酸盐="需查 SI", 铁="需查 SI",
          外加汞形态="MeHg（化学形态未说明）", 加汞后平衡="未报道", 灭菌对照="有：γ 射线辐照（0.6 kGy hour−1，48 h）",
          MeHg方法="0.3~0.4 g 土用 CuSO4-甲醇/溶剂萃取法提取，NaBEt4 乙基化后用 Brooks Rand Model III 测定；THg：DMA-80",
          质控="ERM-CC580 标准物质（回收率未报道）；MeHg 加标回收率94.5%–101.9%（平均98.2%）；检出限 MeHg 2 pg L−1、THg 0.1 ng g−1；空白 < 2 pg L−1",
          示踪剂种类="无", 示踪剂剂量="无", 示踪剂预平衡="无", 示踪培养时长="无", 是否测t0="无", Km公式="无", Kd公式="无（只报道降解百分比）", 同位素测定="无",
          Q_示踪剂超本底="不适用（无同位素）", Q_示踪超24h="不适用（无同位素）", Q_灭菌对照="是")
T1 = [
 {**_s, "实验编号": "Zhou2020_EST_Exp1", "实验名称": "short-term (48 h) incubation experiment", "实验类型": "A",
  "实验目的": "比较3个稻田土在未灭菌和灭菌条件下 48 h 内的 MeHg 降解。", "土壤数量": "3",
  "处理组": "未灭菌土 + MeHg；γ 辐照灭菌土 + MeHg", "外加汞剂量": "MeHg：湖南 7.7、贵州 6.8、湖北 5.6 μg·kg−1", "相对本底倍数": "需查 SI",
  "其他添加物": "无", "抑制剂": "无", "土量g": "20", "水量mL": "未报道", "土水比": "未报道",
  "容器": "100 mL 血清瓶", "密封方式": "未报道", "气氛": "瓶内用纯 N2 吹扫 10 min", "温度": "25 °C", "避光": "是", "重复数": "5",
  "取样方式": "破坏性：48 h 后取样", "总培养时长d": "2（48 h）", "取样时间点": "0、48 h（0 h 是否实测：不确定）", "各时间点指标": "48 h：MeHg",
  "Q_测t0": "不确定", "Q_严格厌氧": "否（只用 N2 吹扫，未在手套箱中）", "Q_透氧容器": "未报道",
  "原文摘录": ("【土量/汞剂量】“Soil samples (20 g) from Hunan, Guizhou and Hubei were respectively spiked with MeHg at the concentrations of 7.7, 6.8 and 5.6 μg·kg-1.”（p.6）\n"
            "【容器/气氛/培养时长】“The spiked soil was then distributed to 100-mL serum bottles, which were flushed with pure nitrogen gas for 10 min to produce an anoxic condition. Five replicates of each treatment were incubated at 25 C in the dark for 48 h.”（p.6；原文 25 与 C 之间的符号无法识别）\n"
            "【水量】未报道。\n【Km/Kd 公式】无。"),
  "需查SI字段": "土壤性质（Table S1）、各土 MeHg 结果（Figure S1）", "备注": "表2未记录本实验数值（只有 Figure S1 和降解率 30.5%–33.9%）。"},
 {**_s, "实验编号": "Zhou2020_EST_Exp2", "实验名称": "longer term (120 d) degradation experiment", "实验类型": "A",
  "实验目的": "在湖南稻田土中考察水分、抑制剂、Cu 和氮添加对 MeHg 长期降解的影响，并识别相关微生物。", "土壤数量": "1（湖南桃源）",
  "处理组": "CN（不加 MeHg，70% WHC）；CT（70% WHC，非饱和）；CTW（淹水，水层5 cm）；Sterilization（γ 辐照）；MoO4（40 mM 钼酸钠）；BES（20 mM）；Cu（400 mg·kg−1）；NH4W（80 mM NH4Cl，淹水）；NO3W（200 mM NaNO3，淹水）；NH4（80 mM NH4Cl，非饱和）；NO3（200 mM NaNO3，非饱和）",
  "外加汞剂量": "MeHg 7.7 μg·kg−1（CN 除外）", "相对本底倍数": "需查 SI",
  "其他添加物": "Cu 400 mg·kg−1；NH4Cl 80 mM；NaNO3 200 mM", "抑制剂": "钼酸钠 40 mM；BES 20 mM",
  "土量g": "300", "水量mL": "未报道（淹水处理保持5 cm 水层；非饱和处理为70% 田间持水量）", "土水比": "未报道",
  "容器": "PVC 容器（10 × 10 × 13 cm）", "密封方式": "未报道", "气氛": "未报道", "温度": "25 °C", "避光": "是", "重复数": "5",
  "取样方式": "不确定（未明确，推测为从同一容器分次取样，原文未说明）", "总培养时长d": "120", "取样时间点": "0, 2, 4, 7, 14, 30, 60, 120 d",
  "各时间点指标": "各时间点：MeHg、土壤化学性质（pH、Eh、NH4+、NO3−）；0/60/120 d：16S rRNA 高通量测序",
  "Q_测t0": "是（0 d 取样）", "Q_严格厌氧": "否", "Q_透氧容器": "是（PVC 敞口/密封情况未报道）",
  "原文摘录": ("【土量/容器】“Each treatment consisted of five replicates, each with 300 g soil that was evenly filled in the PVC (Polyvinylchloride) container with the dimension of 10 × 10 × 13 cm (length × width × height).”（p.7）\n"
            "【水量】“The soil was flooded with deionized water to maintain a standing water 5 cm level above the soil surface.”（p.6–7）\n"
            "【汞剂量】“MeHg was added into ten treatments soil at the concentration of 7.7 μg·MeHg kg-1 soil, and CN treatment was not spiked with MeHg.”（p.7）\n"
            "【培养时长/取样】“all treatments were incubated in the dark for 120 days at 25 C … Soil samples were taken at 0, 2, 4, 7, 14, 30, 60, and 120 d”（p.7）\n【Km/Kd 公式】无。"),
  "需查SI字段": "土壤性质（Table S1）",
  "备注": "只有 CTW、NH4W、NO3W 三个处理是淹水的；CT、NH4、NO3 为非饱和（70% WHC）；Sterilization、MoO4、BES、Cu 的水分条件未说明（不确定）。表2只记录了图1a 中的 CN、CTW、CT、Sterilization，其余处理（图2）未估读。PVC 容器的透氧性按材质标为“是”。"},
 {**_s, "实验编号": "Zhou2020_EST_Exp3", "实验名称": "additional incubation experiments（宏转录组）", "实验类型": "A",
  "实验目的": "考察 MeHg 降解过程中土壤微生物群落基因表达的变化。", "土壤数量": "1（湖南）",
  "处理组": "加 MeHg（与短期实验相同；具体处理未详述，见 Text S1）", "外加汞剂量": "未报道（原文称与短期实验条件相同）", "相对本底倍数": "需查 SI",
  "其他添加物": "无", "抑制剂": "无", "灭菌对照": "未报道",
  "土量g": "20", "水量mL": "未报道", "容器": "100 mL 厌氧血清瓶", "气氛": "同短期实验（N2 吹扫）", "温度": "25 °C", "避光": "是", "重复数": "5",
  "取样方式": "从瓶中取 5 g 土（是否破坏性：不确定）", "总培养时长d": "2（48 h）", "取样时间点": "0 h（T0）、48 h（T48）", "各时间点指标": "T0/T48：总 RNA（宏转录组）",
  "Q_测t0": "是", "Q_灭菌对照": "未报道", "Q_严格厌氧": "否", "Q_透氧容器": "未报道",
  "原文摘录": ("【土量】“Briefly, the Hunan soil (20 g) was homogenized and distributed to 100 mL anoxic serum bottles, with five replicates for each treatment, and incubated under the same conditions as used in the short-term experiment.”（p.7）\n"
            "【取样时间点】“Soil samples (5 g) were collected at 0 h (T0) and 48 h (T48) for total RNA extraction and metatranscriptomic analyses”（p.7）\n【汞剂量】同短期实验（未单独给出）。\n【Km/Kd 公式】无。"),
  "需查SI字段": "实验细节（Text S1）", "备注": "本实验只用于宏转录组分析，表2没有数值。"},
]
_T = ["0 d", "2 d", "4 d", "7 d", "14 d", "30 d", "60 d", "120 d"]
_F = {"CN": ["(1.1)", "(1.4)", "(0.9)", "(0.8)", "(1.1)", "(1.2)", "(1.0)", "(0.9)"],
      "CTW（淹水）": ["(7.6)", "(5.3)", "(4.3)", "(3.8)", "(3.1)", "(3.1)", "(2.1)", "(1.5)"],
      "CT（非饱和）": ["(7.6)", "(5.6)", "(5.0)", "(5.5)", "(5.2)", "(4.3)", "(3.4)", "(1.9)"],
      "Sterilization": ["(7.7)", "(5.8)", "(5.6)", "(5.6)", "(6.6)", "(6.2)", "(7.0)", "(4.1)"]}
T2 = [("Zhou2020_EST_Exp2", "湖南桃源", trt, t, "MeHg", v, "μg·kg−1", "未估读（误差棒类型未报道）", "5", "Figure 1a（p.23），图中估读", "图横轴有断轴，估读精度较低")
      for trt, vals in _F.items() for t, v in zip(_T, vals)]
EXCLUDED = []
