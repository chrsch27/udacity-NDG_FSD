import webbrowser

# The Movie-Class contains the properties an values of a Movie Object
class Movie():

    def __init__ (self,movie_title,movie_year,movie_storyline,poster_image,trailer_youtube):
        """ Constructor of the Movie Class. Takes the values movie_title, movie_year,
            movie-Storyline, poster_image_url, trailer youtube to instantiate the object"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year=movie_year

    def showMedia (self):
        """ showMedia opens the trailer_youtube - Url of the object in a webbrowser"""
        webbrowser.open(self.trailer_youtube_url)
