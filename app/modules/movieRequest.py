
import requests
import json

class MovieFinder():
	def __init__(self):
		self.getGenres()
	def getGenres(self):
		x = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=5bd0b5f0618794cf1f526c25515abdc1&language=en-US").content
		x = json.loads(x)
		x = x['genres']
		self.genres = {}
		for dictionary in x:
			self.genres[dictionary['name'].upper()] = dictionary['id']
		
	def getMovies(self, genre_name, limit = 10):
			with_genres = ''
			commaspace = '%2C%20'
			for name in genre_name:
				name = name.upper()	
				genre_id = self.genres[name]
				with_genres = with_genres + str(genre_id) + commaspace

			x = requests.get(f'https://api.themoviedb.org/3/discover/movie?api_key=5bd0b5f0618794cf1f526c25515abdc1&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres={with_genres}').content
			movies = json.loads(x)
			movies = movies['results']
			self.suggestions = []

			for movie in movies:
				if len(self.suggestions) < limit:
					movie_info = {}
					movie_info['Title'] = movie['title']
					movie_info['Overview'] = movie['overview']
					if movie_info['Overview'] == '':
						movie_info['Overview'] = 'No Description Available.'
					movie_info['Rating'] = movie['vote_average']
					if movie_info['Rating'] == '':
						movie_info['Rating'] = 'No Rating Available'
					movie_info['Genres'] = movie['genre_ids']
					tmp = []
					for id_ in movie_info['Genres']:
						for genre_name, genre_id in self.genres.items():
							if id_ == genre_id:
								tmp.append(genre_name.lower().capitalize())
					movie_info['Genres'] = tmp

					self.suggestions.append(movie_info)
				final_suggestions = json.dumps(self.suggestions)
			#output =  final_suggestions
			output = self.suggestions
			return output
#broken formating
			# 	final_output = ''
			# 	for movie_title, movie_info in self.output.items():
			# 		final_output = final_output + (f""""{movie_title}":\n{movie_info['overview']}\n\nRating: {movie_info['rating']}/10\n\n\n""")
			
			# return final_output



if __name__ == '__main__':
    mf = MovieFinder()
    print(json.dumps(mf.getMovies(["ACTION","COMEDY"],3),indent=1))