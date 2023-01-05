"""
Script recebe requests no endereço localhost:8080 e retorna resposas em API
"""
from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello World')
        if self.path == "/teste":
            self.wfile.write(b'Hello teste')

httpd = HTTPServer(('', 8080), HelloWorldHandler)
httpd.serve_forever()
