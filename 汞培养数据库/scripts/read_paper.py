"""阅读辅助：打印方法部分全文（合并断行）、含数值单位的结果句、表格/图注。
用法: read_paper.py <id> methods [maxchars] | nums [maxchars] | caps | page <n> [maxchars] | grep <regex>"""
import json, re, sys
from pathlib import Path
W = Path(__file__).resolve().parents[1] / "_work"
i, mode = sys.argv[1], sys.argv[2]
bl = json.load(open(W / "blocks" / f"{i}.json"))
def clean(t): return re.sub(r"\s+", " ", t.replace("­ ", "").replace("­", ""))
REF = re.compile(r"^(■\s*)?(references?|acknowledg|literature cited)\b", re.I)
cut = len(bl)
for k,(p,t) in enumerate(bl):
    if REF.match(t) and k > len(bl)*0.4: cut = k; break
body = bl[:cut]
M = re.compile(r"(materials?\s+and\s+methods?|experimental section|^methods?\b|^\d\.\s*methods?)", re.I)
R = re.compile(r"^[\s■\d\.]*(results(\s+and\s+discussion)?)\b", re.I)
if mode == "methods":
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 9000
    st = next((k for k,(p,t) in enumerate(body) if M.search(t[:60]) and (p>1 or k>5)), 0)
    en = next((k for k in range(st+1,len(body)) if R.match(body[k][1]) and len(body[k][1])<200), len(body))
    s = " ".join(f"[p{p}] {clean(t)}" if k==st or body[k-1][0]!=p else clean(t) for k,(p,t) in enumerate(body[st:en], st))
    print(s[:n])
elif mode == "nums":
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 6000
    st = next((k for k,(p,t) in enumerate(body) if R.match(t) and len(t)<200), 0)
    out=[]; tot=0
    for p,t in body[st:]:
        for s in re.split(r"(?<=[a-z\)\]])\.\s+(?=[A-Z(])", clean(t)):
            if re.search(r"\d\s*(ng|μg|µg|mg|%|d−1|d-1|day|h−1|/d|fold|×\s*10)", s) and len(s)<600:
                x=f"[p{p}] {s}"; tot+=len(x)
                if tot>n: break
                out.append(x)
    print("\n".join(out))
elif mode == "caps":
    for p,t in body:
        if re.match(r"^(Fig(ure)?\.?\s*\d|Table\s*\d)", t.strip()): print(f"[p{p}] {clean(t)[:400]}")
elif mode == "page":
    n = int(sys.argv[4]) if len(sys.argv) > 4 else 8000
    print(" ".join(clean(t) for p,t in bl if p==int(sys.argv[3]))[:n])
elif mode == "grep":
    for p,t in body:
        for s in re.split(r"(?<=[a-z\)\]])\.\s+(?=[A-Z(])", clean(t)):
            if re.search(sys.argv[3], s):
                try: print(f"[p{p}] {s[:500]}")
                except BrokenPipeError: sys.exit(0)
