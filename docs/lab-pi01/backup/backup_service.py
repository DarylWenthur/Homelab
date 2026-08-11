from http.server import BaseHTTPRequestHandler, HTTPServer
import json

STATUS_FILE = "/srv/homepage/config/backup-status.txt"

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.serve_html()
        elif self.path == "/api":
            self.serve_api()
        else:
            self.send_response(404)
            self.end_headers()

    def serve_api(self):
        import time

        try:
            with open(STATUS_FILE, "r") as f:
                lines = f.read().splitlines()

            status = lines[0]
            time_str = lines[1] if len(lines) > 1 else ""
            timestamp = int(lines[2]) if len(lines) > 2 else 0

            now = int(time.time())
            age = now - timestamp

            if status == "SUCCESS":
                if timestamp == 0:
                    display_status = "🟢  SUCCESS"
                elif age > 691200:
                    display_status = "🟡  STALE"
                else:
                    display_status = "🟢  SUCCESS"
            else:
                display_status = "🔴  FAILED"

        except Exception:
            display_status = "🔴  UNKNOWN"
            time_str = ""

        data = {
            "status": display_status,
            "time": time_str
        }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def serve_html(self):
        html = """
<html>
<head>
<meta http-equiv="refresh" content="10">
<style>
body {
    font-family: sans-serif;
    background: black;
    color: white;
    text-align: center;
    margin-top: 40px;
}
.status { font-size: 26px; }
.time { font-size: 14px; opacity: 0.7; }
</style>
</head>
<body>

<div id="status">Loading...</div>

<script>
fetch("/api")
  .then(res => res.json())
  .then(data => {
    document.getElementById("status").innerHTML = `
      <div class="status">${data.status}</div>
      <div class="time">${data.time}</div>
    `;
  });
</script>

</body>
</html>
"""

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

server = HTTPServer(("0.0.0.0", 5055), Handler)
server.serve_forever()
