import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A young boy and all his toys coming to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

extra_terrestrial = media.Movie("E.T", "Aliens on Earth", "https://upload.wikimedia.org/wikipedia/en/6/66/E_t_the_extra_terrestrial_ver3.jpg", "https://www.youtube.com/watch?v=oR1-UFrcZ0k")

harry_potter = media.Movie("Harry Potter", "Life of a young wizard", "https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Philosopher%27s_Stone_posters.JPG", "https://www.youtube.com/watch?v=PbdM1db3JbY")

indian_jones = media.Movie("Indiana Jones", "An explorer", "https://upload.wikimedia.org/wikipedia/en/d/d5/Kingdomofthecrystalskull.jpg", "https://www.youtube.com/watch?v=nMhfESAa4tw")

deadpool = media.Movie("Deadpool", "A Psycho", "https://upload.wikimedia.org/wikipedia/commons/c/cd/WW_Chicago_2015_-_Deadpool_%2821056427731%29.jpg", "https://www.youtube.com/watch?v=ZIM1HydF9UA")

movies = [toy_story, avatar, extra_terrestrial, harry_potter, indian_jones, deadpool]
fresh_tomatoes.open_movies_page(movies)
