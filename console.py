import pdb

from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository

artist_repository.delete_all()

artist1 = Artist("Thin Lizzy")

artist_repository.save(artist1)

artist_repository.select_all()


pdb.set_trace()