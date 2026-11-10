from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class ShopNowRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            health_payload = {"status": "healthy"}
            self.wfile.write(json.dumps(health_payload).encode())
            return

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        default_payload = {
            "message": "Request processed successfully!",
            "server": self.server.server_name
        }

        self.wfile.write(json.dumps(default_payload).encode())


def start_server(port):
    http_server = HTTPServer(("0.0.0.0", port), ShopNowRequestHandler)
    http_server.server_name = f"Server on port {port}"

    print(f"The ShopNow server is running on port {port}")

    http_server.serve_forever()
    
