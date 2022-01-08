def wsgi_app(environ, start_response):
    response_headers = [
        ('Content-type', 'text/plain; charset=utf-8'),
    ]
    if environ['PATH_INFO'] == '/hello':
        status = '200 OK'
        text = 'Hello World'.encode('utf-8')
    elif environ['PATH_INFO'] == '/bye':
        text = 'Good Bye World'.encode('utf-8')
        status = '200 OK'
    else:
        text = 'Not found :('.encode('utf-8')
        status = '404 Not Found'
    start_response(status, response_headers)
    return [text]
