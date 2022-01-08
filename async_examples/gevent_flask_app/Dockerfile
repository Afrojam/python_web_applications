FROM python:3.9.5

RUN pip install Flask requests gevent

COPY app.py /app.py

ENV FLASK_APP=app

CMD python app.py
#CMD flask run --no-reload \
#  --$THREADS-threads \
#  --host 0.0.0.0 --port $PORT_APP