from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import mimetypes

ROOT = Path(__file__).resolve().parent
TEMPLATES_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"

ROUTES = {
    "/": "index.html",
    "/about": "about.html",
    "/myresearch": "myresearch.html",
}


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/static/"):
            self.serve_static()
            return

        template_name = ROUTES.get(self.path)
        if template_name:
            self.send_html(template_name)
            return

        self.send_response(404)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"404 Not Found")

    def send_html(self, filename):
        file_path = TEMPLATES_DIR / filename
        if not file_path.exists():
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"404 Not Found")
            return

        content = file_path.read_text(encoding="utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

    def serve_static(self):
        rel_path = self.path.lstrip("/")
        file_path = STATIC_DIR / rel_path.replace("static/", "", 1)
        if file_path.exists() and file_path.is_file():
            content = file_path.read_bytes()
            mime_type, _ = mimetypes.guess_type(str(file_path))
            if mime_type is None:
                mime_type = "application/octet-stream"
            self.send_response(200)
            self.send_header("Content-Type", mime_type)
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    port = 8000
    server = ThreadingHTTPServer(("127.0.0.1", port), AppHandler)
    print(f"Server running at http://127.0.0.1:{port}")
    server.serve_forever()
