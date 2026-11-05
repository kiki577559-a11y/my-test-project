"""Li et al. 2019, Environ. Sci. Technol.（Just Accepted 版，DOI 10.1021/acs.est.8b03511）。页码为 PDF 页码。"""
from .common import NOTRACER
PAPER = {"文件名": "EST_硫酸盐添加促进矿区污染稻田微生物甲基汞产生的机制：汞迁移性变化还是甲基化微生物？.pdf", "第一作者": "Yunyun Li", "年份": "2019",
         "期刊": "Environmental Science & Technology", "DOI": "10.1021/acs.est.8b03511",
         "文献核心问题": "硫酸盐添加促进矿区污染稻田 MeHg 生成，是因为改变了汞的迁移性，还是改变了甲基化微生物。",
         "文献主要结论": "加硫酸盐（50–1000 mg kg–1）使土壤净 MeHg 生成提高28%–61%，稻米 MeHg 提高22%–55%；主要机制是硫酸盐还原产生的硫化物促进 HgS(s) 溶出、提高汞的迁移性，而不是甲基化微生物丰度或活性的变化。"}
_s = dict(NOTRACER, 采样深度="未报道", 土样状态="风干、混匀、过 2 mm 筛；保存条件未报道",
          有机质="未报道", 铁="未报道", 外加汞形态="无（原位污染土，未外加汞）", 外加汞剂量="无", 相对本底倍数="无", 加汞后平衡="无",
          灭菌对照="无", 容器="聚丙烯离心管（Corning，体积未报道）", 密封方式="盖紧后用 Parafilm 封口",
          气氛="未报道（开管测定在充 N2 的手套袋中进行）", 预培养="未报道", 温度="28 °C", 避光="是", 振荡="每天手动混匀2次",
          重复数="3", 取样方式="破坏性：每个时间点开3管", MeHg方法="需查 SI（正文“specified below”部分未摘录）", 质控="需查 SI（标准物质回收率见 SI）",
          Q_测t0="是（0 d）", Q_灭菌对照="否", Q_严格厌氧="否", Q_透氧容器="是（聚丙烯离心管 + Parafilm）")
T1 = [
 {**_s, "实验编号": "Li2019_EST_Exp1", "实验名称": "Batch experiment II（WS 土微宇宙）", "实验类型": "A",
  "实验目的": "考察硫酸盐添加对汞矿区稻田土中甲基化微生物（SRB、hgcA）和 MeHg 生成的影响。",
  "采样地点": "贵州万山汞矿区（WS 土）；具体坐标未报道", "土壤数量": "1", "污染背景": "矿区污染",
  "pH": "未报道", "总汞": "80.8 ± 1.4 mg kg–1", "MeHg": "3.0 ± 0.5 μg kg–1", "硫酸盐": "溶解性硫酸盐 140.9 ± 0.2 mg kg–1；全硫 270 ± 10.1 mg kg–1",
  "处理组": "CK（不添加）；500S（硫酸盐 500 mg S kg–1）；1000S（1000 mg S kg–1）；CK-SRB（加 20 mM 钼酸钠）；所有处理均加 5 mM 乳酸钠",
  "其他添加物": "硫酸盐（500 或 1000 mg S kg–1）；乳酸钠 5 mM（电子供体）", "抑制剂": "Na2MoO4 20 mM（CK-SRB）",
  "土量g": "10", "水量mL": "30（超纯水）", "土水比": "1:3", "总培养时长d": "25", "取样时间点": "0, 5, 10, 15, 20, 25 d",
  "各时间点指标": "各时间点：上覆水 pH、Eh；土壤 MeHg；d0/5/10/15：溶解性硫酸盐；d0、d15：SRB（MPN 法）；d15：hgcA 拷贝数",
  "原文摘录": ("【土量/水量】“Briefly, WS soil (10 g) was placed in the tubes, to which sulfate, sodium molybdate (Na2MoO4, final concentration of 20 mM), and 30 mL of ultrapure water were also added.”（p.10）\n"
            "【培养时长】“The tubes were capped, sealed with Parafilm™, and incubated in darkness at 28 oC for 25 days”（p.11）\n"
            "【取样时间点】“On days 0, 5, 10, 15, 20, and 25, three replicate tubes were opened”（p.11）\n【汞剂量】未外加汞。\n【Km/Kd 公式】无。"),
  "需查SI字段": "MeHg/THg 测定方法与标准物质回收率、hgcA 定量细节",
  "备注": "MeHg 结果只以图呈现，正文未给出数值，表2只记录了本底值。"},
 {**_s, "实验编号": "Li2019_EST_Exp2", "实验名称": "Batch experiment II（补充：QZ、XY、LD、GY 土 20 d 培养）", "实验类型": "A",
  "实验目的": "验证不同 HgS/THg 比例的稻田土中，硫酸盐添加对 MeHg 生成的影响。",
  "采样地点": "贵州清镇（QZ）、陕西旬阳（XY）、湖南娄底（LD）、贵州贵阳（GY）；坐标未报道", "土壤数量": "4（另以 WS 土为参照）",
  "污染背景": "QZ、XY 为矿区污染（HgS/THg 64.7%–75.8%）；LD、GY 为汞矿所在省份的对照点（HgS/THg 23.4%–28.5%）",
  "pH": "未报道", "总汞": "QZ 55.6 ± 0.3，XY 32.9 ± 0.4，LD 0.2 ± 0.0，GY 0.2 ± 0.0 mg kg–1", "MeHg": "QZ 38.4 ± 0.13，XY 4.4 ± 0.07，LD 1.1 ± 0.1，GY 0.08 ± 0.03 μg kg–1",
  "硫酸盐": "未报道",
  "处理组": "加或不加硫酸盐（500 mg S kg–1）；其余条件同 Exp1（“as described above”）", "其他添加物": "硫酸盐 500 mg S kg–1；乳酸钠 5 mM（同 Exp1，不确定）", "抑制剂": "无",
  "土量g": "10（同 Exp1）", "水量mL": "30（同 Exp1）", "土水比": "1:3", "总培养时长d": "20",
  "取样时间点": "QZ、XY：0, 10, 20 d（d15 测 hgcA）；LD、GY：0, 20 d", "各时间点指标": "MeHg；QZ、XY 在 d15 测 hgcA",
  "原文摘录": ("【土量/水量】同 Exp1（“subjected to a 20-day incubation as described above”）（p.11）\n"
            "【培养时长/取样】“the QZ and XY paddy soils were amended or not with sulfate (500 mg S kg–1), and subjected to a 20-day incubation as described above. Concentrations of MeHg in soils were then quantified on days 0, 10 and 20.”（p.11）；“Concentrations of MeHg in LD and GY soils were then quantified on day 0 and 20.”（p.11）\n"
            "【汞剂量】未外加汞。\n【Km/Kd 公式】无。"),
  "需查SI字段": "MeHg 测定方法与质控", "备注": "MeHg 结果只以图呈现，正文未给出数值，表2只记录了本底值。"},
]
T2 = []
for exp, s, thg, ts, me, ms in (("Li2019_EST_Exp1", "WS", "80.8", "1.4", "3.0", "0.5"), ("Li2019_EST_Exp2", "QZ", "55.6", "0.3", "38.4", "0.13"),
                                ("Li2019_EST_Exp2", "XY", "32.9", "0.4", "4.4", "0.07"), ("Li2019_EST_Exp2", "LD", "0.2", "0.0", "1.1", "0.1"),
                                ("Li2019_EST_Exp2", "GY", "0.2", "0.0", "0.08", "0.03")):
    T2.append((exp, s, "原土", "培养前", "THg", thg, "mg kg−1", "± " + ts + "（SD/SE 未说明）", "未报道", "正文 p.7–8", ""))
    T2.append((exp, s, "原土", "培养前", "MeHg", me, "μg kg−1", "± " + ms + "（SD/SE 未说明）", "未报道", "正文 p.7–8", ""))
EXCLUDED = [("Li2019_EST", "Batch experiment I（HgS 颗粒加硫化物 7 d；YX 土加 HgCl2 50 mg/kg 后加硫化物 18 h）", "前者体系不含土壤；后者是汞迁移性实验，未说明淹水/厌氧条件，且不测甲基化"),
            ("Li2019_EST", "盆栽实验（WS 土种稻，5个硫酸盐处理）", "盆栽，有植物")]
