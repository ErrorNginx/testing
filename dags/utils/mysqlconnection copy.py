from sqlalchemy import create_engine

def get_mysql_connection():
    """
    Function to create a connection to MySQL using SQLAlchemy
    """
    # Update with your MySQL connection details
    host = '34.66.217.227'
    port = '3306'
    database = 'test'
    username = 'root'
    password = 'root'

    # Buat string koneksi
    database_url = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"

    engine = create_engine(database_url, echo=True)
    return engine
