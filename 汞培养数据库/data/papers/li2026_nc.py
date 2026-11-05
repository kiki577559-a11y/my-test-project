"""NC 抗生素（氟喹诺酮）促进稻田土壤 MeHg 生成，Nature Communications（Article in Press，DOI 10.1038/s41467-026-79083-7）。页码为 PDF 页码；SI 已提供并摘录了同位素方法。"""
from .common import NOTRACER
PAPER = {"文件名": "NC-抗生素污染促进稻田土壤微生物合成甲基汞.pdf", "第一作者": "Hailong Li", "年份": "2026",
         "期刊": "Nature Communications", "DOI": "10.1038/s41467-026-79083-7",
         "文献核心问题": "氟喹诺酮类抗生素污染是否以及如何影响稻田土壤的微生物 MeHg 生成。",
         "文献主要结论": "在40个稻田土中，10 mg kg−1 氟喹诺酮培养21 d 后使 MeHg 提高2.9%–19.7%，主要是由于甲基化增强而非去甲基化受抑；抑制硫酸盐还原使氟喹诺酮诱导的甲基化降低31%–75%，携带 hgcA 的 SRB 是关键甲基化菌。"}
_s = dict(NOTRACER, 采样地点="中国9个水稻主产省份（2018–2019年）；各土壤信息见 Supplementary Table 2（SI 已提供，未逐项摘录）",
          污染背景="一般农田（全国调查）", 采样深度="0‒20 cm", 土样状态="鲜土，4 °C 保存；过筛及保存时长：未报道",
          pH="需查 SI（Supplementary Table 2）", 有机质="需查 SI", 总汞="需查 SI", MeHg="需查 SI", 硫酸盐="需查 SI", 铁="需查 SI",
          外加汞形态="无（未外加汞）", 外加汞剂量="无", 相对本底倍数="无", 加汞后平衡="无", 灭菌对照="无",
          土量g="2.0", 水量mL="2（除氧无菌水或氟喹诺酮溶液）", 土水比="1:1", 容器="50 mL 灭菌离心管（材质未报道）", 密封方式="未报道",
          气氛="在厌氧手套箱（95% N2、5% H2）中加样和混匀；培养位置：未报道", 预培养="未报道", 温度="25 °C", 避光="是", 振荡="未报道", 重复数="3",
          取样方式="破坏性：每个时间点随机取3管冻干",
          MeHg方法="约 0.2 g 土加 2 mL 25% KOH-甲醇，60 °C 振荡 4 h，EPA 1630，Brooks Rand model III 测定",
          质控="CuSO4/KBr 消解时 MeHg 基质加标回收率为 85%–117%（Supplementary Table 13）；其他：需查 SI",
          Q_测t0="否", Q_灭菌对照="否", Q_严格厌氧="不确定（在手套箱中配制，培养位置未说明）", Q_透氧容器="不确定（离心管材质未报道）")
_EXC0 = ("【土量/水量】“2.0 g of soil was weighed and placed in a 50 mL-sterilized centrifuge tube, and then 2 mL of oxygen-removed sterile water (for the control CK) or 2 mL of the corresponding FQ solutions … was separately added”（p.8）\n"
         "【汞剂量】未外加汞。\n")
T1 = [
 {**_s, "实验编号": "Li2026_NC_Exp1", "实验名称": "Batch assay I-Hg methylating microbes", "实验类型": "A",
  "实验目的": "在甲基化菌组成不同的3个土壤中，考察4种氟喹诺酮（两个剂量）对 MeHg 生成的影响。", "土壤数量": "3（MY：SRB 优势；DL：FeRB 优势；KL：产甲烷菌优势）",
  "处理组": "CK（除氧无菌水）；CIP、ENR、NOR、OFL 各 10 µg kg−1 和 10 mg kg−1", "其他添加物": "氟喹诺酮（CIP、ENR、NOR、OFL），培养开始时加入", "抑制剂": "无",
  "总培养时长d": "30", "取样时间点": "3, 7, 14, 30 d", "各时间点指标": "各时间点：土壤 MeHg；上清液 pH、土壤 THg、溶解态 THg（仅 Meishan 土）",
  "原文摘录": _EXC0 + "【培养时长/取样】“After thorough mixing, these tubes were incubated in the dark at 25 °C. On days 3, 7, 14, and 30, three tubes from each treatment were randomly selected and lyophilized for soil MeHg analyses.”（p.8）\n【Km/Kd 公式】本实验未测。",
  "需查SI字段": "土壤性质（Supplementary Tables 1、2）", "备注": "MeHg 结果只以图呈现，表2未记录。"},
 {**_s, "实验编号": "Li2026_NC_Exp2", "实验名称": "Batch assay II—National survey", "实验类型": "A",
  "实验目的": "在40个稻田土中检验4种氟喹诺酮（10 mg kg−1）对净 MeHg 生成的影响。", "土壤数量": "40",
  "处理组": "CK；CIP、ENR、NOR、OFL 各 10 mg kg−1", "其他添加物": "氟喹诺酮 10 mg kg−1", "抑制剂": "无",
  "总培养时长d": "21", "取样时间点": "21 d", "各时间点指标": "21 d：MeHg、氟喹诺酮残留、土壤 THg",
  "原文摘录": _EXC0 + "【培养时长】“The incubation was carried out as previously described. After 21 days of incubation, soils were lyophilized and stored at -20 °C for the analyses of MeHg”（p.9）\n【取样时间点】21 d。\n【Km/Kd 公式】本实验未测。",
  "需查SI字段": "土壤性质（Supplementary Table 2）", "备注": "结果以 MeHg 增幅（2.9%–19.7%）和图呈现，表2未记录。"},
 {**_s, "实验编号": "Li2026_NC_Exp3", "实验名称": "Batch assay III-metabolism assay（含同位素平行培养）", "实验类型": "A+B",
  "实验目的": "用钼酸盐抑制 SRB，并用同位素示踪测 Km、Kd，判断氟喹诺酮促进 MeHg 生成的机制。", "土壤数量": "4（Huanggang、Tianmen、Meishan、Ganzhou）",
  "处理组": "Mo-free 组：CK、CIP、ENR、NOR、OFL（10 mg kg−1）；+Mo 组：同上再加 20 mM Na2MoO4", "其他添加物": "氟喹诺酮 10 mg kg−1", "抑制剂": "Na2MoO4 20 mM（预实验比较了 5、10、20 mM）",
  "示踪剂种类": "202HgNO3（原文写法）；Me200HgCl", "示踪剂剂量": "约为本底 THg 和 MeHg 的 80%", "示踪剂预平衡": "未报道", "示踪培养时长": "24 h",
  "是否测t0": "未报道", "Km公式": "Km = CH3202Hg+ / (spiked T202Hg2+ × t) × 100%（单位标为 d−1，但公式含 ×100%，不确定）",
  "Kd公式": "spiked CH3200Hg+ / t = −Kd (CH3200Hg+)（原样抄录）", "同位素测定": "GC-ICP-MS（NexION300，PerkinElmer），CH3199Hg+ 作内标，EPA 1630",
  "Q_测t0": "未报道", "Q_示踪剂超本底": "否（约80%）", "Q_示踪超24h": "否",
  "总培养时长d": "22（21 d + 示踪 24 h）", "取样时间点": "21 d；同位素平行培养在第21 d 加示踪剂后 24 h",
  "各时间点指标": "21 d：MeHg、土壤 THg、可提取硫酸盐、hgcA 拷贝数、hgcA 群落、16S rRNA、氟喹诺酮残留、Fe 还原；平行培养 22 d：Me202Hg、Me200Hg（Km、Kd）",
  "原文摘录": _EXC0 + "【培养时长】“In the metabolism assay, four FQs were added as described in Batch assay I. … Another parallel incubation was conducted as described above to quantify the rate constants of Hg methylation and MeHg demethylation using a stable isotopic Hg-tracing technique (Supplementary Method 4).”（p.9）\n"
              "【示踪剂】“On the 21st day of incubation, all samples were transferred into an anaerobic glove box (N2/H2 = 95%/5%). The soil samples were spiked with 202HgNO3 and Me200HgCl solution to reach a concentration of about 80% of the background contents of THg and MeHg … incubated continuously at 25 oC for 24 h in the dark.”（SI p.7）\n"
              "【Km/Kd 公式】“Km = specific methylation rate constant (in d−1), and Km = CH3202Hg+/ (spiked T202Hg2+×t) ×100%; Kd = specific demethylation rate constant (in d−1), spiked CH3200Hg+/t =－Kd (CH3200Hg+); t = incubation time (in days)”（SI p.8）",
  "需查SI字段": "Km/Kd 结果数值", "备注": "Km、Kd 结果只以图呈现，表2未记录。"},
]
T2 = []
EXCLUDED = [("Li2026_NC", "Batch assay IV-SRB enrichment", "富集培养")]
