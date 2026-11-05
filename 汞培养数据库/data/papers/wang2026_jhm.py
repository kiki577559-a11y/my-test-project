"""Wang et al. 2026, Journal of Hazardous Materials 506: 141582。页码为 PDF 页码。"""
from .common import NOTRACER
PAPER = {"文件名": "JHM_有机物料诱导的还原条件促进稻田土壤汞甲基化：来自铁硫还原的证据.pdf", "第一作者": "J. Wang（全名需查原文）", "年份": "2026",
         "期刊": "Journal of Hazardous Materials", "DOI": "10.1016/j.jhazmat.2026.141582",
         "文献核心问题": "不同有机物料（秸秆、猪粪、牛粪、鸡粪）诱导的还原条件如何通过铁、硫还原影响稻田土壤汞甲基化。",
         "文献主要结论": "秸秆和猪粪使 Eh 迅速降到 −300 mV，加快 Fe/S 还原，MeHg 分别在第10 d（7.51 ± 1.16 ng/g）和第18 d（3.94 ± 0.32 ng/g）达峰；牛粪和鸡粪的 Eh 下降和 MeHg 峰值（1.75 ± 0.58、12.94 ± 0.88 ng/g）都推迟到第70 d；这种差异主要由 Eh 引起的 Fe/S 还原驱动。"}
T1 = [{**NOTRACER,
    "实验编号": "Wang2026_JHM_Exp1", "实验名称": "Incubation experiment（2.1 节，模拟稻田淹水培养）", "实验类型": "A",
    "实验目的": "比较4种有机物料对加汞稻田土 90 d 淹水培养中 Eh、Fe/S 还原和 MeHg 动态的影响。",
    "采样地点": "重庆，西南大学国家紫色土肥力与肥料效益监测站；坐标未报道", "土壤数量": "1", "污染背景": "人为加汞（加 HgCl2 后老化 6 个月以上）",
    "采样深度": "未报道", "土样状态": "风干、研磨、过 2 mm 筛；加汞后老化超过 6 个月",
    "pH": "需查 SI（Table S1）", "有机质": "需查 SI（SOM，重铬酸钾氧化法）", "总汞": "3.96 ± 0.22 μg/g（加汞老化后）", "MeHg": "需查 SI", "硫酸盐": "需查 SI", "铁": "需查 SI",
    "处理组": "CK；RS（秸秆）；PM（猪粪类商品有机肥）；CD（牛粪）；CM（鸡粪）；有机物料用量均为 1%（w/w）",
    "外加汞形态": "HgCl2", "外加汞剂量": "土壤终浓度 3.96 ± 0.22 μg/g（加入量本身未报道）", "相对本底倍数": "需查 SI", "加汞后平衡": "有：老化 6 个月以上",
    "其他添加物": "有机物料 1%（培养开始时混入）", "抑制剂": "无", "灭菌对照": "无",
    "土量g": "15", "水量mL": "40（去离子水）", "土水比": "3:8", "容器": "50 mL 厌氧瓶", "密封方式": "未报道（原文只写“sealed”）",
    "气氛": "高纯 N2 吹扫 10 min 后密封；取样在厌氧袋中进行", "预培养": "未报道", "温度": "25 °C", "避光": "是", "振荡": "每天摇匀",
    "重复数": "5", "取样方式": "破坏性", "总培养时长d": "90", "取样时间点": "0 d（4 h）、10、18、33、46、70、90 d",
    "各时间点指标": "各时间点：原位 pH、Eh；土壤 SOM、S0、MeHg、THg、hgcA qPCR；孔隙水 THg、MeHg、DOM、Fe2+/Fe3+、S2−/SO4 2−、Cl−",
    "MeHg方法": "EPA Method 1630（蒸馏、乙基化、GC 分离），Brooks Rand model III 测定",
    "质控": "方法空白低于检出限；标准物质回收率 80%–120%（Table S5）；平行实验、质量平衡和加标回收",
    "Q_测t0": "是（4 h）", "Q_灭菌对照": "否", "Q_严格厌氧": "否（N2 吹扫后密封，在培养箱中培养）", "Q_透氧容器": "未报道",
    "原文摘录": ("【汞剂量】“The soil was spiked with HgCl2 solution, thoroughly homogenized, and subsequently aged for over 6 months, forming a final soil Hg concentration of 3.96 ± 0.22 μg/g.”（p.2）\n"
              "【土量/水量】“For each treatment, five replicate 50 mL anaerobic bottles were prepared by aliquoting 15 g of Hg-spiked soil. … Subsequently, 40 mL of deionized water was added to each bottle, and the system was purged rapidly with high-purity N2 for 10 min”（p.2）\n"
              "【培养时长/取样】“Destructive sampling was performed at seven time points corresponding to key stages of rice growth under flooded conditions: day 0 (4 h), day 10, day 18, day 33, day 46, day 70, and day 90”（p.2）\n【Km/Kd 公式】无。"),
    "需查SI字段": "土壤和有机物料性质（Table S1、S2）、检出限和回收率（Table S5）",
    "备注": "每个处理有5个重复瓶，但有7个时间点且为破坏性取样，瓶数与时间点之间的关系不确定。",
}]
T2 = [("Wang2026_JHM_Exp1", "重庆紫色土（加汞）", "RS", "10 d", "MeHg", "7.51", "ng/g", "± 1.16（SD/SE 未说明）", "5", "正文 p.5（摘要 p.1）", "RS 的峰值"),
      ("Wang2026_JHM_Exp1", "重庆紫色土（加汞）", "PM", "18 d", "MeHg", "3.94", "ng/g", "± 0.32（SD/SE 未说明）", "5", "正文 p.5", "PM 的峰值"),
      ("Wang2026_JHM_Exp1", "重庆紫色土（加汞）", "CD", "70 d", "MeHg", "1.75", "ng/g", "± 0.58（SD/SE 未说明）", "5", "摘要 p.1", "CD 的峰值；与 CK 无显著差异"),
      ("Wang2026_JHM_Exp1", "重庆紫色土（加汞）", "CM", "70 d", "MeHg", "12.94", "ng/g", "± 0.88（SD/SE 未说明）", "5", "正文 p.5", "CM 的峰值"),
      ("Wang2026_JHM_Exp1", "重庆紫色土（加汞）", "全部处理", "培养前", "THg", "3.96", "μg/g", "± 0.22（SD/SE 未说明）", "未报道", "正文 p.2", "加汞老化后")]
EXCLUDED = []
