import http.server
import socket
import socketserver

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    pass

if __name__ == '__main__':
    hostname = socket.gethostname()
    try:
        local_ip = socket.gethostbyname(hostname)
    except Exception:
        local_ip = '127.0.0.1'

    print('Serving SamsungxUASSQL dashboard on:')
    print(f'  http://127.0.0.1:{PORT}/')
    print(f'  http://{local_ip}:{PORT}/')
    print('If you want to access from another device, use the IP address above and make sure all devices are on the same Wi-Fi.')

    with socketserver.TCPServer(('0.0.0.0', PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nServer stopped.')
