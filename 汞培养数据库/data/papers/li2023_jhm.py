"""Li et al. 2023, Journal of Hazardous Materials 448: 130983。页码为 PDF 页码。"""
from .common import NOTRACER
PAPER = {"文件名": "JHM_氮和硫添加减缓碳对稻田土壤微生物汞甲基化的促进作用.pdf", "第一作者": "Y. Li（全名需查原文）", "年份": "2023",
         "期刊": "Journal of Hazardous Materials", "DOI": "10.1016/j.jhazmat.2023.130983",
         "文献核心问题": "碳、氮、硫输入及其化学计量比变化如何影响两种典型稻田土（黄壤、黑土）的微生物 MeHg 生成。",
         "文献主要结论": "单独加碳使黄壤 MeHg 生成提高5.21–12.64倍；碳与硫或氮共同加入可减缓碳的促进作用（如 C+S 为2.58–6.46倍），氮添加的抑制可能与反硝化基因丰度有关；黑土中硫的缓冲作用在30 d 后消失。"}
T1 = [{**NOTRACER,
    "实验编号": "Li2023_JHM_Exp1", "实验名称": "microcosm experiments（2.1 Sample collection and microcosm setup）", "实验类型": "A",
    "实验目的": "考察 C、N、S 及其组合输入对加汞稻田土 50 d 淹水培养中 MeHg 生成的影响。",
    "采样地点": "黄壤：广东（23°16’N，113°36’E）；黑土：黑龙江（47°27´N，126°55´E）", "土壤数量": "2", "污染背景": "一般农田 + 人为加汞",
    "采样深度": "0–20 cm", "土样状态": "鲜土；冰盒运输，研磨、过 2 mm 筛，4 °C 保存；保存时长未报道",
    "pH": "需查 SI（Table S1）", "有机质": "需查 SI", "总汞": "需查 SI", "MeHg": "需查 SI", "硫酸盐": "需查 SI（Table S1；正文称黑土硫酸盐较低）", "铁": "需查 SI",
    "处理组": "Hg、Hg+C、Hg+N、Hg+S、Hg+CN、Hg+CS、Hg+CNS（Table S2）；C 为葡萄糖 500 mg C kg−1，N 为硝酸钠 250 mg N kg−1，S 为硫酸钠 45 mg S kg−1",
    "外加汞形态": "HgCl2", "外加汞剂量": "1 mg kg−1（以 Hg 计）", "相对本底倍数": "需查 SI", "加汞后平衡": "未报道（预培养1周后加汞，即开始 Hg methylation assays）",
    "其他添加物": "葡萄糖、硝酸钠、硫酸钠（按处理，以水溶液加入）", "抑制剂": "无", "灭菌对照": "无",
    "土量g": "100（烘干重当量）", "水量mL": "未报道（土:去离子水约 1:5，并保持 3 cm 水层）", "土水比": "约 1:5", "容器": "PVC 容器（直径 7.5 cm × 高 10 cm）",
    "密封方式": "未报道（原文只写“sealed”）", "气氛": "保持 3 cm 水层维持厌氧环境；未用手套箱", "预培养": "有：25 °C 避光预培养1周",
    "温度": "25 °C", "避光": "是（预培养）；培养期间：未报道", "振荡": "未报道", "重复数": "3",
    "取样方式": "不确定（每个时间点采集下层土，未说明是否为破坏性取样）", "总培养时长d": "50", "取样时间点": "0, 7, 14, 28, 50 d",
    "各时间点指标": "各时间点：MeHg；Eh、pH、全 C/N/S、NH4+、NO3−、硫酸盐、DOC（时间点未逐一说明）；50 d：细菌群落和汞甲基化微生物群落",
    "MeHg方法": "约 100 mg 冻干土（过 0.149 mm 筛）用 7.5 mL 25% HNO3 和 1.5 mL CuSO4（2 mol L−1）浸提，二氯甲烷萃取、水反萃取，CVAFS（Brooks Rand Model III）测定",
    "质控": "ERM-CC580 加标回收率 88.7%–110.0%；MeHg 检出限 0.002 ng L−1；分析空白低于检出限",
    "Q_测t0": "是（0 d）", "Q_灭菌对照": "否", "Q_严格厌氧": "否（靠水层维持厌氧）", "Q_透氧容器": "是（PVC 容器）",
    "原文摘录": ("【土量】“Experimental soil (equivalent to 100 g of oven-dried weight) was placed in a polyvinylchloride container (7.5 cm diameter × 10 cm height) and then pre-incubated at 25 ◦C in darkness for one week before Hg methylation assays.”（p.2）\n"
              "【汞剂量】“The levels of C (glucose), N (sodium nitrate), S (sodium sulfate) and Hg(II) (HgCl2) were 500 mg kg−1 (C/soil), 250 mg kg−1 (N/soil), 45 mg kg−1 (S/soil) and 1 mg kg−1 (Hg/soil …), respectively”（p.2）\n"
              "【水量】“The soil: deionized water ratio was about 1:5 in the incubation systems. … A layer of three centimeters level of water was kept above the soil surface to maintain the anaerobic environment”（p.2）\n"
              "【培养时长/取样】“Each sealed treatment was in triplicate and incubated at 25 ◦C for 50 d. The lower soil was collected at each sampling time point (0, 7, 14, 28, and 50 day)”（p.2）\n【Km/Kd 公式】无。"),
    "需查SI字段": "土壤性质（Table S1）、处理表（Table S2）",
    "备注": "取样时间点写的是 0、7、14、28、50 d，但结果中提到“at 30 day”（不确定）。正文只给出 MeHg 相对对照的倍数，没有绝对浓度，表2无数值。",
}]
T2 = []
EXCLUDED = []
