from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///data/db/spotify.db")

df = pd.read_sql("SELECT * FROM spotify_tracks LIMIT 5", engine)
print(df)
