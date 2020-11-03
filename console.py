import pdb

from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository

artist1 = Artist("Thin Lizzy")

artist_repository.save(artist1)


pdb.set_trace()