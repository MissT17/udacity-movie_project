import webbrowser


# Create a class with the properties that we would like objects to have.
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


# Create a method that would create a webpage and display
# the content of the list.
    # def show_trailer(self):
    #    webbrowser.open(self.trailer_youtube_url)
