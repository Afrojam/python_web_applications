def not_found(environ, start_response):
    start_response('404 Not Found', [('Content-Type', 'text/plain')])
    return ['404 Not Found'.encode('utf-8')]


def hello_world(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ["Hello World!".encode('utf-8')]


def good_bye_world(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ["Good Bye World!".encode('utf-8')]


URLS = {
    "/hello": hello_world,
    "/bye": good_bye_world,
}


def wsgi_app(environ, start_response):
    handler = URLS.get(environ.get('PATH_INFO')) or not_found
    return handler(environ, start_response)
