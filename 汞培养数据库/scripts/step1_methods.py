"""按文献ID打印方法部分中与实验设计相关的段落（每段截断），用于人工判断。"""
import json, re, sys
dig = {x["id"]: x for x in json.load(open("digest.json"))}
M_HEAD = re.compile(r"^[\s■•\d\.IVX]*(materials?\s+and\s+methods?|methods?|experimental(\s+section)?|methodology|online\s+methods)(\s|$|:)", re.I)
R_HEAD = re.compile(r"^[\s■•\d\.IVX]*(results(\s+and\s+discussion)?|discussion|conclusions?|acknowledg|references|data availability)(\s|$|:)", re.I)
KEY = re.compile(r"incubat|microcosm|slurr|\bpots?\b|rhizobox|tracer|spik|glove|serum|bottle|tube|vial|jar|flood|sieved|air-dried|freeze|collected|experiment\s*[I1-9]|batch|treatment|replicat|inhibit|molybdate|autoclav|steril|\bK ?m\b|\bK ?d\b|k ?meth|rate constant|sampl(ed|ing) (on|at) day|days? \d|d\)|soil:water|water ratio|g of (soil|fresh|dry)", re.I)
per = int(sys.argv[1]); ids = sys.argv[2:]
for i in ids:
    x = dig[i]; bl = json.load(open(f"blocks/{i}.json"))
    st = None
    for k,(p,t) in enumerate(bl):
        if M_HEAD.match(t) and (len(t)<60 or t.startswith("■")) and p>1: st=k; break
    if st is None:
        for k,(p,t) in enumerate(bl):
            if M_HEAD.match(t) and (len(t)<60 or t.startswith("■")): st=k; break
    en = len(bl)
    if st is not None:
        for k in range(st+1,len(bl)):
            if R_HEAD.match(bl[k][1]) and (len(bl[k][1])<80 or bl[k][1].startswith("■")): en=k; break
    reg = bl[st:en] if st is not None else bl
    print(f"## {i} | {x['path'].split('/',1)[1][:70]} | 方法={'是' if st is not None else '否'}")
    n=0
    for p,t in reg:
        if KEY.search(t) and len(t)>40:
            s=f"[p{p}] {t[:420]}"
            if n+len(s)>per: break
            print(s); n+=len(s)
    print()
