import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys which come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc")
                        
#print toy_story.storyline

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")
#print avatar.storyline

#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock",
                     "Using rock music to learn",
                     "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                     "https://youtu.be/3PsUJFEBC74")
                     
ratatouille = media.Movie("Ratatouille",
                     "A rat is a chef in Paris",
                     "https://en.wikipedia.org/wiki/Ratatouille_%28film%29#/media/File:RatatouillePoster.jpg",
                     "https://youtu.be/c3sBBRxDAqk")
                     
midnight_in_paris = media.Movie("Midnight in Paris",
                     "Going back in time to meet authors",
                     "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "https://youtu.be/wuOUdZjuCIA")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris]
fresh_tomatoes.open_movies_page(movies)
                     