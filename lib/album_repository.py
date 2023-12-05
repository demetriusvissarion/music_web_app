from lib.album import Album

class AlbumRepository:
    def __init__(self, connection=None):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        # print('rows: ', rows)
        albums = []
        for row in rows:
            item = Album(row["album_id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

    def create(self, album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [album.title, album.release_year, album.artist_id])
        return None
    
    def find(self, album_id):
        raw_data = self._connection.execute('SELECT * from albums WHERE album_id = %s', [album_id])
        data = raw_data[0]
        return Album(data["album_id"], data["title"], data["release_year"], data["artist_id"])
    

    # Delete an album by their id
    def delete(self, album_id):
        self._connection.execute(
            'DELETE FROM albums WHERE album_id = %s', [album_id])
        return None