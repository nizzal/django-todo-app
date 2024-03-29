FROM python:3.8.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "todo_app.wsgi", "--bind", "0.0.0.0:8000"]
