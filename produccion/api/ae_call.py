"""Llama a la API oficial de AliExpress (Open Platform) desde GitHub Actions.
Lee produccion/api/peticion.json y escribe produccion/api/resultado.json.
El token de acceso se guarda cifrado (con la App Secret) en produccion/api/token.enc."""
import hmac, hashlib, time, json, os, subprocess, urllib.parse, urllib.request

KEY = os.environ["AE_APP_KEY"]
SECRET = os.environ["AE_APP_SECRET"]
BASE = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE = os.path.join(BASE, "token.enc")

def sign(params, path=""):
    s = path + "".join(k + str(params[k]) for k in sorted(params))
    return hmac.new(SECRET.encode(), s.encode(), hashlib.sha256).hexdigest().upper()

def call(method=None, path=None, params=None, use_token=True):
    p = {"app_key": KEY, "timestamp": str(int(time.time() * 1000)), "sign_method": "sha256"}
    if method:
        p["method"] = method
    if use_token and os.path.exists(TOKEN_FILE):
        p["access_token"] = load_token()["access_token"]
    p.update({k: str(v) for k, v in (params or {}).items()})
    p["sign"] = sign(p, path or "")
    url = "https://api-sg.aliexpress.com/" + ("rest" + path if path else "sync")
    req = urllib.request.Request(url, data=urllib.parse.urlencode(p).encode(),
                                 headers={"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())

def openssl(args, data):
    return subprocess.run(["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-a", "-A", *args, "-pass", "env:AE_APP_SECRET"],
                          input=data, capture_output=True, check=True).stdout

def save_token(tok):
    with open(TOKEN_FILE, "wb") as f:
        f.write(openssl([], json.dumps(tok).encode()))

def load_token():
    return json.loads(openssl(["-d"], open(TOKEN_FILE, "rb").read()))

def refresh_if_needed():
    if not os.path.exists(TOKEN_FILE):
        return
    t = load_token()
    if int(t.get("expire_time", 0)) - time.time() * 1000 < 6 * 3600 * 1000 and t.get("refresh_token"):
        r = call(path="/auth/token/refresh", params={"refresh_token": t["refresh_token"]}, use_token=False)
        if "access_token" in r:
            save_token(r)

def main():
    refresh_if_needed()
    req = json.load(open(os.path.join(BASE, "peticion.json")))
    out = {"pedido": req.get("id"), "fecha": time.strftime("%Y-%m-%d %H:%M:%S"), "respuestas": []}
    for c in req["llamadas"]:
        time.sleep(0.6)  # evita ApiCallLimit
        try:
            if c.get("tipo") == "token":  # canjear el código de autorización
                r = call(path="/auth/token/create", params={"code": c["code"]}, use_token=False)
                if "access_token" in r:
                    save_token(r)
                    r = {"ok": True, "cuenta": r.get("account"), "caduca_ms": r.get("expire_time")}
            else:
                params = dict(c.get("params") or {})
                if c.get("image_url"):  # búsqueda por imagen: el runner descarga la foto y la pasa en base64
                    import base64
                    img = urllib.request.urlopen(urllib.request.Request(c["image_url"], headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36", "Referer": "https://www.aliexpress.com/"}), timeout=60).read()
                    p0 = dict(params.get("param0") or {})
                    p0["image_base64"] = base64.b64encode(img).decode()
                    params["param0"] = json.dumps(p0)
                elif isinstance(params.get("param0"), dict):
                    params["param0"] = json.dumps(params["param0"])
                r = call(method=c["method"], params=params, use_token=c.get("token", True))
        except Exception as e:
            r = {"error": repr(e)}
        out["respuestas"].append({"llamada": {k: v for k, v in c.items() if k != "code"}, "respuesta": r})
    json.dump(out, open(os.path.join(BASE, "resultado.json"), "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
