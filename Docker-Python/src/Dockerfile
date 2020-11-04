FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN mkdir /data

ENTRYPOINT ["python","./app.py"]


