from lib.album import Album

"""
Album constructs with an album_id, title, release_year and artist_id
"""
def test_album_constructs():
    album = Album(1, "Test Album", "Test Release Year", 1)
    assert album.album_id == 1
    assert album.title == "Test Album"
    assert album.release_year == "Test Release Year"
    assert album.artist_id == 1