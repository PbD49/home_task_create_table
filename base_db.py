import sqlite3

conn = sqlite3.connect('music_database.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS Genres (
        id INTEGER PRIMARY KEY,
        name_genres TEXT UNIQUE
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Artists (
        id INTEGER PRIMARY KEY,
        name_artists TEXT
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Albums (
        id INTEGER PRIMARY KEY,
        name_album TEXT,
        year_of_issue INTEGER CHECK (year_of_issue >= 1900),
        genre_id INTEGER,
        FOREIGN KEY (genre_id) REFERENCES Genres(id)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS ArtistGenres (
        artist_id INTEGER,
        genre_id INTEGER,
        PRIMARY KEY (artist_id, genre_id),
        FOREIGN KEY (artist_id) REFERENCES Artists(id),
        FOREIGN KEY (genre_id) REFERENCES Genres(id)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS ArtistAlbums (
        artist_id INTEGER,
        album_id INTEGER,
        PRIMARY KEY (artist_id, album_id),
        FOREIGN KEY (artist_id) REFERENCES Artists(id),
        FOREIGN KEY (album_id) REFERENCES Albums(id)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS List_of_songs (
        id INTEGER PRIMARY KEY,
        name_songs TEXT,
        song_duration INTEGER CHECK (song_duration > 0),
        album_id INTEGER,
        FOREIGN KEY (album_id) REFERENCES Albums(id)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Collection (
        id INTEGER PRIMARY KEY,
        name_collection TEXT,
        year_of_issue INTEGER CHECK (year_of_issue >= 1900)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS SongCollection (
        song_id INTEGER,
        collection_id INTEGER,
        PRIMARY KEY (song_id, collection_id),
        FOREIGN KEY (song_id) REFERENCES List_of_songs(id),
        FOREIGN KEY (collection_id) REFERENCES Collection(id)
    )
''')

conn.commit()
conn.close()
