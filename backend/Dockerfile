FROM --platform=linux/amd64 ubuntu:latest

RUN apt-get update
RUN apt-get install python3 python3-pip libpq-dev netcat-traditional -y

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9090

CMD ["python3", "src/server.py"]
