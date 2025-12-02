import pandas as pd
import os

def extract_spotify_data():
    # path to your raw CSV
    raw_csv_path = "data/raw/spotify_song.csv"

    # read the CSV
    df = pd.read_csv(raw_csv_path)

    print("RAW extraction complete → Read spotify.csv successfully")

    return df

if __name__ == "__main__":
    extract_spotify_data()


