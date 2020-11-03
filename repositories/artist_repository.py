from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

# import repositories.album_repository as album_repository


def save(artist):

    sql = "INSERT INTO artists (name) VALUES ( %s ) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    artist.id = id
    return artist


def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row["name"], row["id"])
        artists.append(artist)
    return artists


def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)