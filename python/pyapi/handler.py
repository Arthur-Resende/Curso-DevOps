from http.server import HTTPServer, BaseHTTPRequestHandler

class Handle_test(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type:", "text/plain; encoding: utf-8")
        self.end_headers()
        self.wfile()

server_address = ('', 8000)
httpd = HTTPServer(server_address, Handle_test)
httpd.serve_forever()
