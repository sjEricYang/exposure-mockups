"""
Simple Python HTTP server with option to override specific endpoints to
be proxies of external content through the requests library.  Intended
use case for this small script is for quick prototyping of specific
single page web applications where specific web resources hosted by
third parties are restricted by cross-origin policies which is a
standard security feature provided by web browsers which restricts
access of http URLs from a file:// url which is used for local
development

Run this script in the directory containing the static html and JS files
with the `proxy_map` configured with the needed resources.
"""

import argparse
import requests
from io import BytesIO
from http.server import SimpleHTTPRequestHandler
from http.server import test as serve


# default: accessing http://localhost:8000/example.txt will return the
# contents fetched from http://example.com.

proxy_map = {
    '/example.txt': 'http://example.com',
}


class ProxyHTTPRequestHandler(SimpleHTTPRequestHandler):
    """
    Same as simple HTTP request heandler for serving local files, but
    specific paths can be specified to be proxies for specific external
    content to get around cross-site origin restrictions.
    """

    def send_head(self):
        url = proxy_map.get(self.path)
        if url:
            r = requests.get(url)
            self.send_response(200)
            # override content-type to whatever needed.
            self.send_header("Content-type", 'text/plain')
            self.send_header("Content-Length", str(len(r.text)))
            self.end_headers()
            return BytesIO(r.text.encode('utf8'))
        else:
            return super(ProxyHTTPRequestHandler, self).send_head()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', '-b', default='', metavar='ADDRESS',
                        help='Specify alternate bind address '
                             '[default: all interfaces]')
    parser.add_argument('port', action='store',
                        default=8000, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8000]')
    args = parser.parse_args()
    handler_class = ProxyHTTPRequestHandler
    serve(HandlerClass=handler_class, port=args.port, bind=args.bind)
