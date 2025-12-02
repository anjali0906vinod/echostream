import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# --------------------------
# PAGE CONFIG (GREEN THEME + WIDE LAYOUT)
# --------------------------
st.set_page_config(
    page_title="EchoStream Dashboard",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------
# DATABASE CONFIG
# --------------------------
DB_PATH = "D:/echostream/data/db/spotify.db"
engine = create_engine(f"sqlite:///{DB_PATH}")

# --------------------------
# LOAD DATA
# --------------------------
@st.cache_data
def load_data():
    df = pd.read_sql("SELECT * FROM spotify_tracks", engine)

    # Rename columns from your dataset
    rename_map = {
        "track_artist": "artists",
        "track_popularity": "popularity",
        "playlist_genre": "genre",
        "playlist_subgenre": "sub_genre"
    }
    df = df.rename(columns=rename_map)

    # Fill missing genre if needed
    if "genre" not in df.columns or df["genre"].dropna().empty:
        df["genre"] = "Unknown"

    return df

df = load_data()

# ----------------------------------------
# HEADER
# ----------------------------------------
st.title("🎵 EchoStream — Spotify Analytics Dashboard")
st.markdown("EchoStream is an end-to-end data engineering project designed around Spotify music data.✨")

# ----------------------------------------
# KPIs (Green Boxes)
# ----------------------------------------
total_tracks = len(df)
unique_artists = df["artists"].nunique()
unique_genres = df["genre"].nunique()

c1, c2, c3 = st.columns(3)

c1.metric("Total Tracks", f"{total_tracks:,}")
c2.metric("Unique Artists", f"{unique_artists:,}")
c3.metric("Genres", f"{unique_genres:,}")

# ----------------------------------------
# SIDEBAR FILTERS
# ----------------------------------------
st.sidebar.header("🎚️ Filters")

# Genre filter
genres = sorted(df["genre"].dropna().unique())
selected_genre = st.sidebar.selectbox("Select Genre", ["All"] + genres)

filtered = df.copy()
if selected_genre != "All":
    filtered = filtered[filtered["genre"] == selected_genre]

# Artist filter
artists = sorted(df["artists"].dropna().unique())[:100]  # keep menu short
selected_artist = st.sidebar.selectbox("Select Artist", ["All"] + artists)

if selected_artist != "All":
    filtered = filtered[filtered["artists"] == selected_artist]

# ----------------------------------------
# FILTERED TABLE
# ----------------------------------------
st.subheader(f"Filtered Songs ({len(filtered):,})")
cols_to_show = [c for c in ["track_name", "artists", "genre", "sub_genre", "popularity"] if c in filtered.columns]
st.dataframe(filtered[cols_to_show].sort_values(by="popularity", ascending=False))

# ----------------------------------------
# CHARTS SECTION
# ----------------------------------------
st.markdown("### 🎤 Popularity & Audio Features")

left, right = st.columns(2)

# TOP 10 POPULARITY
with left:
    st.subheader("Top 10 Popular Songs")
    top10 = df.nlargest(10, "popularity")
    st.bar_chart(top10.set_index("track_name")["popularity"])

# ENERGY vs DANCEABILITY
with right:
    st.subheader("Energy vs Danceability Scatter")
    scatter_df = df[["energy", "danceability"]].dropna()
    st.scatter_chart(scatter_df)


st.markdown("""
<style>
    .stMetric {
        background-color: #e6f4e6 !important;
        padding: 15px !important;
        border-radius: 12px !important;
        color: #0f5132 !important;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------
# GENRE POPULARITY
# ----------------------------------------
st.markdown("### 🎧 Genre Popularity (Average Popularity by Genre)")

if "genre" in df.columns and "popularity" in df.columns:
    genre_pop = (
        df.groupby("genre")["popularity"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        genre_pop,
        x="genre",
        y="popularity",
        title="Average Popularity by Genre",
        color="popularity",
        color_continuous_scale="greens"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Genre or popularity column missing.")

# ----------------------------------------
# AUDIO FEATURES PER GENRE
# ----------------------------------------
st.markdown("### 🎼 Audio Features by Genre")

features = ["danceability", "energy", "valence"]

if all(f in df.columns for f in features):
    feature_df = df.groupby("genre")[features].mean().reset_index()

    fig = px.bar(
        feature_df,
        x="genre",
        y=features,
        barmode="group",
        title="Average Audio Features by Genre",
        color_discrete_sequence=px.colors.qualitative.Prism
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Required audio feature columns missing.")

# ----------------------------------------
# CORRELATION HEATMAP
# ----------------------------------------
st.markdown("### 🧠 Audio Feature Correlation Heatmap")

# only numeric columns used for correlation
num_cols = ["danceability", "energy", "loudness", "speechiness", 
            "acousticness", "instrumentalness", "liveness", 
            "valence", "tempo", "duration_ms"]

available_cols = [c for c in num_cols if c in df.columns]

if len(available_cols) >= 2:
    corr = df[available_cols].corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Greens",
        title="Correlation Heatmap of Audio Features"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Not enough numeric columns available for correlation heatmap.")

# ----------------------------------------
# TEMPO DISTRIBUTION
# ----------------------------------------
st.markdown("### 🎶 Tempo Distribution (BPM)")

if "tempo" in df.columns:
    fig = px.histogram(
        df,
        x="tempo",
        nbins=30,
        title="Distribution of Song Tempos",
        color_discrete_sequence=["#84cc16"]
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Tempo column not found in dataset.")
