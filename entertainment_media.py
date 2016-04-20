import media
import urllib
import json
import fresh_tomatoes

# Function to get movie details
def get_movie_details(movie_name):
	movie_data = urllib.urlopen('http://www.omdbapi.com/?s='+movie_name)
	return movie_data.read()

# Function to get the movie poster for a particular movie
def get_movie_poster(movie_name):
	movie_data_hash = json.loads(get_movie_details(movie_name))
	movie_poster = movie_data_hash['Search'][1]['Poster'].encode('utf-8').encode('ascii', 'ignore')
	return movie_poster

# Function to get the movie title for a particular movie
def get_movie_title(movie_name):
	movie_data_hash = json.loads(get_movie_details(movie_name))
	movie_title = movie_data_hash['Search'][1]['Title'].encode('utf-8').encode('ascii', 'ignore')
	return movie_title

# Instances of the Class Movie
toy_story = media.Movie(
	"Toy Story", 
	get_movie_title('Toy Story'), 
	get_movie_poster('Toy Story'), 
	"https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie(
	"Avatar", 
	get_movie_title('Avatar'), 
	get_movie_poster('Avatar'), 
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")

extra_terrestrial = media.Movie(
	"E.T", 
	get_movie_title('Extra Terrestrial'), 
	get_movie_poster('Extra Terrestrial'), 
	"https://www.youtube.com/watch?v=oR1-UFrcZ0k")

harry_potter = media.Movie(
	"Harry Potter", 
	get_movie_title('Harry Potter'), 
	get_movie_poster('Harry Potter'), 
	"https://www.youtube.com/watch?v=PbdM1db3JbY")

indiana_jones = media.Movie(
	"Indiana Jones", 
	get_movie_title('Indiana Jones'), 
	get_movie_poster('Indiana Jones'), 
	"https://www.youtube.com/watch?v=nMhfESAa4tw")

deadpool = media.Movie(
	"Deadpool", 
	get_movie_title('Deadpool'), 
	get_movie_poster('Deadpool'), 
	"https://www.youtube.com/watch?v=ZIM1HydF9UA")

# List of all the movies
movies = [toy_story, avatar, extra_terrestrial, harry_potter, indiana_jones, deadpool]

# Passing the movies list to fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
