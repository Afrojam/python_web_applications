from wsgiref.simple_server import make_server


def wsgi_app(environ, start_response):
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain; charset=utf-8'),
    ]
    start_response(status, response_headers)
    text = 'Hello World'.encode('utf-8')
    # print(environ)
    return [text]


if __name__ == "__main__":
    httpd = make_server("127.0.0.1", 8051, wsgi_app)
    httpd.serve_forever()
