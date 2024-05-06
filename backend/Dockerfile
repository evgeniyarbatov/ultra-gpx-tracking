FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

COPY ./src/* /app/
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 9090

CMD ["python", "server.py"]
