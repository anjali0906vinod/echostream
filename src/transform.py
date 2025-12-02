import pandas as pd
import os

def clean_spotify_data(df):
    print("Starting TRANSFORM...")

    # 1. Remove duplicate rows
    df = df.drop_duplicates()

    # 2. Drop completely empty columns (if any)
    df = df.dropna(axis=1, how='all')

    # 3. Drop rows where ALL values are empty
    df = df.dropna(how='all')

    # 4. Standardize column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # 5. Save cleaned data
    cleaned_path = "data/cleaned/spotify_cleaned.csv"
    os.makedirs("data/cleaned", exist_ok=True)
    df.to_csv(cleaned_path, index=False)

    print("TRANSFORM complete → Saved spotify_cleaned.csv")
    return df

# To test this file alone
if __name__ == "__main__":
    from extract import extract_spotify_data
    df = extract_spotify_data()
    clean_spotify_data(df)
