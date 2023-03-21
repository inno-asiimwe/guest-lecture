FROM python:3.7

WORKDIR /app

RUN apt-get update && \
    apt-get install netcat -y

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

RUN chmod +x /app/scripts/start.sh

CMD ["/app/scripts/start.sh"]