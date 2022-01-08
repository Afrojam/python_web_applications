from starlette.responses import PlainTextResponse
from starlette.testclient import TestClient

async def asgi_app(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello, world!')
    await response(scope, receive, send)

if __name__ == "__main__":
    client = TestClient(asgi_app)
    resp = client.get("?/whatever=33")

    print(f"Object type: {type(resp)}")
    print(f"Response status: {resp.status_code}")
    print(f"Response content type: {resp.content}")
