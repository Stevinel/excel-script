import os

import psycopg2

import upload
from config import HOST, USER, PASSWORD, DATABASE

connection = None

def init_db():
    try:
        global connection
        connection = psycopg2.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        connection.autocommit = True
        cursor = connection.cursor()

        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")

            print(f"Server version: {cursor.fetchone()}")

        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS endpoint_names (\
                    id serial PRIMARY KEY,\
                    endpoint_id INT,\
                    endpoint_names  VARCHAR(100) NOT NULL);"
            )
            connection.commit()
            print("[INFO] Table created successfully")

        with connection.cursor() as cursor:
            endpoint_id, endpoint_names = upload.get_new_data()
            x = dict(zip(endpoint_id, endpoint_names))
            for endpoint_id, endpoint_names in x.items():
                cursor.execute(
                    "INSERT INTO endpoint_names\
                        (endpoint_id, endpoint_names) VALUES\
                        (%s, %s) ",
                        (endpoint_id, endpoint_names)
                )
                cursor.execute(
                    """CREATE TABLE query AS SELECT * FROM endpoint_names\
                        GROUP BY id, endpoint_id HAVING id IN (SELECT MAX(id)\
                        FROM endpoint_names GROUP BY endpoint_id)"""
                )
                cursor.execute(
                    "DELETE FROM endpoint_names\
                        WHERE (id) NOT IN (SELECT id FROM query)"
                )
                cursor.execute("DROP TABLE IF EXISTS query")
                connection.commit()
            input("Вы успешно перенесли новый данные в БД, нажмите Enter "
            "для завершения")
            print("[INFO] Data was succefully inserted")

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")
