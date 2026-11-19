import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


def build_response(path):
    if path == "/health":
        return 200, {"status": "ok"}
    if path == "/version":
        return 200, {"version": os.getenv("APP_VERSION", "dev")}
    return 404, {"error": "not found"}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status, body = build_response(self.path)
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()