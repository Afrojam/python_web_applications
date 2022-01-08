def wsgi_app(environ, start_response):
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain; charset=utf-8'),
    ]
    start_response(status, response_headers)
    text = 'Hello World'.encode('utf-8')
    return [text]


def log_environ(app_handler):
    from pprint import pprint

    def _print_environ_and_response_in_alternate_caps(environ, start_response):
        pprint(environ)  # pre-process
        resp = app_handler(environ, start_response)
        resp = [resp[0].swapcase()]  # post-process
        return resp

    return _print_environ_and_response_in_alternate_caps


app = log_environ(wsgi_app)
