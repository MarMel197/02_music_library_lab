from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository


def save(album):
    sql = (
        "INSERT INTO albums (title, genre, artist_id) VALUES ( %s, %s, %s ) RETURNING *"
    )
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    album.id = id
    return album


def select_all():
    # Create an empty list
    albums = []

    # Get all the albums from albums table is SQL and store in results
    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    # For each album in results
    for row in results:
        # create an artist variable using the select(id) method from artist_repository
        artist = artist_repository.select(row["artist_id"])
        # Use this artist variable for the artist name when creating the album object below
        album = Album(row["title"], row["genre"], artist)
        # Add the above object to the list albums
        albums.append(album)
    # return the list
    return albums


def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result["artist_id"])
        album = Album(result["title"], result["genre"], artist, result["id"])
    return album


def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(album):
    sql = "UPDATE albums SET ( name ) = ( %s ) WHERE id = %s"
    values = [album.title, album.genre, album.artist_id, album.id]
    run_sql(sql, values)