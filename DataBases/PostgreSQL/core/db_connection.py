import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("PG_PORT"))


def get_pg_connection() -> psycopg2.extensions.connection:
    """
    Establishes and returns connection to the PostgreSQL database.
    """

    try:
        conn = psycopg2.connect(
            host=os.getenv("PG_HOST"),
            database=os.getenv("PG_DB"),
            user=os.getenv("PG_USER"),
            password=os.getenv("PG_PASSWORD"),
            port=os.getenv("PG_PORT"),
        )
        return conn
    except psycopg2.Error as connection_error:
        print(f"Error in connecting to the PostgreSQL: {connection_error}")
        return None


def close_pg_connection(conn: psycopg2.extensions.connection) -> None:
    """
    Closes the connection to the PostgreSQL database.

    Args:
        conn (psycopg2.extensions.connection) : A connection object established to the PostgreSQL database.

    Returns:
        None
    """
    if conn:
        conn.close()
        # print("PostgreSQL connection closed.")
