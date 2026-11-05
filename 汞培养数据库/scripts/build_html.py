"""从 Excel 数据库生成单文件离线浏览页“数据库浏览.html”（数据内嵌，不依赖网络）。"""
import json
from pathlib import Path
from openpyxl import load_workbook

B = Path(__file__).resolve().parents[1]
wb = load_workbook(B / "稻田汞培养数据库.xlsx", read_only=True)


def sheet(name):
    rows = list(wb[name].iter_rows(values_only=True))
    return {"cols": [str(c) for c in rows[0]], "rows": [["" if v is None else str(v) for v in r] for r in rows[1:]]}


DATA = {"t1": sheet("表1_培养条件"), "t2": sheet("表2_结果数值")}

HTML = r"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>稻田汞培养数据库</title>
<style>
:root{--bg:#fafaf8;--fg:#1d1d1b;--muted:#6b6b66;--line:#dcdcd6;--card:#fff;--head:#eef2f7;--accent:#2f5d8a;
--unrep:#e6e6e3;--si:#f8d9c6;--unc:#fbeeb0;--est:#dbe9f7}
@media (prefers-color-scheme:dark){:root{--bg:#161616;--fg:#e8e8e4;--muted:#a3a39c;--line:#3a3a37;--card:#1f1f1e;--head:#26303b;--accent:#8fb6e0;
--unrep:#3a3a38;--si:#5a3a28;--unc:#57501f;--est:#253b52}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.5 system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif}
header{padding:16px;border-bottom:1px solid var(--line)}h1{font-size:18px;margin:0 0 4px}.sub{color:var(--muted);font-size:13px}
.tabs{display:flex;gap:8px;padding:12px 16px 0}.tab{border:1px solid var(--line);background:var(--card);color:var(--fg);padding:6px 14px;border-radius:6px 6px 0 0;cursor:pointer}
.tab.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.bar{display:flex;flex-wrap:wrap;gap:8px;padding:12px 16px;border-bottom:1px solid var(--line);background:var(--card)}
.bar label{font-size:12px;color:var(--muted);display:flex;flex-direction:column;gap:2px}
select,input{font:inherit;padding:4px 6px;border:1px solid var(--line);border-radius:4px;background:var(--bg);color:var(--fg);min-width:120px}
input[type=search]{min-width:220px}.count{align-self:flex-end;color:var(--muted);font-size:12px;margin-left:auto}
.legend{display:flex;gap:10px;flex-wrap:wrap;padding:8px 16px;font-size:12px;color:var(--muted)}.legend span{padding:1px 6px;border-radius:3px;color:var(--fg)}
.wrap{overflow:auto;max-height:calc(100vh - 230px);margin:0 16px 16px;border:1px solid var(--line)}
table{border-collapse:collapse;font-size:12.5px}th,td{border:1px solid var(--line);padding:4px 6px;vertical-align:top;text-align:left}
th{position:sticky;top:0;background:var(--head);z-index:1;white-space:nowrap}
td{max-width:340px;white-space:pre-wrap;word-break:break-word}td.long{min-width:260px}
td:first-child,th:first-child{position:sticky;left:0;background:var(--card);z-index:2}th:first-child{background:var(--head);z-index:3}
.unrep{background:var(--unrep)}.si{background:var(--si)}.unc{background:var(--unc)}.est{background:var(--est)}
mark{background:#ffe066;color:#000}
@media (max-width:600px){.wrap{margin:0;max-height:none}.bar{padding:12px}input[type=search]{min-width:0;width:100%}}
</style></head><body>
<header><h1>稻田汞培养实验数据库</h1><div class="sub">数据来源：稻田汞培养数据库.xlsx（离线浏览，数据内嵌）。表1每行一个实验批次；表2每行一个“实验×土壤×处理×时间点×指标”。</div></header>
<div class="tabs"><button class="tab on" data-t="t1">表1 培养条件</button><button class="tab" data-t="t2">表2 结果数值</button></div>
<div class="bar" id="bar"></div>
<div class="legend"><span class="unrep">未报道</span><span class="si">需查 SI</span><span class="unc">不确定</span><span class="est">(图中估读)</span></div>
<div class="wrap"><table id="tbl"></table></div>
<script>
const D = __DATA__;
let cur = "t1";
const F1 = [
 ["实验类型","实验类型",v=>v],
 ["外加汞形态","外加汞形态",v=>v.split(/[（(；;]/)[0].trim()||v],
 ["有无同位素示踪","示踪剂种类",v=>v.startsWith("无")?"无":"有"],
 ["【质量】测了 t0","【质量】测了 t0",q],["【质量】示踪剂剂量超过本底汞","【质量】示踪剂剂量超过本底汞",q],
 ["【质量】同位素示踪培养超过 24 h","【质量】同位素示踪培养超过 24 h",q],["【质量】设有灭菌对照","【质量】设有灭菌对照",q],
 ["【质量】手套箱/严格厌氧","【质量】手套箱/严格厌氧",q],["【质量】使用透氧容器或密封材料","【质量】使用透氧容器或密封材料",q]];
const F2 = [["实验编号","实验编号",v=>v],["指标","指标",v=>v],["数据来源","数据出处",v=>v.includes("估读")?"图中估读":"正文/表格"]];
function q(v){return v.split(/[（(]/)[0].trim()}
function cls(v){if(/^\(.*\)$/.test(v.trim()))return"est";if(v.includes("不确定"))return"unc";if(v.includes("需查 SI")||v.includes("需查SI"))return"si";if(v.startsWith("未报道"))return"unrep";return""}
function esc(s){return s.replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]))}
function filters(){return cur==="t1"?F1:F2}
function buildBar(){
  const d=D[cur], bar=document.getElementById("bar"); bar.innerHTML="";
  filters().forEach(([lab,col,fn],i)=>{const ci=d.cols.indexOf(col); if(ci<0)return;
    const vals=[...new Set(d.rows.map(r=>fn(r[ci])))].sort();
    const s=document.createElement("select"); s.dataset.i=i; s.innerHTML='<option value="">全部</option>'+vals.map(v=>`<option>${esc(v)}</option>`).join("");
    s.onchange=render; const l=document.createElement("label"); l.textContent=lab.replace("【质量】","质量·"); l.appendChild(s); bar.appendChild(l);});
  const l=document.createElement("label"); l.textContent="关键词搜索"; const inp=document.createElement("input"); inp.type="search"; inp.id="kw"; inp.placeholder="如 BES、glovebox、Sikeng";
  inp.oninput=render; l.appendChild(inp); bar.appendChild(l);
  const c=document.createElement("div"); c.className="count"; c.id="cnt"; bar.appendChild(c);
}
function render(){
  const d=D[cur], kw=(document.getElementById("kw").value||"").trim().toLowerCase();
  const sel=[...document.querySelectorAll("#bar select")].map(s=>[filters()[+s.dataset.i],s.value]).filter(x=>x[1]);
  const rows=d.rows.filter(r=>sel.every(([[,col,fn],v])=>fn(r[d.cols.indexOf(col)])===v)&&(!kw||r.join(" ").toLowerCase().includes(kw)));
  const long=new Set(["原文摘录（英文原句+页码）","各时间点测定指标","处理组列表及说明","文献核心问题","文献主要结论","质控（标准物质/回收率/检出限）","备注"]);
  const hl=s=>{let h=esc(s); if(kw){const i=h.toLowerCase().indexOf(kw); if(i>=0)h=h.slice(0,i)+"<mark>"+h.slice(i,i+kw.length)+"</mark>"+h.slice(i+kw.length)} return h};
  document.getElementById("tbl").innerHTML="<thead><tr>"+d.cols.map(c=>`<th>${esc(c)}</th>`).join("")+"</tr></thead><tbody>"+
    rows.map(r=>"<tr>"+r.map((v,i)=>`<td class="${cls(v)} ${long.has(d.cols[i])?"long":""}">${hl(v)}</td>`).join("")+"</tr>").join("")+"</tbody>";
  document.getElementById("cnt").textContent=`显示 ${rows.length} / ${d.rows.length} 行`;
}
document.querySelectorAll(".tab").forEach(b=>b.onclick=()=>{document.querySelectorAll(".tab").forEach(x=>x.classList.remove("on"));b.classList.add("on");cur=b.dataset.t;buildBar();render();});
buildBar(); render();
</script></body></html>"""

out = B / "数据库浏览.html"
out.write_text(HTML.replace("__DATA__", json.dumps(DATA, ensure_ascii=False)), encoding="utf-8")
print("已生成", out, f"{out.stat().st_size // 1024} KB")
