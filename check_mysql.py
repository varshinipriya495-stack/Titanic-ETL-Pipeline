
import mysql.connector
from config import DB_CONFIG

print("Step 1: Starting test", flush=True)

try:
    print("Step 2: Connecting with timeout", flush=True)

    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"],
        connection_timeout=5,
        use_pure=True
    )

    print("Step 3: Connected successfully!", flush=True)
    print("Database:", connection.database, flush=True)
    connection.close()

except Exception as error:
    print("Connection failed:", repr(error), flush=True)
