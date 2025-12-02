-- 1. Top 10 most popular songs
SELECT track_name, artists, popularity
FROM spotify_tracks
ORDER BY popularity DESC
LIMIT 10;

-- 2. Most common genres
SELECT genre, COUNT(*) AS total
FROM spotify_tracks
GROUP BY genre
ORDER BY total DESC;

-- 3. Top artists by number of tracks
SELECT artists, COUNT(*) AS total_songs
FROM spotify_tracks
GROUP BY artists
ORDER BY total_songs DESC
LIMIT 10;

-- 4. Average audio features per genre
SELECT genre, 
       AVG(danceability) AS avg_dance,
       AVG(energy) AS avg_energy,
       AVG(valence) AS avg_valence
FROM spotify_tracks
GROUP BY genre;

-- 5. Longest songs
SELECT track_name, artists, duration_ms
FROM spotify_tracks
ORDER BY duration_ms DESC
LIMIT 10;

-- 6. Yearly trend of number of songs released
SELECT year, COUNT(*) AS count_songs
FROM spotify_tracks
GROUP BY year
ORDER BY year;
