FROM python:3.9

RUN pip install pandas

WORKDIR /app
COPY pipeline.py /app 

ENTRYPOINT [ "python", "pipeline.py"]

# docker run -it \
#     -e POSTGRES_USER="root" \
#     -e POSTGRES_PASSWORD="root" \
#     -e POSTGRES_DB="ny_taxi" \
#     -v /home/george/de-zc/1-docker-sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
#     -p 5455:5432 \
#     --network=pg-network \
#     --name pg-database \
#     postgres:13

# docker run -t \
#     -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
#     -e PGADMIN_DEFAULT_PASSWORD="root" \
#     -p 8080:80 \
#     --network=pg-network \
#     --name pg-admin \
#     dpage/pgadmin4