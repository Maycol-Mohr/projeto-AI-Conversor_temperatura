from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        print(">>> OPTIONS ejecutado correctamente <<<")
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(length))

        celsius = float(data["celsius"])
        fahrenheit = (celsius * 9/5) + 32

        respuesta = {"fahrenheit": round(fahrenheit, 2)}
        resp_bytes = json.dumps(respuesta).encode()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(resp_bytes)

print("Servidor Python corriendo en http://localhost:8000")
HTTPServer(("localhost", 8000), Handler).serve_forever()