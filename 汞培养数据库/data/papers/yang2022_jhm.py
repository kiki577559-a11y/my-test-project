"""Yang et al. 2022, Journal of Hazardous Materials 423: 126895。页码为 PDF 页码。"""
from .common import NOTRACER
PAPER = {"文件名": "JHM_微塑料对不同类型稻田土壤汞甲基化的影响.pdf", "第一作者": "X. Yang（全名需查原文）", "年份": "2022",
         "期刊": "Journal of Hazardous Materials", "DOI": "10.1016/j.jhazmat.2021.126895",
         "文献核心问题": "PVC 微塑料对不同类型稻田土壤（红壤、碱性土）汞甲基化的影响及机制。",
         "文献主要结论": "PVC 微塑料降低了红壤和碱性土中的有效态 MeHg（DGT 测定）；可能的机制包括：改变 DOM 组成及其对 Hg2+ 的结合能力，改变硫酸盐、溶解态 Fe 等土壤性质，以及影响微生物群落和甲基化功能基因。"}
T1 = [{**NOTRACER,
    "实验编号": "Yang2022_JHM_Exp1", "实验名称": "Microcosmic experiment（2.1 Experimental set up and design）", "实验类型": "A",
    "实验目的": "考察不同剂量 PVC 微塑料对两种稻田土中加汞后有效态 Hg2+ 和 MeHg 的影响。",
    "采样地点": "红壤：湖南永州；碱性土：内蒙古赤峰；原文称采自 agricultural fields（是否为稻田：不确定，标题和讨论中称 paddy soils）",
    "土壤数量": "2", "污染背景": "人为加汞", "采样深度": "0–10 cm", "土样状态": "风干、混匀、过 ≤ 2 mm 筛，温室（约22 °C）保存",
    "pH": "需查 SI（Table S1）", "有机质": "需查 SI", "总汞": "需查 SI", "MeHg": "需查 SI", "硫酸盐": "需查 SI", "铁": "需查 SI",
    "处理组": "每种土4个处理：PVC 微塑料 0%（RS/AS 对照）、2%、7%、10%（按干土质量）；共8个处理", "外加汞形态": "未报道",
    "外加汞剂量": "目标汞含量 800 ng g−1 d.w.（预培养后加入）", "相对本底倍数": "需查 SI", "加汞后平衡": "无（加汞后即放入 DGT 开始计时）",
    "其他添加物": "PVC 微塑料（0.1–10 µm）；丙酮酸钠 1 mM（激活甲基化微生物）", "抑制剂": "无", "灭菌对照": "无",
    "土量g": "50（土或土-微塑料混合物）", "水量mL": "100（去离子水）", "土水比": "1:2", "容器": "玻璃罐（高 6.2 cm，直径 6.9 cm）",
    "密封方式": "气密螺旋盖，锡箔包裹", "气氛": "预培养后的操作均在厌氧操作箱中进行；用刃天青指示剂确认缺氧",
    "预培养": "有：室温避光预培养 4 d", "温度": "25 °C（室温）", "避光": "是", "振荡": "未报道（加汞前搅拌几秒）", "重复数": "3",
    "取样方式": "破坏性：每个时间点牺牲3个罐", "总培养时长d": "21（加汞后；另有预培养 4 d）", "取样时间点": "加汞后 < 1 d 至 21 d（具体时间点：未在正文列出，见 Fig.）",
    "各时间点指标": "各时间点：ORP、pH、DGT 有效态 Hg2+ 和 MeHg；上覆水溶解态 Fe、硫酸盐、DOC、EEM-PARAFAC；16S rRNA、甲基化功能基因 qPCR（时间点未明确）",
    "MeHg方法": "DGT 法（细节见 SI）", "质控": "需查 SI",
    "Q_测t0": "不确定（< 1 d）", "Q_灭菌对照": "否", "Q_严格厌氧": "是（厌氧操作箱，刃天青确认）", "Q_透氧容器": "否",
    "原文摘录": ("【土量/水量】“For each experimental replicate, 50 g soil or soil-microplastics mixture was added to glass jars of 6.2 cm height and 6.9 cm diameter, with 100 ml deionized water (18.2 MΩ cm Milli-Q water).”（p.2）\n"
              "【汞剂量】“Target Hg content was 800 ng g−1 d.w.”（p.2）\n"
              "【培养时长/取样】“Replicate jars (n = 3) were sacrificed for sampling at designated contact times <1 and up to 21 days after Hg addition.”（p.2）\n"
              "【Km/Kd 公式】无。"),
    "需查SI字段": "土壤性质（Table S1）、微塑料性质（Table S2）、DGT 方法",
    "备注": "汞的化学形态未在正文说明。本文测的是 DGT 有效态，没有测土壤总 MeHg，表2无数值（正文只给出相对变化百分比）。",
}]
T2 = []
EXCLUDED = []
