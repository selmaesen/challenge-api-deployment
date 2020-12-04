FROM python
COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt


RUN mkdir /app
RUN mkdir /app/dcoker
RUN mkdir /app/pipeline

COPY docker /app/docker
COPY pipeline /app/pipeline


COPY pipeline/model /app/pipeline/model
COPY pipeline/model/data /app/pipeline/model/data

WORKDIR /app

CMD ["python","pipeline/model/house_price.py"]