import webbrowser

class Movie:
	def __init__(self, movie_title, movie_story, poster_image, youtube_url):
		"""
			The init method get's initialized when an instance
			of this class is created in any other class.
		"""
		self.title = movie_title
		self.storyline = movie_story
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_url

	# Function to show trailer for a particular movie
	def show_trailer(self):
		"""
			The show_trailer instance method will 
			show the trailer of the movie, when the 
			movie poster is clicked.
		"""
		webbrowser.open(self.url)
