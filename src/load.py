import pandas as pd
from sqlalchemy import create_engine
import os

def load_to_sqlite():
    print("Starting LOAD...")

    # Path to cleaned CSV
    cleaned_path = "data/cleaned/spotify_cleaned.csv"

    # Path to your SQLite database file
    db_path = "data/db/spotify.db"

    # Create SQLAlchemy engine for SQLite
    engine = create_engine(f"sqlite:///{db_path}")

    # Read cleaned data
    df = pd.read_csv(cleaned_path)

    # Load into SQLite table
    df.to_sql(
        "spotify_tracks",         # table name
        engine,
        index=False,
        if_exists="replace"       # replace table each run
    )

    print("LOAD complete → Data written to sqlite table 'spotify_tracks'")

# For standalone testing
if __name__ == "__main__":
    load_to_sqlite()
