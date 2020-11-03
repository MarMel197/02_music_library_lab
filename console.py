import pdb

from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()
album_repository.delete_all()

artist1 = Artist("Thin Lizzy")
artist_repository.save(artist1)

album1 = Album("Whiskey in the Jar", "Rock", artist1)
album2 = Album("The Boys Are Back in Town", "Rock", artist1)
album3 = Album("Live and Dangerous", "Rock", artist1)

album_repository.save(album1)
album_repository.save(album2)
album_repository.save(album3)


artist_repository.select_all()
album_repository.select_all()


pdb.set_trace()