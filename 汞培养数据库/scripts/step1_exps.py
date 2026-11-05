"""列出方法部分中与实验划分相关的小标题/句子，帮助计数培养实验。"""
import json, re, sys
PAT = re.compile(r"(experiment|batch|assay|incubation|microcosm|treatment)s?\s*(\d|[IVX]+\b|[A-C]\b)|(incubation|microcosm|slurry|tracer|batch|pot|kinetic) (experiment|incubation|assay|study)|(first|second|third) (experiment|incubation|set)|Km|Kd|k ?meth|rate constant|(\d+)[- ]?(d|days|h|hours?)\b.*incubat|incubat.*\b(\d+)[- ]?(d|days|h)\b", re.I)
REF = re.compile(r"^(■\s*)?(references?|acknowledg)", re.I)
for i in sys.argv[2:]:
    bl = json.load(open(f"blocks/{i}.json")); out=[]; n=0
    for p,t in bl:
        if REF.match(t) and p>2: break
        for s in re.split(r"(?<=[.;])\s+(?=[A-Z(])", t):
            if PAT.search(s) and 25<len(s)<420:
                ss=f"[p{p}] {s}"
                if n+len(ss)>int(sys.argv[1]): break
                out.append(ss); n+=len(ss)
    print("##", i); print("\n".join(out)); print()
