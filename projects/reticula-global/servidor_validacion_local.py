"""Servidor local estático con proxy de solo lectura a la API pública."""

from __future__ import annotations

import argparse
import functools
import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


PUBLIC_API = "https://support.jumalenin.com/api/reticula/v1/datos.php"
LOCAL_API_PATH = "/__reticula_api__/datos.php"
SUPPORT_ROOT = Path(__file__).resolve().parents[2]


class ValidationHandler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        request_url = urlsplit(self.path)
        if request_url.path != LOCAL_API_PATH:
            super().do_GET()
            return

        upstream_url = PUBLIC_API
        if request_url.query:
            upstream_url = f"{upstream_url}?{request_url.query}"

        request = Request(
            upstream_url,
            headers={"Accept": "application/json", "User-Agent": "ReticulaGlobalLocalValidation/1.0"},
        )
        try:
            with urlopen(request, timeout=15) as response:
                body = response.read()
                self.send_response(response.status)
                self.send_header("Content-Type", response.headers.get("Content-Type", "application/json"))
                self.send_header("Cache-Control", "no-store")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
        except HTTPError as error:
            body = error.read()
            self.send_response(error.code)
            self.send_header("Content-Type", error.headers.get("Content-Type", "application/json"))
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except URLError:
            body = json.dumps(
                {"ok": False, "errors": [{"code": "LOCAL_PROXY_ERROR", "message": "No se pudo consultar la API pública."}]},
                ensure_ascii=False,
            ).encode("utf-8")
            self.send_response(502)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)


def main() -> None:
    parser = argparse.ArgumentParser(description="Servidor de validación local de Retícula Global")
    parser.add_argument("--port", type=int, default=8088)
    arguments = parser.parse_args()
    handler = functools.partial(ValidationHandler, directory=str(SUPPORT_ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", arguments.port), handler)
    print(f"Retícula Global: http://127.0.0.1:{arguments.port}/projects/mapa-mundi/")
    print(f"Proxy API pública: {PUBLIC_API}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
