"""He et al. 2023, Chemosphere 339: 139711。页码为 PDF 页码。"""
from .common import NOTRACER
PAPER = {"文件名": "Chemosphere_老化水稻秸秆降低稻田土壤汞和甲基汞的生物有效性.pdf", "第一作者": "Y. He（全名需查原文）", "年份": "2023",
         "期刊": "Chemosphere", "DOI": "10.1016/j.chemosphere.2023.139711",
         "文献核心问题": "老化（干湿交替、光化学、冻融）水稻秸秆还田对稻田土壤汞和 MeHg 生物有效性的影响。",
         "文献主要结论": "与新鲜秸秆（RS）相比，三种老化秸秆处理在20 d 培养中使有效态 Hg、MeHg（DGT 法测定）降低（DRS 2.2%–27.6%、LRS 13.5%–69.8%、FRS 23.5%–86.1%）。"}
T1 = [{**NOTRACER,
    "实验编号": "He2023_Chemosphere_Exp1", "实验名称": "Incubation experiments（2.4 节）", "实验类型": "A",
    "实验目的": "考察老化秸秆添加对稻田土壤有效态 Hg、MeHg（DGT-Hg、DGT-MeHg）及土壤性质、甲基化微生物动态的影响。",
    "采样地点": "贵州万山汞矿区五坑（WK）稻田；坐标未在正文给出", "土壤数量": "1", "污染背景": "矿区污染",
    "采样深度": "未报道", "土样状态": "需查 SI（Table S1）", "pH": "需查 SI（Table S1）", "有机质": "需查 SI", "总汞": "需查 SI", "MeHg": "需查 SI", "硫酸盐": "需查 SI", "铁": "需查 SI",
    "处理组": "RS（新鲜秸秆）；DRS（干湿交替老化）；LRS（光化学老化）；FRS（冻融老化）；各 0.1 g 秸秆；未设不加秸秆的对照",
    "外加汞形态": "无（原位污染土）", "外加汞剂量": "无", "相对本底倍数": "无", "加汞后平衡": "无",
    "其他添加物": "秸秆 0.1 g（1% w/w，过 100 μm 筛；秸秆 THg 2.14 ng/g、MeHg 0.81 ng/g）；丙酮酸钠 1 mM（培养开始时）", "抑制剂": "无", "灭菌对照": "无",
    "土量g": "10.0", "水量mL": "30（去离子水）", "土水比": "1:3", "容器": "50 mL 离心管（材质未报道）", "密封方式": "未报道（原文只写“sealed tubes”）",
    "气氛": "未报道（ORP、pH 在厌氧箱中测定）", "预培养": "未报道", "温度": "25 °C", "避光": "是", "振荡": "未报道", "重复数": "3",
    "取样方式": "破坏性：每个时间点取3管", "总培养时长d": "20", "取样时间点": "0 d（加秸秆后 4 h）、2、6、10、20 d",
    "各时间点指标": "各时间点：ORP、pH、DGT-Hg、DGT-MeHg；上覆水溶解态 Fe、Mn、硫酸盐、DOC；SOC；0 d（4 h）和 20 d：微生物群落、hgcA 拷贝数",
    "MeHg方法": "DGT 法测有效态 MeHg（细节见 Text S1，需查 SI）", "质控": "需查 SI",
    "Q_测t0": "是（加秸秆后 4 h）", "Q_灭菌对照": "否", "Q_严格厌氧": "未报道", "Q_透氧容器": "不确定（离心管材质未报道）",
    "原文摘录": ("【土量/水量】“Briefly, 10.0 g of WK soil and 0.1 g of straw (RS, DRS, LRS, and FRS) were put in 50 mL centrifuge tubes, then poured in 30 mL deionized water.”（p.3）\n"
              "【培养时长/取样】“All sealed tubes were incubated in the dark at 25 ◦C. Samples were taken on day 0 (i.e., 4 h after straw amendment), as well as on days 2, 6, 10, and 20.”（p.3）\n"
              "【汞剂量】未外加汞。\n【Km/Kd 公式】无。"),
    "需查SI字段": "土壤性质（Table S1）、DGT 方法（Text S1）、微生物方法（Text S2）",
    "备注": "本文测的是 DGT 有效态 Hg 和 MeHg，没有测土壤总 MeHg，因此表2没有数值。同文的石英砂水稻培养实验（种植物）已排除。第一作者全名在文字层中未提取到（页眉为“Y. He et al.”）。",
}]
T2 = []
EXCLUDED = [("He2023_Chemosphere", "Sand culture experiments（石英砂中种水稻幼苗）", "种植了植物，且不是土壤培养")]
