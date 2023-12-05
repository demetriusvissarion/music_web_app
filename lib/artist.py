class Artist:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, genre, albums = []):
        self.artist_id = id
        self.artist_name = name
        self.genre = genre
        self.albums = albums

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        if len(self.albums) > 0:
            return f"Artist({self.artist_id}, {self.artist_name}, {self.genre}, {self.albums})"
        return f"Artist({self.artist_id}, {self.artist_name}, {self.genre})"
