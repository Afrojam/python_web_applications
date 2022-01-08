from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.api_route("/hello")
async def hello_world():
    return "Hello World"

@app.api_route("/bye")
async def bye_world():
    return "Bye World!"


@app.exception_handler(404)
def page_not_found(request: Request, exc: Exception):
    return RedirectResponse("/hello", 404, {"Refresh": "1; url=/hello"})
