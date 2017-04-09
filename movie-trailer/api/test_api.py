import urllib
import json
import media
import fresh_tomatoes
import re
from youtube_video_api import youtube_search


def create_film_list(requested_films):
    #  This is the source that provides us with the information (title,
    #  description and the poster) related to the movies.
    source = "http://www.omdbapi.com/?"

    movies = []
    for film in requested_films:
        #  The variable changes its name here just for the easier comprehension
        #  of my thinking process.
        user_input = film
        user_input = user_input.lower()
        url = source + "t=" + user_input
        handle = urllib.urlopen(url).read()
        info = json.loads(str(handle))
        if info["Response"] != "False":
            storyline = info["Plot"]
            poster_image_url = info["Poster"]
            title = info["Title"]
        else:
            title = "The film <span style='color:red'>" + str(user_input) + "</span> was not found in the database."  # NOQA
            storyline = ""
            poster_image_url = ""
        #  The user_input is used in the youtube query to identify
        #  the correct movie trailer (the url extension to the movie trailer).
        video_code = str(youtube_search(user_input))
        #  The youtube url extension to the movie trailer is used to create
        #  the full youtube url to the movie trailer.
        result_url = "http://www.youtube.com/watch?v=" + video_code
        film = media.Movie(title, storyline, poster_image_url, result_url)
        movies.append(film)

    fresh_tomatoes.open_movies_page(movies)
