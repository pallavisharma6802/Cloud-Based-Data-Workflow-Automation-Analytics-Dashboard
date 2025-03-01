import sqlite3
import pandas as pd

# Connect to SQLite (local DB)
conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()

# Initialize table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS analytics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        value REAL
    )
""")
conn.commit()

def save_to_db(df):
    """Save dataframe into the SQLite database."""
    if df is not None:
        df.to_sql("analytics", conn, if_exists="replace", index=False)

def fetch_data_from_db():
    """Retrieve data from the SQLite database."""
    return pd.read_sql("SELECT * FROM analytics", conn)

def execute_custom_query(query):
    """Run any user-provided SQL query."""
    try:
        result = pd.read_sql(query, conn)
        return result
    except Exception as e:
        return f"Query Error: {e}"

def close_connection():
    """Close SQLite connection."""
    conn.close()
