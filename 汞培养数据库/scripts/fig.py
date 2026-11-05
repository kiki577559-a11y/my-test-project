"""渲染PDF某页（或某区域，坐标为页面比例 x0 y0 x1 y1）为PNG用于图中估读与核对。用法: fig.py <id> <page> [dpi] [x0 y0 x1 y1]"""
import json, sys
from pathlib import Path
import pymupdf
B = Path(__file__).resolve().parents[1]; R = B.parent
inv = {d["id"]: d for d in json.load(open(B / "_work/inventory.json"))["docs"]}
i, pg = sys.argv[1], int(sys.argv[2]); dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 110
d = pymupdf.open(R / inv[i]["path"]); p = d[pg - 1]; r = p.rect
clip = r
if len(sys.argv) > 7:
    x0, y0, x1, y1 = map(float, sys.argv[4:8]); clip = pymupdf.Rect(r.width*x0, r.height*y0, r.width*x1, r.height*y1)
out = Path("/tmp/claude-0/-home-user-my-test-project/6693b062-e69c-54f2-9870-a68719e6ebab/scratchpad/fig") / f"{i}_p{pg}.png"
p.get_pixmap(dpi=dpi, clip=clip).save(out); print(out)
