import media
import fresh_tomatoes
""" this program defines some of my favourite movies and shows them
    in a browser"""

# define my favourite Movies using the Movie class from the media module
toy_Story = media.Movie("Toy Story",
                        "1995",
                        "Story abaout a boy and his toys coming to Life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", #noqa
                        "https://www.youtube.com/watch/?v=KYz2wyBy3kc")
Life_of_Brian = media.Movie("Life of Brian",
                            "1979" ,
                            "It's not the story of the messias, \
                            it's the story of a naughty boy...",
                            "http://cdn-images.9cloud.us/953/piccit_monty_pythons_life_of_brian__565896653.jpg", #noqa
                            "https://www.youtube.com/watch/?v=IqnCf82LPcw")
Lucky_number_Slevin = media.Movie("Lucky#Slevin",
                                  "2006",
                                  "A case of mistaken identity lands Slevin \
                                  into the middle of a war being plotted by \
                                  two of the city's most rival crime bosses.",
                                  "http://ia.media-imdb.com/images/M/MV5BMzc1OTEwMTk4OF5BMl5BanBnXkFtZTcwMTEzMDQzMQ@@._V1_SY317_CR3,0,214,317_AL_.jpg", #noqa
                                  "https://www.youtube.com/watch?v=mKTo2nzYpic") #noqa
JungleBook = media.Movie("Junglebook",
                         "1967",
                         "Mowgli the human Child lives in the jungle and \
                         experiences thrilling adventures. ",
                         "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcT_Pg-KMWSXqx8fooDZeig4CPVPMV1JtCuJFj6p08HXava7RulK",#noqa
                         "https://www.youtube.com/watch?v=VBb-0KCqZgY")
High_Fidelity = media.Movie("High Fidelity",
                            "2003",
                            "Rob Gordon is a self-professed music junkie,\
                            who is going to go into adulthood.",
                            "http://resizing.flixster.com/ABWi1De55CZ4ac5BYk1lSO4FgmI=/180x258/dkpu1ddg7pbsk.cloudfront.net/movie/10/89/19/10891984_ori.jpg", #noqa
                            "https://www.youtube.com/watch?v=q8DIm_47xPU")
Love_Actually = media.Movie("Love actaually",
                            "2000",
                            "Christmas-themed romantic comedy telling the \
                            love-stories of many people.",
                            "https://upload.wikimedia.org/wikipedia/en/e/eb/Love_Actually_movie.jpg", #noqa
                            "https://www.youtube.com/watch?v=cYCkFTyADJ0")

#make a movie list form the defined movies
movies = [toy_Story,
          Life_of_Brian,
          Lucky_number_Slevin,
          JungleBook,
          High_Fidelity,
          Love_Actually]

# using the fresh tomato module to build the website from the movies data
fresh_tomatoes.open_movies_page(movies)

