from sqlalchemy import create_engine
import pandas as pd

DB_PATH = "data/db/spotify.db"
engine = create_engine(f"sqlite:///{DB_PATH}")

# query the database
query = "SELECT * FROM test_table"

df = pd.read_sql(query, engine)

print(df)
