FROM python:3.9.14-slim-bullseye
COPY . /searchengine

WORKDIR /searchengine

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl
RUN apt-get -y install python3-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python","app.py"]