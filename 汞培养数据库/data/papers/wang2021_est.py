"""Wang et al. 2021, Environ. Sci. Technol.（DOI 10.1021/acs.est.0c07321）。页码为 PDF 页码。"""
from .common import NOTRACER
PAPER = {"文件名": "EST_系统氧化还原变化下稻田土壤汞的活化、甲基化与去甲基化.pdf", "第一作者": "Jianxu Wang", "年份": "2021",
         "期刊": "Environmental Science & Technology", "DOI": "10.1021/acs.est.0c07321",
         "文献核心问题": "在 Eh 从 −300 mV 逐步升到 +300 mV 的过程中，污染稻田土壤中汞的活化、甲基化和去甲基化如何变化。",
         "文献主要结论": "Eh 从 −300 升到 +200 mV 时 MeHg 下降，主要是甲基化减弱所致（+200 mV 时溶解态 THg 和 Desulfitobacterium 相对丰度分别比 −300 mV 时下降50%和96%）；去甲基化菌（Clostridium）也下降93%以上，去甲基化的作用可能较小。"}
T1 = [{**NOTRACER,
    "实验编号": "Wang2021_EST_Exp1", "实验名称": "Redox Experiments Using Advanced Biogeochemical Microcosm Technique", "实验类型": "A",
    "实验目的": "用自动控制 Eh 的生物地球化学微宇宙系统，研究系统性 Eh 变化下汞的活化、甲基化和去甲基化。",
    "采样地点": "中国西南某污染稻田（原文坐标写作 25°63′37.20″N，105°20′37.40″E；“63′”不是有效的分值，不确定）", "土壤数量": "1",
    "污染背景": "污染稻田（污染来源未说明）", "采样深度": "0−20 cm", "土样状态": "风干、混匀、过 4 mm 尼龙筛；采土约 200 kg；保存条件未报道",
    "pH": "8.6 ± 0.08", "有机质": "1.21%（organic matter）", "总汞": "8.9 ± 2.0 mg kg−1", "MeHg": "未报道", "硫酸盐": "未报道", "铁": "全铁 54.8 ± 0.92 g kg−1",
    "处理组": "单一处理，按 Eh 窗口顺序取样：−300、−200、−100、0、+100、+200、+300 mV", "外加汞形态": "无（原位污染土）", "外加汞剂量": "无", "相对本底倍数": "无", "加汞后平衡": "无",
    "其他添加物": "每个微宇宙加小麦秸秆粉约 15 g、葡萄糖 10 g（碳源），培养开始时加入", "抑制剂": "无", "灭菌对照": "无",
    "土量g": "未报道（只给出土水质量比 1:8）", "水量mL": "未报道", "土水比": "1:8（质量比）", "容器": "生物地球化学微宇宙（MC）系统，材质和体积见引用文献（未报道）",
    "密封方式": "未报道", "气氛": "初期微生物还原达到最低 Eh（−333 mV，65 h）；之后每 48 h 用合成空气（N2/O2 79.5/20.5）或 O2 吹扫，使 Eh 升高约 100 mV；取样后在 95% N2/5% H2 厌氧工作站中处理",
    "预培养": "未报道", "温度": "未报道", "避光": "未报道", "振荡": "未报道（原文称 soil slurry，搅拌情况见引用文献）", "重复数": "3（3个独立微宇宙）",
    "取样方式": "从同一微宇宙中分次取样（每次用注射器抽取约 80 mL 土悬液）", "总培养时长d": "不确定（约 65 h + 6 × 48 h，约 15 d，原文未直接给出）",
    "取样时间点": "按 Eh 窗口取样（C1–C7）：−300（约 65 h 达到）、−200、−100、0、+100、+200、+300 mV，每个窗口平衡约 48 h 后取样",
    "各时间点指标": "每个 Eh 窗口：溶解态和胶体态 THg、MeHg、Fe、DOC、SO4 2−、Cl−；沉积相 MeHg、Fe 形态（XANES）、16S rRNA；−300、0、+300 mV：胶体 STEM-EDS",
    "MeHg方法": "液体样品蒸馏浓缩；土样用 CuSO4-甲醇提取，再用二氯甲烷萃取、水反萃取，乙基化后 CVAFS（Brooks Rand）测定，USEPA 1630",
    "质控": "DMA-80 检出限 0.01 ng；MeHg 质控：未报道",
    "Q_测t0": "否（第一个取样点为 −300 mV）", "Q_灭菌对照": "否", "Q_严格厌氧": "否（还原阶段只靠微生物耗氧，之后通入空气或 O2）", "Q_透氧容器": "未报道",
    "原文摘录": ("【土量/水量】“Each MC was filled with air-dried soil and water at a mass ratio of 1:8.”（p.3）\n"
              "【汞剂量】未外加汞；“Total concentrations of Hg and Fe in the soil were 8.9 ± 2.0 mg kg−1 and 54.8 ± 0.92 g kg−1, respectively.”（p.3）\n"
              "【培养时长/取样时间点】“The lowest Eh value (−333 mV) was achieved after 65 h through microbial reduction effects. … Except at −300 mV, six predefinite Eh windows (−200, −100, 0, +100, +200, and +300 mV) were set and subsequently sampled after 48 h of equilibrium.”（p.3）\n"
              "【Km/Kd 公式】无（用 MeHg/THg 表示甲基化潜力）。"),
    "需查SI字段": "土壤性质测定方法（S1.1）",
    "备注": "MeHg/THg 比值（原文称 methylation potential/efficiency）以 ×10−6 表示，没有说明是溶解相还是固相（不确定）。溶解态和胶体态 MeHg（Figure 6A）是水相浓度，不属于表2规定的土壤 MeHg 指标，未估读。",
}]
T2 = [("Wang2021_EST_Exp1", "西南污染稻田土", "Eh −300 至 −100 mV", "Eh −300、−200、−100 mV 窗口", "%MeHg", "105–123", "×10−6（MeHg/THg 比值）", "未报道", "3", "正文 p.6；Figure 6B", "原文称 methylation potential；相态不确定"),
      ("Wang2021_EST_Exp1", "西南污染稻田土", "Eh 0 至 +300 mV", "Eh 0、+100、+200、+300 mV 窗口", "%MeHg", "18–52", "×10−6（MeHg/THg 比值）", "未报道", "3", "正文 p.6；Figure 6B", "同上"),
      ("Wang2021_EST_Exp1", "西南污染稻田土", "原土", "培养前", "THg", "8.9", "mg kg−1", "± 2.0（SD/SE 未说明）", "未报道", "正文 p.3", "")]
EXCLUDED = []
