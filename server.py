from http.server import BaseHTTPRequestHandler, HTTPServer


class HTTPRequestHandler(BaseHTTPRequestHandler):
    """Request handler class"""

    def do_GET(self):
        """Handler for GET requests."""

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header("Cache-Control", "no-cache")

        if self.path.endswith(".wasm"):
            # Header to serve .wasm file
            self.send_header("Content-Type", "application/wasm")
        else:
            self.send_header("Content-Type", "text/html")

        self.end_headers()

        # Serve the file contents
        urlpath = self.path
        if urlpath == "/":
            urlpath = "/index.html"

        with open(f".{urlpath}", "rb") as f:
            content = f.read()

        self.wfile.write(content)


def main():
    print("starting server...")

    # Server settings
    server_address = ("localhost", 8080)
    httpd = HTTPServer(server_address, HTTPRequestHandler)

    print("running server...")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
