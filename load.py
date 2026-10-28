
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from config import DB_CONFIG


def load_data(df, table_name="passengers", if_exists="replace"):
    print("Loading data into MySQL...", flush=True)

    connection_url = URL.create(
        drivername="mysql+mysqlconnector",
        username=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        port=3306,
        database=DB_CONFIG["database"]
    )

    engine = create_engine(
        connection_url,
        connect_args={
            "connection_timeout": 5,
            "use_pure": True
        }
    )

    try:
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists=if_exists,
            index=False
        )

        print("Data loaded successfully!")
        print("Rows loaded:", len(df))
        print("Table name:", table_name)
        print("Load mode:", if_exists)

    except Exception as error:
        print("Data loading failed:", error)
        raise

    finally:
        engine.dispose()
