FROM ubuntu:18.04
FROM python:3.8
COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt


RUN mkdir /app
RUN mkdir /app/dcoker
RUN mkdir /app/pipeline

COPY docker /app/docker
COPY pipeline /app/pipeline


COPY pipeline/model /app/pipeline/model
COPY pipeline/predict /app/pipeline/predict
COPY pipeline/preprocessing /app/pipeline/preprocessing
COPY app.py /app/app.py

WORKDIR /app

CMD ["python", "app.py"]
