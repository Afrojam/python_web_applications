FROM python:3.9.5

RUN pip install aiohttp

COPY slow_api.py /slow_api.py

CMD ["python", "/slow_api.py"]