from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def movies_page():
    return render_template("index.html")

@app.route('/homepage')
def homepage():
    movies = []
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)