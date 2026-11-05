"""Wu et al. 2023, Journal of Hazardous Materials 460: 132486。页码为 PDF 页码。"""
PAPER = {"文件名": "JHM_稻田中硫酸盐还原和产甲烷作用与Hg(II)及甲基汞还原相耦合.pdf", "第一作者": "Qingqing Wu", "年份": "2023",
         "期刊": "Journal of Hazardous Materials", "DOI": "10.1016/j.jhazmat.2023.132486",
         "文献核心问题": "在汞污染梯度稻田土壤中，Hg(II) 和 MeHg 的还原过程如何发生，硫酸盐还原和产甲烷作用分别贡献多少。",
         "文献主要结论": "高污染土壤中硫酸盐还原强烈影响 Hg(II) 还原；产甲烷作用是控制 MeHg 还原的重要微生物过程；在培养条件下，最多99%的 MeHg 去甲基化为氧化去甲基化；Hg(II) 还原可能限制废弃汞矿区稻田的 Hg(II) 甲基化。"}
T1 = [{
    "实验编号": "Wu2023_JHM_Exp1", "实验名称": "Microcosm incubations（2.2 Microcosm incubations setup）", "实验类型": "B",
    "实验目的": "用 202Hg(NO3)2、CH3198HgNO3 示踪剂结合钼酸盐/BES 抑制剂梯度，同时测定 Hg(II) 还原、MeHg 还原、甲基化和去甲基化速率常数。",
    "采样地点": "贵州省：Sikeng（废弃汞矿区）、Gouxi（土法炼汞区，均在万山汞矿区）；Huaxi（贵阳西南，对照）；坐标见 Fig. 1（正文未列出）",
    "土壤数量": "3", "污染背景": "矿区污染（Sikeng、Gouxi）+ 对照（Huaxi）", "采样深度": "0–2 cm（表层土）",
    "土样状态": "鲜土；每样点3个子样，每个约 2 L；与上覆水混合制泥浆（去除石子和根）；保存条件未报道",
    "pH": "Huaxi 8.23 ± 0.58，Gouxi 7.41 ± 0.02，Sikeng 9.87 ± 0.26（Table 1，p.5；未说明是野外原样还是培养后）",
    "有机质": "未报道", "总汞": "Huaxi 0.46 ± 0.01，Gouxi 37.16 ± 31.46，Sikeng 65.75 ± 46.19 mg⋅kg−1（Table 1，标注*引自配套研究 [12]）",
    "MeHg": "Huaxi 0.96 ± 0.24，Gouxi 2.07 ± 1.23，Sikeng 0.98 ± 0.25 μg⋅kg−1（Table 1，引自 [12]）",
    "硫酸盐": "未报道（Table 2 为 XANES 测定的 Na2SO4 形态占总 S 的 24%–25%）", "铁": "Fe2+：Huaxi 95.52 ± 12.70，Gouxi 33.24 ± 12.97，Sikeng 11.93 ± 3.90 μM（Table 1）",
    "处理组": "reference control（原泥浆）；钼酸盐梯度（5、10、20、50 mM）；BES 梯度（5、10、20、50 mM）；Mo + BES（20 mM 钼酸盐 + 50 mM BES）；autoclaved（121 °C，30 min）",
    "外加汞形态": "仅示踪剂：202Hg(NO3)2（98.68%）、CH3198HgNO3（98.52%，合成纯度 83.2%）", "外加汞剂量": "202Hg 为本底 THg 的 10%；Me198Hg 为本底 MeHg 的 100%",
    "相对本底倍数": "202Hg 0.1 倍；Me198Hg 1 倍", "加汞后平衡": "未报道", "其他添加物": "无",
    "抑制剂": "钼酸盐 5/10/20/50 mM；BES 5/10/20/50 mM；Mo + BES 20 + 50 mM", "灭菌对照": "有：高压灭菌 121 °C，30 min",
    "土量g": "未报道（每瓶约 30 mL 泥浆）", "水量mL": "未报道（泥浆含水率约 55%）", "土水比": "不确定（只报道含水率约 55%）",
    "容器": "100 mL 血清瓶", "密封方式": "丁基胶塞 + 铝盖压封", "气氛": "全部操作在 Ar/H2（9:1）厌氧箱中进行；试剂均脱氧", "预培养": "未报道",
    "温度": "25 °C（室温）", "避光": "是", "振荡": "未报道", "重复数": "t1：1瓶；t2：3瓶", "取样方式": "破坏性（t1、t2 各自牺牲整瓶）",
    "示踪剂种类": "202Hg(NO3)2；CH3198HgNO3", "示踪剂剂量": "202Hg 为本底 THg 的 10%；Me198Hg 为本底 MeHg 的 100%", "示踪剂预平衡": "无（t1 在加示踪剂后 5 min 内取样）",
    "示踪培养时长": "24 h", "是否测t0": "是（t1：加示踪剂后 5 min 内牺牲1瓶）",
    "Km公式": "km = ([Me202Hg]t2 − [Me202Hg]t1) / ([202Hg2+] × t)", "Kd公式": "kd = (In([Me198Hg]t1) − In([Me198Hg]t2)) / t",
    "同位素测定": "MeHg 同位素：GC-ICPMS；Hg(0)：N2 吹扫、金管捕集、ICPMS（Agilent 7700x）",
    "总培养时长d": "1（24 h）", "取样时间点": "t1（加示踪剂后 5 min 内）、t2（24 h）",
    "各时间点指标": "t1、t2：202Hg(0)、198Hg(0)（计算 kre-Hg(II)、kre-MeHg）、Me202Hg、Me198Hg（km、kd）；部分样品：RNA/DNA（merA、hgcA、16S、dsrA、mcrA 的 RT-qPCR）；CH4、CO2",
    "MeHg方法": "按文献 [64] 的方法（正文未详述）", "质控": "未报道",
    "Q_测t0": "是", "Q_示踪剂超本底": "否（202Hg 为 10%，Me198Hg 等于本底）", "Q_示踪超24h": "否", "Q_灭菌对照": "是", "Q_严格厌氧": "是", "Q_透氧容器": "否",
    "原文摘录": ("【土量/水量】“The water content of the slurries … was about 55%. Approximately 30 mL slurries were dispensed into a 100 mL serum bottle by careful pipetting”（p.3）\n"
              "【汞剂量】“Two Hg isotope tracers, CH3 198HgNO3 (98.52 ± 0.15%) and 202Hg (NO3)2 (98.68 ± 0.2%), were added at 100% and 10% of ambient concentrations of each site”（p.3）\n"
              "【培养时长】“All serum bottles were sealed with butyl rubber septa and aluminum crimp caps and subsequently incubated in the dark at room temperature (25 ℃) for 24 h.”（p.3）\n"
              "【取样时间点】“Within 5 min after tracer addition, Hg(0) from sacrificed serum bottles was purged out … These samples were designated as “t1”. After 24 h of incubation … These samples were designated “t2”.”（p.3）\n"
              "【Km/Kd 公式】“km = ([Me202Hg]t2 − [Me202Hg]t1) / ([202Hg2+] × t) (3)”；“kd = (In([Me198Hg]t1) − In([Me198Hg]t2)) / t (4)”（p.3–4；按文字层整理，分式结构未逐一按页面图核对）"),
    "需查SI字段": "相关性分析（Table S5）",
    "备注": "本文正文没有给出本实验的 km、kd 数值；Table 3 中稻田土的 km/kd 引自配套研究 [12]（与 Wu 2020 EST 为同一样点、同一层位，可能为同批样品，不确定），未记入表2。表2只记录 Table 1 中的 THg、MeHg。kre（还原速率常数）不属于规定的5项指标，未记录。",
}]
T2 = []
for site, thg, ts, me, ms in (("Huaxi", "0.46", "0.01", "0.96", "0.24"), ("Gouxi", "37.16", "31.46", "2.07", "1.23"), ("Sikeng", "65.75", "46.19", "0.98", "0.25")):
    T2.append(("Wu2023_JHM_Exp1", site + " 0–2 cm", "野外原样", "培养前", "THg", thg, "mg kg−1", "± " + ts + "（SD/SE 未说明）", "未报道", "Table 1（p.5）", "引自配套研究 [12]"))
    T2.append(("Wu2023_JHM_Exp1", site + " 0–2 cm", "野外原样", "培养前", "MeHg", me, "μg kg−1", "± " + ms + "（SD/SE 未说明）", "未报道", "Table 1（p.5）", "引自配套研究 [12]"))
EXCLUDED = []
