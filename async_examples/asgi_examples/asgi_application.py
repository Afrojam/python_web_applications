# async_examples/asgi_examples/asgi_application.py


async def asgi_app(scope, receive, send):
    status = 200
    response_headers = [
        ('Content-type', 'text/plain; charset=utf-8'),
    ]
    text = 'Hello World'.encode('utf-8')
    print(scope)
    await send({"type": "http.response.start", "status": status, "headers": response_headers})
    await send({"type": "http.response.body", "body": text})
