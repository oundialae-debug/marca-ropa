"""Descarga la documentación oficial de la AliExpress Open Platform (página con JavaScript)
usando un navegador sin pantalla. Guarda el texto de cada API y las respuestas JSON internas."""
import asyncio, json, os, re
from playwright.async_api import async_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
BASE = "https://openservice.aliexpress.com/doc/api.htm"
CATS = os.environ.get("CATS", "21038").split(",")  # 21038 = AE-Dropshipper

async def main():
    os.makedirs(OUT, exist_ok=True)
    captured = []
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1400, "height": 2000})
        async def on_resp(r):
            if "json" in (r.headers.get("content-type") or "") and "openservice" in r.url:
                try:
                    captured.append({"url": r.url, "body": await r.json()})
                except Exception:
                    pass
        pg.on("response", on_resp)
        index = {}
        for cid in CATS:
            await pg.goto(f"{BASE}#/api?cid={cid}", wait_until="networkidle", timeout=90000)
            await pg.wait_for_timeout(4000)
            txt = await pg.inner_text("body")
            open(f"{OUT}/categoria_{cid}.txt", "w").write(txt)
            methods = sorted(set(re.findall(r"(aliexpress\.[a-z0-9_.]+)", txt)))
            index[cid] = methods
            for m in methods:
                await pg.goto(f"{BASE}#/api?cid={cid}&path={m}&methodType=GET/POST", wait_until="networkidle", timeout=90000)
                await pg.wait_for_timeout(3000)
                open(f"{OUT}/{m}.txt", "w").write(await pg.inner_text("body"))
        json.dump(index, open(f"{OUT}/indice.json", "w"), indent=1)
        json.dump(captured, open(f"{OUT}/json_interno.json", "w"), ensure_ascii=False)
        await b.close()

asyncio.run(main())
