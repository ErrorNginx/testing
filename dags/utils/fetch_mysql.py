import pandas as pd
from sqlalchemy import create_engine
from utils.mysqlconnection import get_mysql_connection
import os

sql_file_path = os.path.join(os.path.dirname(__file__), 'query_all.sql') 

def fetch_data_task(output_file):
    engine = get_mysql_connection()

    try:
        with open(sql_file_path, "r") as file:
            sql_queries = file.read()

        # Split SQL queries by semicolon
        sql_queries_list = sql_queries.split(';')

        # Execute only the first query
        sql_query = sql_queries_list[0]

        with engine.connect() as connection:
            result = connection.execute(sql_query)
            records = result.fetchall()
            column_names = result.keys()
            df = pd.DataFrame(records, columns=column_names)

            if os.path.exists(output_file):
                raise FileExistsError("File already exists.")
            df.to_csv(output_file, index=False, header=True)

    except FileExistsError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        engine.dispose()

    return output_file

if __name__ == '__main__':
    fetch_data_task()
