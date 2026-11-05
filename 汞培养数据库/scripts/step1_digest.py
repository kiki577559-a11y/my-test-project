"""第1步：为每篇正文（及SI）生成筛选摘要：标题、摘要、方法部分定位、与培养相关的段落（带页码）。"""
import json, re
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
W = Path(__file__).resolve().parents[1] / "_work"
inv = json.load(open(W / "inventory.json"))
(W / "blocks").mkdir(exist_ok=True)

M_HEAD = re.compile(r"^[\s■•\d\.IVX]*(materials?\s+and\s+methods?|methods?|experimental(\s+section|\s+procedures?)?|methodology|materials\s*&\s*methods|online\s+methods)(\s|$|:)", re.I)
R_HEAD = re.compile(r"^[\s■•\d\.IVX]*(results(\s+and\s+discussion)?|results\s*&\s*discussion|discussion|conclusions?|acknowledg(e)?ments?|references|data availability)(\s|$|:)", re.I)
KW = re.compile(r"incubat|microcosm|slurr|flood|anoxic|anaerob|spike|isotop|enriched|\b(19[89]|20[0-4])\s*Hg|Me\s*(19[89]|20[0-4])|glove|serum bottle|pot experiment|rhizobox|pure culture|strain|K\s*m\b|k\s*meth|demethylation rate|methylation rate|paddy|rice field|sediment", re.I)

def blocks_of(path):
    doc = pymupdf.open(path)
    out = []
    for i, pg in enumerate(doc):
        for b in pg.get_text("blocks"):
            t = re.sub(r"\s+", " ", b[4]).strip()
            if t:
                out.append((i + 1, t))
    return out

digest = []
for d in inv["docs"]:
    bl = blocks_of(ROOT / d["path"])
    json.dump(bl, open(W / "blocks" / f"{d['id']}.json", "w"), ensure_ascii=False)
    head = " ".join(t for p, t in bl if p == 1)[:1800]
    ms = [k for k, (p, t) in enumerate(bl) if M_HEAD.match(t) and (len(t) < 60 or t.split()[0].isupper() or t.startswith('■'))]
    mstart = None
    for k in ms:
        if bl[k][0] > 1 or len(ms) == 1:
            mstart = k; break
    if mstart is None and ms:
        mstart = ms[0]
    mend = None
    if mstart is not None:
        for k in range(mstart + 1, len(bl)):
            if R_HEAD.match(bl[k][1]) and (len(bl[k][1]) < 80 or bl[k][1].startswith('■')):
                mend = k; break
        mend = mend or min(len(bl), mstart + 150)
        region = bl[mstart:mend]
    else:
        region = bl
    hits = [(p, t) for p, t in region if KW.search(t)]
    # 方法识别失败或方法中无命中时，在全文中找关键词段落
    if not hits:
        hits = [(p, t) for p, t in bl if KW.search(t)]
    snip = []
    total = 0
    for p, t in hits:
        s = f"[p{p}] {t[:700]}"
        if total + len(s) > 6000: break
        snip.append(s); total += len(s)
    digest.append({"id": d["id"], "path": d["path"], "is_si": d["is_si"],
                   "si": d.get("si"), "methods_found": mstart is not None,
                   "methods_pages": [bl[mstart][0], bl[mend - 1][0]] if mstart is not None else None,
                   "head": head, "snips": snip})
json.dump(digest, open(W / "digest.json", "w"), ensure_ascii=False, indent=1)
print(sum(x["methods_found"] for x in digest), "/", len(digest), "识别到方法部分")
for x in digest:
    if not x["methods_found"]:
        print("未识别：", x["id"], x["path"])
