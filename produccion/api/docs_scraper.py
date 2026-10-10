"""Descarga la documentación oficial de la AliExpress Open Platform (sección AE-Dropshipper)
desde el servicio JSON que usa su web. Guarda cada API en docs/<método>.json y un resumen legible."""
import asyncio, json, os
from playwright.async_api import async_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
CID = os.environ.get("CATS", "21038").split(",")[0]
H = "https://openservice.aliexpress.com/handler/share/apidoc/"

async def main():
    os.makedirs(OUT, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        await pg.goto(f"https://openservice.aliexpress.com/doc/api.htm#/api?cid={CID}", wait_until="networkidle", timeout=90000)
        cats = await (await pg.request.get(H + "getApiCategoryMixed.json?oeid=AE_DOC&lang=en_US")).json()
        cat = [c for c in cats["data"] if str(c["id"]) == CID][0]
        resumen = [f"# {cat['name']} (cid {CID})\n"]
        for a in cat["apiList"]:
            path = a.get("path") or a.get("apiName")
            r = await pg.request.get(H + "getApi.json", params={"cid": CID, "path": path, "methodType": "GET/POST", "oeid": "AE_DOC", "lang": "en_US"})
            d = (await r.json()).get("data", {})
            json.dump(d, open(f"{OUT}/{path}.json", "w"), ensure_ascii=False, indent=1)
            resumen.append(f"\n## {path} — {d.get('title') or a.get('title')}\n{d.get('description') or a.get('description') or ''}\n")
            def rows(lst, depth=0):
                for x in lst or []:
                    resumen.append(f"{'  '*depth}- `{x.get('name')}` ({x.get('type')}{', obligatorio' if str(x.get('required')).lower() in ('true','1','yes') else ''}): {(x.get('description') or '').strip()}")
                    rows(x.get("children") or x.get("subParams"), depth + 1)
            resumen.append("**Parámetros:**"); rows(d.get("requestParams") or d.get("params"))
            resumen.append("**Respuesta:**"); rows(d.get("responseParams"))
        open(f"{OUT}/RESUMEN_dropshipper.md", "w").write("\n".join(resumen))
        await b.close()

asyncio.run(main())
