import os
from flask import Flask, request
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
# from example_routes import apply_example_routes
# apply_example_routes(app)

# == End Example Code ==

# Request:
# POST /albums
#   With body parameter: title=Voyage, release_year=2022, artist_id=2
@app.route('/albums', methods=['POST'])
def create_album():
    if check_if_data_is_valid(request.form):
        return "No data to create album", 400
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)

    title = request.form['title'] 
    release_year = request.form['release_year'] 
    artist_id = request.form['artist_id']
    album = Album(None, title, release_year, artist_id)
    album_repository.create(album)
    return '', 200

def check_if_data_is_valid(form):
    return 'title' not in form or \
        'release_year' not in form or \
        'artist_id' not in form


# Request:
# GET /albums
#   With body parameter: 
@app.route('/albums', methods=['GET'])
def get_all_records():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    return "\n".join(
        f"{album}" for album in album_repository.all()
    )

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

