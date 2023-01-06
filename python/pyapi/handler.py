"""
Serves responses to GET requests, base file in '/' and status codes in their respective paths
(eg. '/200' or '/404')
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
from os import chdir

chdir("C:/Users/Arthur/Desktop/treinamento/python/pyapi")

class Handler(BaseHTTPRequestHandler):
    """
    Instance of class BaseHTTPRequestHandler, since the class itself cannot respond to requests and
    SimpleHTTPRequestHandler only serves files.
    """
    def do_GET(self):
        """Responds to GET requests"""
        match self.path:
            case "/":
                f = open("./index.html", 'r', encoding="utf-8")
                self.wfile.write(f)

            case "/200":
                self.send_response(200)
                self.send_header("Content-Type:", "text/plain; encoding: utf-8")
                self.end_headers()
                self.wfile.write(b'hello world')

server_address = ('', 8000)
httpd = HTTPServer(server_address, Handler)
httpd.serve_forever()
