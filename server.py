import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus


class BaseServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def do_GET(self):
        if self.path == '/status':
            response = {"status": "up and running!"}
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(response).encode('utf-8')))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        if self.path == '/estate':
            response = {"posted": "ok"}
            self._set_headers()
            self.wfile.write(json.dumps(response))


def run(server_class=HTTPServer, handler_class=BaseServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('HTTP server running on port %s'% port)
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()