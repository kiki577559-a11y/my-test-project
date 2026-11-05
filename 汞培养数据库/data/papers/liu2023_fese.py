"""Liu et al. 2023, Frontiers of Environmental Science & Engineering 17(12): 145。页码为 PDF 页码。"""
from .common import NOTRACER
PAPER = {"文件名": "FESE_汞污染土壤甲基汞生成增加及其在水稻中的积累：藻类分解的关键作用.pdf", "第一作者": "Di Liu", "年份": "2023",
         "期刊": "Frontiers of Environmental Science & Engineering", "DOI": "10.1007/s11783-023-1745-6",
         "文献核心问题": "汞污染稻田中藻类分解如何影响土壤 MeHg 生成及其在水稻中的积累。",
         "文献主要结论": "盆栽和微宇宙实验表明，藻类分解提高了土壤 MeHg 和水稻 MeHg 积累；微宇宙前10 d 内分解藻屑中的 MeHg 显著下降，提示其可能是土壤 MeHg 的来源之一。"}
T1 = [{**NOTRACER,
    "实验编号": "LiuD2023_FESE_Exp1", "实验名称": "microcosm experiment（2.2 节）", "实验类型": "A",
    "实验目的": "考察分解藻类聚集体对土-水体系中 MeHg 分布的作用。",
    "采样地点": "贵州省万山汞矿区稻田（27°33′51″N，109°11′35″E）", "土壤数量": "1", "污染背景": "矿区污染",
    "采样深度": "0−20 cm", "土样状态": "研磨、过 100 目（147 μm）尼龙筛（微宇宙用）；风干与否及保存条件：未报道",
    "pH": "需查 SI（Table S1）", "有机质": "需查 SI", "总汞": "5.2 mg/kg（Table S1）", "MeHg": "需查 SI", "硫酸盐": "需查 SI", "铁": "需查 SI",
    "处理组": "AW（藻 + 水，无土）；AWS（藻 + 土 + 水）", "外加汞形态": "无（原位污染土）", "外加汞剂量": "无", "相对本底倍数": "无", "加汞后平衡": "无",
    "其他添加物": "藻粉 0.2 g（丝状藻，装在 1600 目尼龙凋落物袋中，悬于上覆水中），培养开始时加入", "抑制剂": "无", "灭菌对照": "无",
    "土量g": "40", "水量mL": "60（超纯水）", "土水比": "2:3", "容器": "100 mL PTFE 离心管（Corning）", "密封方式": "未报道", "气氛": "未报道",
    "预培养": "未报道", "温度": "26 °C（人工气候箱）", "避光": "未报道", "振荡": "未报道", "重复数": "3", "取样方式": "不确定（未说明藻屑袋是从同一反应器中分次取出，还是破坏性取样）",
    "总培养时长d": "25", "取样时间点": "0, 1, 3, 6, 10, 15, 20, 25 d（藻屑）",
    "各时间点指标": "各时间点：藻屑质量损失、藻屑 THg、MeHg；土壤和上覆水的测定：未报道",
    "MeHg方法": "土壤 THg：王水消解，BrCl 氧化，SnCl2 还原，金管富集，CVAFS（Brooks Rand）；MeHg 方法引自文献（未详述）",
    "质控": "THg 标准物质 GBW10020、GBW07405；MeHg 标准物质 ERM-CC580、TORT-3；标准物质和加标回收率 85%–110%；平行样 RSD < 15%",
    "Q_测t0": "是（0 d）", "Q_灭菌对照": "否", "Q_严格厌氧": "未报道", "Q_透氧容器": "否（PTFE）",
    "原文摘录": ("【土量/水量】“For AWS, 40 g of soil was weighed in the bottom of the reactor before adding 60 mL of ultrapure water and 0.2 g of algal powders to the litterbags, which were suspended in the overlying water above the soil surface.”（p.3）\n"
              "【培养时长】“Thereafter, they were incubated at a constant temperature of 26 °C in an artificial climate chamber (SPX-250BIII, Tianjin, China) for 25 days.”（p.3）\n"
              "【取样时间点】“In the microcosm experiment, algal debris in the litterbags was collected at 0, 1, 3, 6, 10, 15, 20, and 25 d”（p.3）\n"
              "【汞剂量】未外加汞。\n【Km/Kd 公式】无。"),
    "需查SI字段": "土壤性质（Table S1）、反应器示意图（Fig. S1）",
    "备注": "微宇宙中测定的对象是藻屑（不是土壤），因此表2没有土壤 MeHg 的数值。是否淹水：有 60 mL 上覆水，可视为淹水；是否厌氧未报道。同文的盆栽实验已排除。",
}]
T2 = [("LiuD2023_FESE_Exp1", "万山汞污染稻田土", "原土", "培养前", "THg", "5.2", "mg/kg", "未报道", "未报道", "正文 p.3（Table S1）", "")]
EXCLUDED = [("LiuD2023_FESE", "盆栽实验（5 L 桶，2 kg 土，种水稻）", "盆栽，有植物")]
