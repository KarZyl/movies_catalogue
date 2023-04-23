from flask import Flask, render_template, request
import tmdb_client 
import random

app = Flask(__name__)


@app.route('/homepage')
def movies_gitpage():
    lists= ["now_playing","upcoming","popular","top_rated"]
    return render_template("index.html",lists=lists)

@app.route('/')
def homepage():
    lists = tmdb_client.get_lists()
    selected_list = request.args.get('list_type', 'popular')
    if selected_list in lists:
        pass
    else:
        selected_list = 'popular'
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    
   
    return render_template("homepage.html", movies=movies, current_list=selected_list, lists=lists)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
   details = tmdb_client.get_single_movie(movie_id)
   details["budget"] = tmdb_client.millify(details["budget"])
   if details["budget"] == "0":
       details["budget"] = "N/A"
   cast = tmdb_client.get_single_movie_cast(movie_id)[:8]
   movies = tmdb_client.get_popular_movies()["results"]
   random.shuffle(movies)
   movies=movies[:4]
   movie_images = tmdb_client.get_movie_images(movie_id)
   selected_backdrop = random.choice(movie_images['backdrops'])
   return render_template("movie_details.html", movie=details, cast=cast, movies=movies, selected_backdrop=selected_backdrop)


if __name__ == '__main__':
    app.run(debug=True)