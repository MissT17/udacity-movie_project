import media
import fresh_tomatoes

# Create instances of the Movie class with the necessary properties.
film1 = media.Movie("Allied", "A romantic thriller about a Canadian"
                    " intelligence officer and Marion Cotillard as a"
                    " French Resistance fighter and collaborator, who"
                    " fall in love during a mission in Casablanca.",
                    "https://upload.wikimedia.org/wikipedia/en/4/43/Allied_%28film%29.png",  # NOQA
                    "https://www.youtube.com/watch?v=Jlp94-C31cY")

film2 = media.Movie("Casablanca", "Set during World War II, the film"
                    " focuses on an American expatriate who must choose"
                    " between his love for a woman and helping her Czech"
                    " Resistance leader husband escape the Vichy-controlled"
                    " city of Casablanca to continue his fight against"
                    " the Nazis.",
                    "https://upload.wikimedia.org/wikipedia/commons/b/b3/CasablancaPoster-Gold.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=BkL9l7qovsE")

film3 = media.Movie("X-Men: The Last Stand", "A superhero film with a plot"
                    " that revolves around a 'mutant cure' that causes"
                    " serious repercussions among mutants"
                    " and humans.",
                    "https://upload.wikimedia.org/wikipedia/en/5/56/X-Men_The_Last_Stand.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=x_EZZrIErDI")

film4 = media.Movie("X-Men", "An American superhero film series"
                    " based on the fictional superhero team of the same name.",
                    "https://upload.wikimedia.org/wikipedia/en/8/8c/XMen1poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=nbNcULQFojc")

film5 = media.Movie("The Wolverine", "In the film, which follows"
                    " the events of X-Men: The Last Stand, Logan travels"
                    " to Japan, where he engages an old"
                    " acquaintance in a struggle that has lasting"
                    " consequences. Stripped of his healing factor, Wolverine"
                    " must battle deadly samurai while struggling with guilt.",
                    "https://upload.wikimedia.org/wikipedia/en/7/74/The_Wolverine_posterUS.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=th1NTVIhUQU")

film6 = media.Movie("Kate & Leopold", "A story of a duke who travels"
                    " through time from New York in 1876 to the present"
                    " and falls in love with a woman in modern New York.",
                    "https://upload.wikimedia.org/wikipedia/en/6/6b/Kate_and_leopold_ver2.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=lFJywpD2PU4")

# Create a list of films that will be displayed on the webpage
movies = [film1, film2, film3, film4, film5, film6]

# Call the method that will create the page and display the content
# of the list movies.
fresh_tomatoes.open_movies_page(movies)
