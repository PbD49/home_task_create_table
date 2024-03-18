import sqlite3

conn = sqlite3.connect('music_database.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Genres (
    id SERIAL PRIMARY KEY,
    name_genres TEXT
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS Artists (
    id SERIAL PRIMARY KEY,
    name_artists TEXT
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS Albums (
    id SERIAL PRIMARY KEY,
    name_album TEXT,
    year_of_issue INTEGER
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS ArtistAlbums (
    artist_id INTEGER,
    album_id INTEGER,
    PRIMARY KEY (artist_id, album_id),
    FOREIGN KEY (artist_id) REFERENCES Artists(id),
    FOREIGN KEY (album_id) REFERENCES Albums(id)
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS List_of_songs (
    id SERIAL PRIMARY KEY,
    name_songs TEXT,
    song_duration INTEGER,
    album_id INTEGER,
    FOREIGN KEY (album_id) REFERENCES Albums(id)
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS Collection (
    id SERIAL PRIMARY KEY,
    name_collection TEXT,
    year_of_issue INTEGER
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS SongCollection (
    song_id INT,
    collection_id INT,
    PRIMARY KEY (song_id, collection_id),
    FOREIGN KEY (song_id) REFERENCES List_of_songs(id),
    FOREIGN KEY (collection_id) REFERENCES Collection(id)
);""")

conn.commit()
conn.close()