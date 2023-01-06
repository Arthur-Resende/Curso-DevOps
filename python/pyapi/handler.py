# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import json

db = {
    "name" : "",
    "tasks" : []
}

class Handler(BaseHTTPRequestHandler):
    # makes a response with status code, and a plain text message made in order to not repeat code
    def custom_response(self, status: int, message: str):
        self.send_response(status)
        self.send_header("Content-Type:", "text/plain; encoding: utf-8")
        self.end_headers()
        self.wfile.write(message)

    # Verifies, gets and returns query parameters
    def get_query(self, path: str):
        try:
            query = urlparse(self.path, "scheme://netloc/path;parameters?query#fragment").query
            return dict(qc.split('=') for qc in query.split('&'))      
        except Exception:
            self.custom_response(400, "No parameters sent".encode('utf-8'))

    def do_GET(self):
        self.custom_response(200, json.dumps(db).encode('utf-8'))

    def do_POST(self):
        query_items = self.get_query(self.path)
        if "name" in query_items.keys():
            try:
                db["name"] = query_items["name"]
                self.custom_response(201, "Name changed successfully".encode('utf-8'))
            except Exception:
                self.send_response(500)
                self.end_headers()

        else:
            self.custom_response(404, "Variable \"name\" not defined".encode('utf-8'))

    # DELETE request handler, to be implemented
    def do_DELETE(self):
        print('delete request received')

    def do_PUT(self):
        query_items = self.get_query(self.path)
        if "tasks" in query_items.keys():
            try:
                db["tasks"].extend(query_items["tasks"].split('+'))
                self.custom_response(201, "Tasks created successfully".encode('utf-8'))
            except Exception:
                self.send_response(500)
                self.end_headers()

        else:
            self.custom_response(404, "Variable \"tasks\" not defined".encode('utf-8'))

server_address = ('0.0.0.0', 8000)
httpd = HTTPServer(server_address, Handler)
httpd.serve_forever()
