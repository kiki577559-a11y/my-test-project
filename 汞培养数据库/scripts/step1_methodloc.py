"""改进的方法部分定位：块首标题、块内大写标题（ACS 的 ■MATERIALS AND METHODS）、Nature 式文末 Methods。输出 methods_loc.json"""
import json, re
dig = json.load(open("digest.json"))
P1 = re.compile(r"^[\s■•\d\.IVX]*(materials?\s+and\s+methods?|methods?|experimental(\s+section|\s+procedures?)?|methodology|online\s+methods|materials\s*&\s*methods)(\s|$|:)", re.I)
P2 = re.compile(r"(■\s*|\b\d\.\s*)(MATERIALS AND METHODS|EXPERIMENTAL SECTION|METHODS)\b")
P3 = re.compile(r"\b(MATERIALS AND METHODS|EXPERIMENTAL SECTION)\b")
res = {}
for x in dig:
    bl = json.load(open(f"blocks/{x['id']}.json"))
    hit = None
    for k,(p,t) in enumerate(bl):
        if (P1.match(t) and (len(t) < 80 or t.split()[0].isupper())) or P2.search(t) or (P3.search(t) and p > 1) or (p > 2 and re.match(r"^(Online )?Methods\s+[A-Z]", t)):
            if p == 1 and len(bl) > 30 and re.match(r"(?i)^\s*methods?\b", t) is None and not P2.search(t):
                continue
            hit = (p, t[:80]); break
    res[x["id"]] = hit
json.dump(res, open("methods_loc.json","w"), ensure_ascii=False, indent=0)
fail = [x for x in dig if res[x["id"]] is None]
print(len(dig)-len(fail), "/", len(dig))
for x in fail: print(x["id"], x["path"].split("/",1)[1][:60])
