from http.server import BaseHTTPRequestHandler, HTTPServer
import re

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"Detected OS: {self.headers}".encode())

    def parse_user_agent(self, user_agent):
        if user_agent:
            return user_agent
        return 'No User-Agent'

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
