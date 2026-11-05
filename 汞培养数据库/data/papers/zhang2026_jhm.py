"""Zhang et al. 2026, Journal of Hazardous Materials 513: 142544。页码为 PDF 页码。图2数值为估读。"""
PAPER = {"文件名": "JHM_微生物多样性调控稻田土壤汞循环.pdf", "第一作者": "Qianshuo Zhang", "年份": "2026",
         "期刊": "Journal of Hazardous Materials", "DOI": "10.1016/j.jhazmat.2026.142544",
         "文献核心问题": "微生物多样性下降如何影响汞污染梯度稻田土壤的汞甲基化和 MeHg 去甲基化。",
         "文献主要结论": "在 HX、GX 土中，多样性降低抑制甲基化（为原土的0.31–0.82倍）、促进去甲基化（为原土的1.33–7.00倍）；在 SK 高污染土中结果相反。土壤 THg 约 30,000 ng/g 是决定效应方向的阈值。"}
T1 = [{
    "实验编号": "Zhang2026_JHM_Exp1", "实验名称": "Microcosm incubation experiment（2.2 节）", "实验类型": "A+B",
    "实验目的": "用稀释-灭绝法构建微生物多样性梯度，结合 202HgII/Me198Hg 示踪，量化多样性对 Km、Kd 的影响。",
    "采样地点": "贵州省：SK（废弃汞矿区）、GX（土法炼汞区）、HX（贵阳附近未污染农村）；坐标未在正文给出（Text S1，需查 SI）",
    "土壤数量": "3", "污染背景": "矿区污染（SK、GX）+ 对照（HX）",
    "采样深度": "1–10 cm（土-水界面以下），插秧后 50–60 d 采样（2023年8月）",
    "土样状态": "鲜土；每样点4个点混合；装入无顶空的 500 mL 无菌 PP 瓶，用 Parafilm 封口，4 °C 运输；保存时长未报道",
    "总汞": "HX 165 ng/g，GX 20,707 ng/g，SK 659,303 ng/g（p.3）", "MeHg": "需查 SI（Text S1）",
    "pH": "需查 SI", "有机质": "需查 SI", "硫酸盐": "需查 SI", "铁": "需查 SI",
    "处理组": "OS（原土：20 g 未灭菌土 + 30 mL 灭菌水）；SS（灭菌土对照：20 g γ 辐照灭菌土 + 30 mL 灭菌水）；T1–T3（20 g 灭菌土 + 30 mL 系列稀释接种液；接种液母液为 50 g 土 + 450 mL 灭菌水）",
    "外加汞形态": "仅同位素示踪剂：202Hg(NO3)2、Me198HgNO3", "外加汞剂量": "202HgII 约为本底 THg 的 10%，Me198Hg 约为本底 MeHg 的 100%（Table S1）",
    "相对本底倍数": "202HgII 约 0.1 倍；Me198Hg 约 1 倍", "加汞后平衡": "未报道",
    "其他添加物": "无", "抑制剂": "无", "灭菌对照": "有：γ 辐照（原文“0.6 h−1 gamma irradiation for 48 h”）",
    "土量g": "20", "水量mL": "30", "土水比": "2:3（20 g : 30 mL，按原文数值计算）",
    "容器": "血清瓶（serum bottle），材质和体积未报道", "密封方式": "未报道",
    "气氛": "在 N2 手套箱中操作；加示踪剂后迅速封瓶并移出手套箱培养；取样在手套箱内",
    "预培养": "有：15 °C 预培养1周（激活厌氧微生物）", "温度": "未报道（预培养 15 °C；24 h 示踪培养的温度未明确）",
    "避光": "未报道", "振荡": "未报道", "重复数": "3", "取样方式": "破坏性：24 h 后在手套箱中整瓶取样",
    "示踪剂种类": "202Hg(NO3)2（202HgII）；Me198HgNO3（Me198Hg）", "示踪剂剂量": "202HgII 约为本底 THg 的 10%；Me198Hg 约为本底 MeHg 的 100%",
    "示踪剂预平衡": "未报道", "示踪培养时长": "24 h", "是否测t0": "是（原文：“evaluated initially (t0) and after 24 h (ti)”）",
    "Km公式": "Km = ([Me202Hg]ti − [Me202Hg]t0) / ([202HgII] × (ti − t0))",
    "Kd公式": "Kd = (ln([Me198Hg]t0) − ln([Me198Hg]ti)) / (ti − t0)",
    "同位素测定": "GC-ICP-MS（Agilent 7700x），乙基化-吹扫捕集",
    "总培养时长d": "8（预培养 7 d + 示踪 24 h）", "取样时间点": "t0、24 h",
    "各时间点指标": "t0：Me202Hg、Me198Hg；24 h：Me202Hg、Me198Hg（Km、Kd）、S2−、Fe2+、Fe3+、pH、DOM、16S rRNA、hgcA 丰度",
    "MeHg方法": "需查 SI（Text S3 为土壤本底 THg、MeHg 的测定方法）",
    "质控": "三个平行样的 RSD < 15%；硫化物检出限 0.13 μM；标准物质和回收率：需查 SI",
    "Q_测t0": "是", "Q_示踪剂超本底": "否（202HgII 为 10%，Me198Hg 约等于本底）", "Q_示踪超24h": "否",
    "Q_灭菌对照": "是", "Q_严格厌氧": "不确定（在手套箱中准备和取样，但培养是在手套箱外的密封血清瓶中进行）", "Q_透氧容器": "未报道",
    "原文摘录": ("【土量/水量】“original soil (OS, containing 20 g non-sterilized soil and 30 mL sterilized water)”（p.2）\n"
              "【汞剂量】“The amounts of spiked 202HgII and Me198Hg tracers were ~10% and ~100% (Table S1), respectively, of the soil ambient total Hg (THg) and MeHg concentrations”（p.3）\n"
              "【培养时长/取样】“All treatments were pre-incubated at 15◦C for one week to activate anaerobic microorganisms”（p.2）；“Three bottles were destructively sampled in the glovebox after 24 h of incubation”（p.3）\n"
              "【Km/Kd 公式】“Km = ([Me202Hg]ti − [Me202Hg]t0) / ([202HgII] × (ti − t0)) (1)；Kd = (ln([Me198Hg]t0) − ln([Me198Hg]ti)) / (ti − t0) (2)”；“which were evaluated initially (t0) and after 24 h (ti)”（p.4）"),
    "需查SI字段": "样点信息和本底 MeHg（Text S1）、示踪剂实际加入量（Table S1）、MeHg/THg 测定方法（Text S3）",
    "备注": "灭菌剂量原文写作“0.6 h−1 gamma irradiation for 48 h”，单位表述不完整（不确定）。另有一个全国数据集（250个土样）的统计分析，不是培养实验，未记录。",
}]
_km = {"HX": ["(0.0177)", "(0.0095)", "(0.0073)", "(0.0077)", "(0.0006)"],
       "GX": ["(0.0062)", "(0.0032)", "(0.0043)", "(0.0011)", "(0.0001)"],
       "SK": ["(0.000135)", "(0.000176)", "(0.000213)", "(0.00023)", "(0.000027)"]}
_kd = {"HX": ["(0.31)", "(0.41)", "(1.11)", "(1.12)", "(0.06)"],
       "GX": ["(0.21)", "(0.38)", "(0.49)", "(1.69)", "(0.33)"],
       "SK": ["(1.32)", "(1.14)", "(0.92)", "(0.70)", "(0.39)"]}
T2 = []
for site in _km:
    for ind, d in (("Km", _km), ("Kd", _kd)):
        for trt, v in zip(["OS", "T1", "T2", "T3", "SS（灭菌）"], d[site]):
            T2.append(("Zhang2026_JHM_Exp1", site, trt, "24 h", ind, v, "day−1", "SE（未估读）", "3",
                       f"Fig. 2{'a' if ind == 'Km' else 'b'}（p.5），图中估读", "误差棒为 mean ± SE（p.4）"))
for site, thg in (("HX", "165"), ("GX", "20,707"), ("SK", "659,303")):
    T2.append(("Zhang2026_JHM_Exp1", site, "原土（本底）", "培养前", "THg", thg.replace(",", ""), "ng/g", "未报道", "未报道", "正文 p.3", "原文写作 " + thg + " ng/g"))
EXCLUDED = [("Zhang2026_JHM", "全国 250 个土样数据集的统计分析（2.3 节）", "不是培养实验")]
