import pandas as pd
import argparse
import os

from time import time
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    # download the csv
    csv_name = "output.csv"
    os.system(f"wget {url} -O - | gunzip -c > {csv_name}")

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    engine.connect()

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100_000)

    df = next(df_iter)
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

    df.to_sql(name=table_name, con=engine, if_exists="replace")
    print("Created table and instered chunk 1")

    for i, df in enumerate(df_iter, 2):
        t_start = time()
        df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
        df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
        df.to_sql(name=table_name, con=engine, if_exists="append")

        t_end = time()

        print(f"inserted chunk {i}, took {t_end-t_start:.3f} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ingest-data", description="Ingest CSV data to Postgres")
    parser.add_argument("user", help="username for postgres")
    parser.add_argument("password", help="password for postgres")
    parser.add_argument("host", help="host for postgres")
    parser.add_argument("port", help="port for postgres", type=int)
    parser.add_argument("db", help="database name in postgres")
    parser.add_argument("table_name", help="name of table where results are written to")
    parser.add_argument("url", help="url of the csv file")

    args = parser.parse_args()

    main(args)