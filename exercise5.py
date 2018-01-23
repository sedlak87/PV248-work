from http.server import HTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlparse

import time

HOST_NAME = 'localhost'
PORT_NUMBER = 8000

class server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        query = urlparse(self.path).query
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Http server v pythone</title></head>".encode())
        self.wfile.write("<body><p>You entered query: {}</p></body></html>".format(query).encode())

server_class = HTTPServer
httpd = server_class((HOST_NAME, PORT_NUMBER), server)
print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))

