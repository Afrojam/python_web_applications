import werkzeug


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
    client = werkzeug.Client(wsgi_app, response_wrapper=werkzeug.Response)
    resp = client.get("?/whatever=33")
    print(f"Object type: {type(resp)}")
    print(f"Response status: {resp.status}")
    print(f"Response content type: {resp.content_type}")
