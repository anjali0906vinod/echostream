import pandas as pd
from sqlalchemy import create_engine
import os

# path to database file inside db folder
DB_PATH = "data/db/spotify.db"

# this creates the connection
engine = create_engine(f"sqlite:///{DB_PATH}")

# create a tiny sample table
df = pd.DataFrame({
    "song": ["Hello", "Blinding Lights", "Calm Down"],
    "artist": ["Adele", "The Weeknd", "Rema"],
    "streams": [120, 500, 300]
})

# write the table to the database
df.to_sql("test_table", engine, index=False, if_exists="replace")

print("Database created and test_table added successfully!")
