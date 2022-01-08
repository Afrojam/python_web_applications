FROM python:3.9.5

RUN pip install fastapi uvicorn aiohttp

COPY app.py /app.py

CMD uvicorn app:app \
  --host 0.0.0.0 --port $PORT_APP