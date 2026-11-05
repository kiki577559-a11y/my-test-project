"""Zhang et al. 2023, Environmental Pollution 323: 121335。页码为 PDF 页码。图1b数值为估读。"""
from .common import NOTRACER
PAPER = {"文件名": "EP_厌氧-好氧交替条件下外源汞在酸性稻田土壤中的滞留与转化：动力学与机理.pdf", "第一作者": "Yufan Zhang", "年份": "2023",
         "期刊": "Environmental Pollution", "DOI": "10.1016/j.envpol.2023.121335",
         "文献核心问题": "外源 Hg(II) 进入酸性稻田土壤后，在厌氧-好氧交替条件下的形态转化和甲基化动力学及机理。",
         "文献主要结论": "厌氧期水溶态、可交换态等活性汞形态迅速下降，腐殖酸结合态、有机-硫化物结合态增加；MeHg 在厌氧第20 d 达峰；厌氧期 Desulfovibrio、Desulfomicrobium 是主要甲基化菌，通氧后 Clostridium 类去甲基化菌增长。"}
T1 = [{**NOTRACER,
    "实验编号": "Zhang2023_EP_Exp1", "实验名称": "Soil incubation experiments（biogeochemical microcosm system）", "实验类型": "A",
    "实验目的": "模拟淹水-排水，追踪外加 HgCl2 的酸性稻田土在厌氧40 d、好氧20 d 过程中的汞形态和 MeHg 变化。",
    "采样地点": "江西省鹰潭市某未受汞污染稻田（原文坐标写作 28°13′45′′N，16°54′38′′E，经度疑有误，不确定）",
    "土壤数量": "1", "污染背景": "一般农田（非汞污染）+ 人为加汞", "采样深度": "0–20 cm",
    "土样状态": "风干、均质；理化分析用土过 0.15 mm 筛（培养用土的过筛粒径：未报道）；保存条件未报道",
    "pH": "4.52", "有机质": "需查 SI（Table S1，OM）", "总汞": "需查 SI（Table S1）", "MeHg": "需查 SI", "硫酸盐": "需查 SI", "铁": "需查 SI（DCB-Fe、Ox-Fe、全铁）",
    "处理组": "单一处理：加 HgCl2 后先厌氧 40 d，再好氧 20 d", "外加汞形态": "HgCl2", "外加汞剂量": "每瓶 6 g 土加 30 mL 4.93 mg L−1 HgCl2 溶液，终浓度 24.65 mg kg−1 Hg",
    "相对本底倍数": "需查 SI（本底 THg 在 Table S1）", "加汞后平衡": "未报道", "其他添加物": "无", "抑制剂": "无", "灭菌对照": "无",
    "土量g": "6（干土）", "水量mL": "30（HgCl2 溶液）", "土水比": "1:5", "容器": "50 mL 血清瓶",
    "密封方式": "厌氧期：丁基胶塞 + 铝盖；好氧期：换成 0.45 μm 透气膜", "气氛": "在无氧手套箱（H2/N2 2/98）中用 N2 吹扫后密封；培养在手套箱外的摇床上进行",
    "预培养": "未报道", "温度": "28 °C", "避光": "未报道", "振荡": "是：水平摇床 220 r min−1", "重复数": "3",
    "取样方式": "破坏性：每个时间点取3瓶，在无氧手套箱中处理", "总培养时长d": "60（厌氧 40 d + 好氧 20 d）",
    "取样时间点": "厌氧期 0, 2, 5, 10, 20, 40 d；好氧期 2, 7, 15, 20 d（即第 42, 47, 55, 60 d）",
    "各时间点指标": "各时间点：Eh、pH；滤液 NO3−、SO4 2−、NH4+、DOC、Fe(II)、水溶态 Hg（F0）、水溶态 MeHg（WMeHg）；湿土 TOC、HCl 提取态 Fe(II)/Fe(III)、改进 Tessier 法汞形态（F1–F7）、THg、总 MeHg（TMeHg）、有效态 MeHg（EMeHg）；微生物群落（时间点见原文）",
    "MeHg方法": "TMeHg：冻干土用 20% CuSO4–HNO3 和 CH2Cl2 依次提取，加热水反萃取；EMeHg：(NH4)2S2O3 提取；WMeHg：滤液蒸馏；均乙基化后用 CVAFS（MERX，Brooks Rand）测定，USEPA 1630",
    "质控": "GBW07453（GSS-24）测得 THg 70 ± 8 μg kg−1（认证值 75 ± 7）；ERM-CC580 测得 MeHg 83 ± 5.7 μg kg−1（认证值 75.5 ± 4）；形态提取汞回收率 91%–108%",
    "Q_测t0": "是（0 d）", "Q_灭菌对照": "否", "Q_严格厌氧": "否（在手套箱中密封，但在手套箱外培养）", "Q_透氧容器": "否（厌氧期）",
    "原文摘录": ("【土量/水量/汞剂量】“The system was established in 50 mL serum bottles containing 6 g dry soil and spiked with 30 mL 4.93 mg L−1 HgCl2 solution to obtain a final concentration of 24.65 mg kg−1 Hg”（p.2）\n"
              "【培养时长】“The sealed bottles were taken out from the O2-free glovebox and shaken on a horizontal shaker with a constant speed of 220 r min−1 at 28 ◦C for 40 d (anoxic period). Subsequently, the butyl rubber stoppers and aluminum covers of the bottles were replaced with a porous film (0.45 μm) to allow gas exchange with the air for 20 d with continuous shaking (oxic period).”（p.2）\n"
              "【取样时间点】“During the anoxic (0, 2, 5, 10, 20, and 40 d) and oxic (2, 7, 15, and 20 d) periods, three repeated destructive samples were collected from the incubated bottles in an O2-free glovebox.”（p.2）\n【Km/Kd 公式】无（另有形态转化动力学模型，速率常数见 Table 1）。"),
    "需查SI字段": "土壤理化性质和本底 THg（Table S1）、形态提取方法（Table S2、Text 2）",
    "备注": "原文给出的经度 16°54′38′′E 与江西鹰潭不符（不确定，可能为 116°）。文中动力学模型拟合的形态转化速率常数（Table 1）不属于规定的 Km/Kd，未记录。",
}]
_T = [("0 d", "(1.0)"), ("2 d", "(1.0)"), ("5 d", "(9)"), ("10 d", "(28)"), ("20 d", "46.85"), ("40 d", "(38)"),
      ("42 d（好氧2 d）", "(33)"), ("47 d（好氧7 d）", "(30)"), ("55 d（好氧15 d）", "(21.7)"), ("60 d（好氧20 d）", "(27)")]
T2 = [("Zhang2023_EP_Exp1", "鹰潭酸性稻田土", "HgCl2 24.65 mg/kg", t, "MeHg", v, "μg kg−1", "未报道", "3",
       "Fig. 1b（p.4）" + ("，图中估读" if v.startswith("(") else "；数值见正文 p.4"), "TMeHg（总 MeHg）") for t, v in _T]
T2.append(("Zhang2023_EP_Exp1", "鹰潭酸性稻田土", "HgCl2 24.65 mg/kg", "好氧期（42–60 d，范围）", "MeHg", "21.69–32.74", "μg kg−1", "未报道", "3", "正文 p.4",
           "原文为“TMeHg and EMeHg ranged from 21.69 to 32.74”，不确定该范围是指 TMeHg 还是两者"))
EXCLUDED = []
