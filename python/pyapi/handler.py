# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import json

db = {
    "name" : "",
    "tasks" : []
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type:", "text/plain; encoding: utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(db).encode('utf-8'))

    def do_POST(self):
        query = urlparse(self.path, "scheme://netloc/path;parameters?query#fragment").query
        query_items = dict(qc.split('=') for qc in query.split('&'))
        if "name" in query_items.keys():
            self.send_response(200)
            self.send_header("Content-Type:", "text/plain; encoding: utf-8")
            self.end_headers()
            self.wfile.write("Name changed successfully".encode('utf-8'))
            db["name"] = query_items["name"]
        
        else:
            self.send_response(404)
            self.send_header("Content-Type:", "text/plain; encoding: utf-8")
            self.end_headers()
            self.wfile.write("Variable \"name\" not defined".encode('utf-8'))

    def do_DELETE(self):
        print("delete request received")
    
    def do_PUT(self):
        print("put request received")

server_address = ('0.0.0.0', 8000)
httpd = HTTPServer(server_address, Handler)
httpd.serve_forever()
