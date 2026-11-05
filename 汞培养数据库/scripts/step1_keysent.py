"""为筛选打印每篇文献中与实验设计相关的关键句（排除参考文献部分），带页码。"""
import json, re, sys
dig = json.load(open("digest.json"))
STRONG = re.compile(r"incubat|microcosm|slurr|pot (experiment|trial)|rhizobox|pots?\b.*(rice|plant)|pure cultur|culture[sd]? (of|were)|strain|field (survey|sampling|experiment|trial)|in situ|core[sd]? incubation|enriched (stable )?isotop|isotope tracer|\b(19[89]|20[0-2])Hg|Me(19[89]|20[0-2])Hg|K ?m\b|K ?d\b|k ?meth|glove ?box|serum bottle|flooded|anoxic", re.I)
REF = re.compile(r"^(■\s*)?references?\b|^literature cited", re.I)
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for x in dig[lo:hi]:
    bl = json.load(open(f"blocks/{x['id']}.json"))
    # 截断参考文献
    cut = len(bl)
    for k, (p, t) in enumerate(bl):
        if REF.match(t) and k > len(bl) * 0.4:
            cut = k; break
    sents = []
    for p, t in bl[:cut]:
        for s in re.split(r"(?<=[.;])\s+(?=[A-Z(])", t):
            if STRONG.search(s) and 30 < len(s) < 500:
                sents.append(f"[p{p}] {s}")
    out, n = [], 0
    seen = set()
    for s in sents:
        k = s[6:60]
        if k in seen: continue
        seen.add(k)
        if n + len(s) > 1400: break
        out.append(s); n += len(s)
    print(f"## {x['id']} | {x['path'].split('/',1)[1][:60]} | M={x['methods_found']} {x['methods_pages']}")
    print("\n".join(out) or "(无关键句)")
    print()
