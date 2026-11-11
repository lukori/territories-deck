# Local server for presenting the deck: serves this folder as UTF-8 on http://localhost:8780
# (localhost counts as secure, so the "עוד פעם" voice trigger can use the microphone).
#   python3 serve.py   →  http://localhost:8780/  (lecturers)   ·   http://localhost:8780/class.html  (classroom)
import http.server, functools, os
root = os.path.dirname(os.path.abspath(__file__))
H = http.server.SimpleHTTPRequestHandler
H.extensions_map.update({'.html': 'text/html; charset=utf-8', '.svg': 'image/svg+xml; charset=utf-8'})
http.server.ThreadingHTTPServer(('', 8780), functools.partial(H, directory=root)).serve_forever()
