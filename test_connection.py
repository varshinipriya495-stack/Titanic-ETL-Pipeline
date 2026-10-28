
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from config import DB_CONFIG


def test_mysql_connection():
    print("Connection test started!", flush=True)

    # Step 1: Create the database URL
    print("Step 1: Creating database URL", flush=True)

    connection_url = URL.create(
        drivername="mysql+mysqlconnector",
        username=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        port=3306,
        database=DB_CONFIG["database"]
    )

    # Step 2: Create the database engine
    print("Step 2: Creating database engine", flush=True)

    engine = create_engine(
        connection_url,
        connect_args={
            "connection_timeout": 5,
            "use_pure": True
        },
        echo=True
    )

    try:
        # Step 3: Connect to MySQL
        print("Step 3: Connecting to MySQL", flush=True)

        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT DATABASE(), VERSION()")
            )

            database_name, mysql_version = result.fetchone()

            print("\nMySQL connection successful!", flush=True)
            print(f"Database: {database_name}", flush=True)
            print(f"MySQL Version: {mysql_version}", flush=True)

    except Exception as error:
        print("\nMySQL connection failed.", flush=True)
        print(f"Error: {error}", flush=True)

    finally:
        engine.dispose()
        print("Connection test finished!", flush=True)


if __name__ == "__main__":
    test_mysql_connection()
