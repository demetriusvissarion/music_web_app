# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===


"""
When: I make a POST request to /albums
Then: I should get a 200 response
"""
def test_post_create_album(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    response = web_client.post('/albums', data={
        'title': 'Voyage', 
        'release_year': '2022', 
        'artist_id': '2'
        })

    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''



"""
When: I make a GET request to /albums
Then: I should get a 200 response with a list of records
"""
def test_get_all_records(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    web_client.post('/albums', data={
    'title': 'Voyage', 
    'release_year': '2022', 
    'artist_id': '2'
    })
    response = web_client.get('/albums')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        'Album(1, Doolittle, 1989, 1)\nAlbum(2, Surfer Rosa, 1988, 1)\nAlbum(3, Waterloo, 1974, 2)\nAlbum(4, Super Trouper, 1980, 2)\nAlbum(5, Bossanova, 1990, 1)\nAlbum(6, Lover, 2019, 3)\nAlbum(7, Folklore, 2020, 3)\nAlbum(8, I Put a Spell on You, 1965, 4)\nAlbum(9, Baltimore, 1978, 4)\nAlbum(10, Here Comes the Sun, 1971, 4)\nAlbum(11, Fodder on My Wings, 1982, 4)\nAlbum(12, Ring Ring, 1973, 2)\nAlbum(13, Voyage, 2022, 2)'


"""
When: I make a POST request to /albums with no data
Then: I should get a 400 response
"""
def test_post_create_album_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")

    response = web_client.post("/albums")
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "" \
        "No data to create album"

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        'Album(1, Doolittle, 1989, 1)\nAlbum(2, Surfer Rosa, 1988, 1)\nAlbum(3, Waterloo, 1974, 2)\nAlbum(4, Super Trouper, 1980, 2)\nAlbum(5, Bossanova, 1990, 1)\nAlbum(6, Lover, 2019, 3)\nAlbum(7, Folklore, 2020, 3)\nAlbum(8, I Put a Spell on You, 1965, 4)\nAlbum(9, Baltimore, 1978, 4)\nAlbum(10, Here Comes the Sun, 1971, 4)\nAlbum(11, Fodder on My Wings, 1982, 4)\nAlbum(12, Ring Ring, 1973, 2)'


"""
When: I make a GET request to /artists
Then: I should get a 200 response and a comma separated string of all artists
"""
def test_get_all_artists_string(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        'Pixies, ABBA, Taylor Swift, Nina Simone'



"""
When: I make a POST request to /artists
Then: I should get a 200 response and add a new artist to the DB
"""
def test_post_new_artist(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")

    post_response = web_client.post('/artists', data={
    'artist_name': 'Queen', 
    'genre': 'Rock'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        'Pixies, ABBA, Taylor Swift, Nina Simone, Queen'

