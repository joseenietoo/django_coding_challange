FROM python:3.8

RUN mkdir -p /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

WORKDIR /app

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]



