import requests
import math
import json

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxODhiZDgzZWJjYTczMzQ5OWI1OGQyODdmMGY4Y2Q1OCIsInN1YiI6IjY0M2MzNWYxZGExMGYwMWIzYjY0ZTNjZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.c67qzVAMHnttsamXTDfj6ci3MY9mLldDHjGapkznkFo"

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()


def get_popular_movies():
    endpoint = "movie/popular"
    return call_tmdb_api(endpoint)

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"movie/{movie_id}"
    return call_tmdb_api(endpoint)

def get_single_movie_cast(movie_id):
    endpoint = f"movie/{movie_id}/credits"
    return call_tmdb_api(endpoint)["cast"]

def millify(n):
    millnames = ['',' Thousand',' Million',' Billion',' Trillion']
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

def get_movie_images(movie_id):
    endpoint = f"movie/{movie_id}/images"
    return call_tmdb_api(endpoint)

def get_movies_list(list_name):
    endpoint = f"movie/{list_name}"
    return call_tmdb_api(endpoint)

def get_movies(how_many, list_name):
    data = get_movies_list(list_name)
    return data["results"][:how_many]

def get_lists():
    response= ['now_playing','upcoming','popular','top_rated']
    return response

