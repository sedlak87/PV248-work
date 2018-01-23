from http.server import HTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

import time

HOST_NAME = 'localhost'
PORT = 8000


class server(BaseHTTPRequestHandler):
    def getJson(self, queries):
        return json.dumps(queries)
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        query = urlparse(self.path).query
        queries = parse_qs(query)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Http server</title></head>".encode())
        if "f" in queries.keys() and "json" in queries["f"]:
            self.wfile.write("<body><p>{}</p></body></html>".format(self.getJson(queries)).encode())
        else:
            for (k, v) in queries.items():
                self.wfile.write("<body><p>You entered query: {} with value {}</p></body></html>".format(k, v).encode())


server_class = HTTPServer
httpd = server_class((HOST_NAME, PORT), server)
print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT))
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT))