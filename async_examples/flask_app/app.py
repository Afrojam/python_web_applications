import requests
from flask import Flask, request

api_url = f'http://slow_api:8051/'

app = Flask(__name__)


@app.route('/')
def index():
    delay = float(request.args.get('delay') or 1)
    resp = requests.get(f'{api_url}?delay={delay}')
    return 'Hi there! ' + resp.text
