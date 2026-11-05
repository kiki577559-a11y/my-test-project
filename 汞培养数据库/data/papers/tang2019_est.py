"""Tang et al. 2019, Environ. Sci. Technol.（Just Accepted 版，DOI 10.1021/acs.est.8b07145）。页码为 PDF 页码；SI 已提供。"""
from .common import NOTRACER
PAPER = {"文件名": "EST−秸秆改良对水稻甲基汞积累的影响.pdf", "第一作者": "Wenli Tang", "年份": "2019",
         "期刊": "Environmental Science & Technology", "DOI": "10.1021/acs.est.8b07145",
         "文献核心问题": "秸秆还田是否以及如何增加稻田土壤 MeHg 生成和稻米 MeHg 积累。",
         "文献主要结论": "64个野外土壤中加秸秆使净 MeHg 生成提高11%–1043%；盆栽中秸秆还田使稻米 MeHg 升高；批量培养显示秸秆通过促进 SRB 等微生物甲基化、改变汞形态提高 MeHg 生成。"}
_s = dict(NOTRACER, 外加汞形态="无（未外加汞）", 外加汞剂量="无", 相对本底倍数="无", 加汞后平衡="无", 灭菌对照="无",
          MeHg方法="约 0.3 g 湿土加 2 mL 25% KOH-CH3OH，60 °C 消解 4 h，用 Brooks Rand Model III 测定（EPA 1630）（SI p.2）",
          质控="三平行、方法/试剂空白、基质加标（回收率 86%–105%）和标准物质（回收率见 Table S5）；操作过程中 MeHg 损失 < 5%（SI p.2）",
          Q_灭菌对照="否")
T1 = [
 {**_s, "实验编号": "Tang2019_EST_Exp1", "实验名称": "Field survey（64个野外土壤 21 d 批量培养）", "实验类型": "A",
  "实验目的": "量化全国64个稻田土加秸秆后的净 MeHg 生成。", "采样地点": "中国12个省份64个样点（Fig. S1）",
  "土壤数量": "64", "污染背景": "一般农田（THg 大多为 24–446 µg/kg）；52号样点为矿区污染（74 mg/kg）", "采样深度": "2–15 cm（2017年水稻收获后）",
  "土样状态": "鲜湿土，冰盒运回后用于培养；过筛情况未报道", "总汞": "大多为 24–446 µg/kg；52号样点 74 mg/kg（Table S3）",
  "pH": "需查 SI（Table S3，SI 已提供，未逐项摘录）", "有机质": "需查 SI", "MeHg": "需查 SI", "硫酸盐": "需查 SI", "铁": "需查 SI",
  "处理组": "CK（不加秸秆）；RS（1% 稻草，即 10 g/kg 土）", "其他添加物": "稻草 1%（w/w），培养开始时加入（秸秆 THg 30.9 ± 0.2、MeHg 2.7 ± 0.1 µg/kg）", "抑制剂": "无",
  "土量g": "未报道（正文写 details in SI，SI 中未找到具体用量）", "水量mL": "未报道", "土水比": "未报道", "容器": "批量反应器（batch reactor），类型未报道",
  "温度": "28 °C", "重复数": "未报道", "取样方式": "未报道", "总培养时长d": "21", "取样时间点": "21 d", "各时间点指标": "21 d：MeHg",
  "Q_测t0": "否", "Q_严格厌氧": "未报道", "Q_透氧容器": "未报道",
  "原文摘录": ("【土量/水量】未报道（“details in SI”）。\n【汞剂量】未外加汞。\n"
            "【培养时长/取样】“All soils were subjected to 21 days of batch incubation at 28°C. Two treatments, CK (soil without rice straw) and RS (soil + 1% rice straw amendment, i.e., 10 g/kg soil), were established, with soil MeHg levels determined on day 21”（p.8）\n【Km/Kd 公式】无。"),
  "需查SI字段": "土壤性质（Table S3）", "备注": "各土壤 MeHg 只在 Fig. S1 中；正文提到“2–4.4 µg/kg in 20 sites”（加秸秆土壤），已记入表2。"},
 {**_s, "实验编号": "Tang2019_EST_Exp2", "实验名称": "Incubation experiments（XUN 土批量培养）", "实验类型": "A",
  "实验目的": "在 XUN 汞污染土中考察秸秆、乳酸和钼酸盐对微生物 MeHg 生成和汞形态的影响。", "采样地点": "陕西旬阳（XUN）汞矿区稻田；坐标未报道",
  "土壤数量": "1", "污染背景": "矿区污染", "采样深度": "0–20 cm", "土样状态": "风干、研磨、过 2 mm 筛",
  "总汞": "44.0 ± 3.3 mg/kg", "MeHg": "6.0 ± 0.1 µg/kg", "pH": "需查 SI（Table S1）", "有机质": "需查 SI", "硫酸盐": "需查 SI", "铁": "需查 SI",
  "处理组": "CK；RS（1% 稻草）；RS-SRB（1% 稻草 + 20 mM Na2MoO4）；L（10 mM 乳酸钠）；RS+L（1% 稻草 + 10 mM 乳酸钠）",
  "其他添加物": "稻草 1%；乳酸钠 10 mM（培养开始时）", "抑制剂": "Na2MoO4 20 mM",
  "土量g": "10", "水量mL": "30（去离子水）", "土水比": "1:3", "容器": "离心管（材质和体积未报道）", "密封方式": "未报道（原文只写“sealed”）",
  "气氛": "密封厌氧培养（Eh 见 Fig. S2）；第40 d 后每天开盖 1 h（亚缺氧，Eh −41~46 mV）；样品分装在充 N2 的手套袋中进行（pot 部分）",
  "预培养": "未报道", "温度": "28 °C（环境箱）", "避光": "是", "振荡": "未报道", "重复数": "3", "取样方式": "破坏性：每个时间点取3管（每个处理共18管）",
  "总培养时长d": "45（厌氧 40 d + 再氧化 5 d）", "取样时间点": "4 h，5, 10, 15, 30, 45 d",
  "各时间点指标": "各时间点：土壤 MeHg；上覆水 MeHg、Eh、pH、溶解态 Fe、DOC、SO4；d5/10/30：XANES 汞形态；d5/10/15/30：SRB（MPN）；d15：hgcA 拷贝数",
  "Q_测t0": "是（4 h）", "Q_严格厌氧": "否（在环境箱中培养，40 d 后每天开盖）", "Q_透氧容器": "未报道",
  "原文摘录": ("【土量/水量】“Specifically, 10 grams of amended or unamended soil were re-suspended in 30 mL DI (for CK and RS treatments) and Na2MoO4 (for RS-SRB, 20 mM final concentration) or lactate (for L and RS+L treatments, 10 mM final concentration) was added.”（p.10）\n"
            "【培养时长】“All tubes were sealed and incubated in the dark under anoxic conditions (Eh values shown in Fig. S2) in an environmental chamber (28°C). After 40 days, all tubes were uncapped for 1 h every day to evaluate MeHg dynamics under sub-anoxic conditions (Eh = -41–46 mV).”（p.10）\n"
            "【取样时间点】“After 4 h and 5, 10, 15, 30, and 45 days, three tubes in each treatment (total of 18 tubes/treatment) were centrifuged”（p.10）\n【汞剂量】未外加汞。\n【Km/Kd 公式】无。"),
  "需查SI字段": "土壤性质（Table S1）", "备注": "MeHg 时间动态只以图呈现，正文未给出数值，表2只记录本底值。"},
]
T2 = [("Tang2019_EST_Exp1", "20个样点（加秸秆土）", "RS", "21 d", "MeHg", "2–4.4", "µg/kg", "未报道", "未报道", "正文 p.18；Fig. S1", "原文“e.g., 2–4.4 µg/kg in 20 sites”"),
      ("Tang2019_EST_Exp2", "XUN", "原土", "培养前", "THg", "44.0", "mg/kg", "± 3.3（SD/SE 未说明）", "未报道", "正文 p.7", ""),
      ("Tang2019_EST_Exp2", "XUN", "原土", "培养前", "MeHg", "6.0", "µg/kg", "± 0.1（SD/SE 未说明）", "未报道", "正文 p.7", "")]
EXCLUDED = [("Tang2019_EST", "盆栽实验（XUN 土种稻 129 d）", "盆栽，有植物"), ("Tang2019_EST", "幼苗吸收和砂培实验", "植物实验")]
