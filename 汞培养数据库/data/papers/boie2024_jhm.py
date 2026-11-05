"""Boie et al. 2024, Journal of Hazardous Materials 472: 134446。页码为 PDF 页码。"""
from .common import NOTRACER
PAPER = {"文件名": "JHM_可控氧化还原变化下田间老化稻壳生物炭促进稻田土壤汞甲基化并改变微生物群落.pdf", "第一作者": "F. Boie（全名需查原文）", "年份": "2024",
         "期刊": "Journal of Hazardous Materials", "DOI": "10.1016/j.jhazmat.2024.134446",
         "文献核心问题": "在可控的动态氧化还原条件下，田间老化的稻壳生物炭如何影响汞污染稻田土壤的微生物群落和汞甲基化/去甲基化。",
         "文献主要结论": "加生物炭的土壤中汞甲基化超过去甲基化，固相 MeHg 在 EH < 0 mV 时最高（对照 7.4、生物炭 12.2 µg/kg）；微生物网络比单一物种对汞转化更重要。"}
T1 = [{**NOTRACER,
    "实验编号": "Boie2024_JHM_Exp1", "实验名称": "Biogeochemical microcosm experiment（2.2 节）", "实验类型": "A",
    "实验目的": "用自动控制 EH 的微宇宙，比较对照土和田间老化生物炭处理土在 EH 从还原到氧化变化时的 MeHg 和微生物群落。",
    "采样地点": "贵州万山汞矿区试验田（N 27°33’56，E 109°13’52），油菜-玉米-水稻轮作", "土壤数量": "2（对照土、生物炭处理土）",
    "污染背景": "矿区污染；田间施用稻壳生物炭 72 t ha−1（老化3个月）", "采样深度": "1 – 30 cm",
    "土样状态": "风干、过 4 mm 筛；保存条件未报道", "pH": "需查 SI（Tab. S1）", "有机质": "总碳：对照 25 g/kg，生物炭处理 50 g/kg",
    "总汞": "39.8 mg/kg（Tab. S1）", "MeHg": "对照 2.5 µg/kg，生物炭处理 4.3 µg/kg", "硫酸盐": "需查 SI", "铁": "需查 SI",
    "处理组": "对照土（未施生物炭）；生物炭处理土（田间老化）；无其他添加", "外加汞形态": "无（原位污染土）", "外加汞剂量": "无", "相对本底倍数": "无", "加汞后平衡": "无",
    "其他添加物": "无（原文：No additional substrate was added）", "抑制剂": "无", "灭菌对照": "无",
    "土量g": "210", "水量mL": "未报道（土与自来水比例 1:8，按此约 1680，未直接报道）", "土水比": "1:8", "容器": "MC 玻璃容器（体积未报道）",
    "密封方式": "气密密封，铝箔包裹", "气氛": "自动通入 N2（降低 EH）或合成空气/O2（升高 EH）", "预培养": "未报道", "温度": "未报道（自动记录，但未给出数值）",
    "避光": "是（铝箔包裹）", "振荡": "是：持续搅拌 500–600 rpm", "重复数": "3（Table 1 中 n = 3）",
    "取样方式": "从同一微宇宙中分次取样（每次 80 mL 土悬液）", "总培养时长d": "未报道",
    "取样时间点": "淹水后 1 h（初始）；最低 EH（对照 −10 mV，生物炭 −60 mV）；0、+100、+200、+300、+400、+500、+550 mV（生物炭另有 +600 mV），每个窗口 EH 稳定至少 24 h 后取样",
    "各时间点指标": "每个 EH 窗口：土壤溶液 THg、MeHg、DOC、TDN、NO3−、SO4 2−、Fe、Mn、S、SUVA；固相 PLFA、DNA 测序；固相 MeHg 只在初始和3个窗口（< 0 mV、200 mV、> 500 mV）测定",
    "MeHg方法": "固相 MeHg：CuSO4-甲醇提取，二氯甲烷相分离，CVAFS（Brooks Rand）测定；溶液 MeHg：EPA 1630",
    "质控": "标准物质 GBW(E)070009 和 CC580；三次测定 RSD < 15%；DMA-80 绝对检出限 0.05 ng；回收率未报道",
    "Q_测t0": "是（淹水后 1 h）", "Q_灭菌对照": "否", "Q_严格厌氧": "否（还原阶段通 N2，之后通空气或 O2）", "Q_透氧容器": "否",
    "原文摘录": ("【土量/水量】“MC glass vessels were filled with 210 g of soil and tap water in the ratio of 1:8.”（p.2）\n"
              "【汞剂量】未外加汞；“The content of total mercury in the paddy soil was 39.8 mg/kg (Tab. S1).”（p.2）\n"
              "【培养时长/取样时间点】“We conducted the first sampling one hour after flooding (initial), the next sampling at the lowest EH established in the system (for control at - 10 mV and for biochar-treated paddy soil at - 60 mV). Afterwards, we increased the EH stepwise to predefined windows … Samples were taken at each of these redox windows, when the EH was stable for at least 24 h.”（p.3）\n"
              "【Km/Kd 公式】无。"),
    "需查SI字段": "土壤与生物炭性质（Tab. S1）",
    "备注": "总培养天数未直接报道。Table 1 中 MeHgsed 为全部 EH 窗口的平均值（对照 5.69、生物炭 10.53 µg/kg，n = 4）。",
}]
T2 = [("Boie2024_JHM_Exp1", "对照土", "无生物炭", "EH < 0 mV 窗口", "MeHg", "7.4", "µg/kg", "未报道", "3", "正文 p.6；Fig. 4b", "固相 MeHg 最高值"),
      ("Boie2024_JHM_Exp1", "生物炭处理土", "田间老化生物炭", "EH < 0 mV 窗口", "MeHg", "12.2", "µg/kg", "未报道", "3", "正文 p.6；Fig. 4b", "固相 MeHg 最高值"),
      ("Boie2024_JHM_Exp1", "对照土", "无生物炭", "各 EH 窗口平均", "MeHg", "5.69", "µg/kg", "1.67（Table 1 第二列，SD/SE 未说明）", "4", "Table 1（p.6）", "MeHgsed"),
      ("Boie2024_JHM_Exp1", "生物炭处理土", "田间老化生物炭", "各 EH 窗口平均", "MeHg", "10.53", "µg/kg", "1.01（同上）", "4", "Table 1（p.6）", "MeHgsed"),
      ("Boie2024_JHM_Exp1", "对照土", "原土", "培养前", "MeHg", "2.5", "µg/kg", "未报道", "未报道", "正文 p.2", ""),
      ("Boie2024_JHM_Exp1", "生物炭处理土", "原土", "培养前", "MeHg", "4.3", "µg/kg", "未报道", "未报道", "正文 p.2", ""),
      ("Boie2024_JHM_Exp1", "对照土", "原土", "培养前", "THg", "39.8", "mg/kg", "未报道", "未报道", "正文 p.2", "")]
EXCLUDED = []
