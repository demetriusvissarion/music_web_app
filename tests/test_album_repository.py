from lib.album import Album
from lib.album_repository import AlbumRepository

"""
#all method returns a list of all album objects
"""
def test_all(db_connection):
    db_connection.seed("seeds/music_web_app.sql") # Seed our database with some test data
    album1 = Album(1, "Test Album 1", 1977, 1)
    album2 = Album(2, "Test Album 2", 1978, 2)
    album_repository = AlbumRepository(db_connection)
    album_repository.create(album1)
    album_repository.create(album2)
    assert str(album_repository.all()) == '[Album(1, Doolittle, 1989, 1), Album(2, Surfer Rosa, 1988, 1), Album(3, Waterloo, 1974, 2), Album(4, Super Trouper, 1980, 2), Album(5, Bossanova, 1990, 1), Album(6, Lover, 2019, 3), Album(7, Folklore, 2020, 3), Album(8, I Put a Spell on You, 1965, 4), Album(9, Baltimore, 1978, 4), Album(10, Here Comes the Sun, 1971, 4), Album(11, Fodder on My Wings, 1982, 4), Album(12, Ring Ring, 1973, 2), Album(13, Test Album 1, 1977, 1), Album(14, Test Album 2, 1978, 2)]'


"""
Given an album id
#find method returns a specific album from the DB
"""
def test_find(db_connection):
    db_connection.seed("seeds/music_web_app.sql") # Seed our database with some test data
    album1 = Album(1, "Test Album 1", 1977, 1)
    album2 = Album(2, "Test Album 2", 1978, 2)
    album_repository = AlbumRepository(db_connection)
    album_repository.create(album1)
    album_repository.create(album2)
    assert str(album_repository.find(1)) == 'Album(1, Doolittle, 1989, 1)'


"""
When we call AlbumRepository#create
We get a new album in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "Test Album 3", 1979, 3))

    result = repository.all()
    assert str(result) == '[Album(1, Doolittle, 1989, 1), Album(2, Surfer Rosa, 1988, 1), Album(3, Waterloo, 1974, 2), Album(4, Super Trouper, 1980, 2), Album(5, Bossanova, 1990, 1), Album(6, Lover, 2019, 3), Album(7, Folklore, 2020, 3), Album(8, I Put a Spell on You, 1965, 4), Album(9, Baltimore, 1978, 4), Album(10, Here Comes the Sun, 1971, 4), Album(11, Fodder on My Wings, 1982, 4), Album(12, Ring Ring, 1973, 2), Album(13, Test Album 3, 1979, 3)]'


"""
When we call AlbumRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert str(result) == '[Album(1, Doolittle, 1989, 1), Album(2, Surfer Rosa, 1988, 1), Album(4, Super Trouper, 1980, 2), Album(5, Bossanova, 1990, 1), Album(6, Lover, 2019, 3), Album(7, Folklore, 2020, 3), Album(8, I Put a Spell on You, 1965, 4), Album(9, Baltimore, 1978, 4), Album(10, Here Comes the Sun, 1971, 4), Album(11, Fodder on My Wings, 1982, 4), Album(12, Ring Ring, 1973, 2)]'