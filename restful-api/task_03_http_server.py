import http.server
import json
from urllib.parse import urlparse

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        response_code = 200
        response_data = "Hello, this is a simple API!"
        content_type = "text/plain"

        if path == "/":
            response_data = "Hello, this is a simple API!"
        elif path == "/data":
            response_data = json.dumps({"name": "John", "age": 30, "city": "New York"})
            content_type = "application/json"
        elif path == "/status":
            response_data = json.dumps({"status": "OK"})
            content_type = "application/json"
        else:
            response_code = 404
            response_data = json.dumps({"error": "Endpoint not found"})
            content_type = "application/json"


        self.send_response(response_code)

        # Send headers
        self.send_header("Content-type", content_type)
        self.end_headers()

        # Send response data
        self.wfile.write(response_data.encode())



def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd server on port 8000...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
