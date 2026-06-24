"""
Servidor HTTP estático — Proximidades do Assaí.

Local:
    python server.py

Railway / Docker:
    PORT é definido automaticamente pelo ambiente.
"""
import http.server
import os
import socketserver

PORT = int(os.environ.get('PORT', '8000'))
HOST = os.environ.get('HOST', '0.0.0.0')

MIME_EXTRA = {
    '.geojson': 'application/geo+json',
    '.json': 'application/json',
    '.svg': 'image/svg+xml',
}


class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def guess_type(self, path):
        ext = os.path.splitext(path)[1].lower()
        if ext in MIME_EXTRA:
            return MIME_EXTRA[ext]
        return super().guess_type(path)

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, fmt, *args):
        print(f'  {self.address_string()} [{self.log_date_time_string()}] {fmt % args}')


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)

    print('=' * 52)
    print('  Assaí — Análise de Proximidades')
    print('=' * 52)
    print(f'  Servidor: http://{HOST}:{PORT}')
    print('  Pressione Ctrl+C para encerrar.')
    print('=' * 52)

    with socketserver.TCPServer((HOST, PORT), CORSHandler) as httpd:
        httpd.allow_reuse_address = True
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\n  Servidor encerrado.')


if __name__ == '__main__':
    main()
