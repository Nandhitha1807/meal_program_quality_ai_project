import pandas as pd
from src.db_connection import get_connection

def load_data_from_db():
    conn = get_connection()
    query = "SELECT * FROM meal_data"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
