"""第0步：列出全部PDF，按MD5去重，正文与SI配对，并抽取全文文本（带页码标记）。"""
import hashlib, json, re, sys
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[2]          # 仓库根目录
OUT = Path(__file__).resolve().parents[1] / "_work"
TXT = OUT / "text"
TXT.mkdir(parents=True, exist_ok=True)

SI_PAT = re.compile(r"(?:[_\-\s]?(?:SI|si|Supporting[ _]Information|Supplementary.*|补充材料))\.pdf$")

pdfs = sorted(p for p in ROOT.rglob("*.pdf") if "汞培养数据库" not in p.parts and ".git" not in p.parts)
recs = []
for p in pdfs:
    h = hashlib.md5(p.read_bytes()).hexdigest()
    recs.append({"path": str(p.relative_to(ROOT)), "name": p.name, "md5": h,
                 "is_si": bool(SI_PAT.search(p.name))})

# 去重：同 MD5 视为同一文件，保留第一个出现的路径
uniq = {}
for r in recs:
    uniq.setdefault(r["md5"], {**r, "copies": []})["copies"].append(r["path"])
docs = list(uniq.values())

# 同名但不同MD5的情况单独报告
by_name = {}
for r in recs:
    by_name.setdefault(r["name"], set()).add(r["md5"])
same_name_diff = {n: len(s) for n, s in by_name.items() if len(s) > 1}

# SI 配对
mains = [d for d in docs if not d["is_si"]]
sis = [d for d in docs if d["is_si"]]
def stem_main(name):
    return SI_PAT.sub("", name).rstrip("_- ")
for d in mains:
    d["si"] = None
for s in sis:
    key = stem_main(s["name"])
    match = [m for m in mains if m["name"][:-4] == key]
    s["pair"] = match[0]["path"] if match else None
    if match:
        match[0]["si"] = s["path"]

# 抽取全文
for d in docs:
    doc = pymupdf.open(ROOT / d["path"])
    d["pages"] = doc.page_count
    parts = [f"\n=====[PAGE {i+1}]=====\n" + pg.get_text() for i, pg in enumerate(doc)]
    txt = "".join(parts)
    d["chars"] = len(txt)
    d["id"] = d["md5"][:8]
    (TXT / f"{d['id']}.txt").write_text(txt, encoding="utf-8")

json.dump({"docs": docs, "same_name_diff_md5": same_name_diff}, open(OUT / "inventory.json", "w"), ensure_ascii=False, indent=1)
print(f"PDF总数 {len(recs)}；去重后 {len(docs)}（正文 {len(mains)}，SI {len(sis)}）")
print("同名不同内容：", same_name_diff or "无")
for s in sis:
    print("SI配对：", s["name"], "->", s["pair"])
for d in docs:
    flag = "" if d["chars"] > d["pages"] * 500 else "  <-- 文本过少，可能是扫描件"
    print(f"{d['id']} p{d['pages']:>3} c{d['chars']:>7} copies={len(d['copies'])} {d['path']}{flag}")
