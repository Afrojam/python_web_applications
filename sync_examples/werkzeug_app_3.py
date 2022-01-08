import werkzeug

@werkzeug.Request.application
def wsgi_app(request):
    msg = f"A WSGI app with: \n method: {request.method}\n path: {request.path}\n query: {request.query_string}\n"
    return werkzeug.Response(msg)


if __name__ == "__main__":
    client = werkzeug.Client(wsgi_app, response_wrapper=werkzeug.Response)
    resp = client.get("?/whatever=33")
    print(f"Data: {resp.data.decode()}")
