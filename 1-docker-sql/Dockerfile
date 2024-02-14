FROM python:3.9

RUN apt-get install wget
RUN pip install pandas psycopg2 sqlalchemy

WORKDIR /app
COPY ingest-data.py /app 

ENTRYPOINT [ "python", "ingest-data.py"]

