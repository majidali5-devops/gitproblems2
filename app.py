from http.server import HTTPServer, BaseHTTPRequestHandler

class MyApp(emcommerce):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello from Python App!</h1>")

server = HTTPServer(("0.0.0.0", 9000), MyApp)

print("Server running on http://localhost:8080")
server.serve_forever()

