# BEFORE RUNNING: Install psycopg2 by entering "pip install psycopg2" in the terminal.
import psycopg2
from psycopg2 import OperationalError

# create_connection: Establishes a connection with a PostgreSQL database
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL database successful.")
    except OperationalError as e: print(f"Connection Error: '{e}'")
    return connection

# query: Executes a given query to a given database.
def query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query successful.")
    except OperationalError as e: print(f"Query Error: '{e}'")

# queryFetch: A query variant that returns fetchable data (i.e. from SELECT)
def queryFetch(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query successful.")
    except OperationalError as e: print(f"Query Error: '{e}'")
    return cursor.fetchall()