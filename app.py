from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Main Page"


# TASK 01
@app.route("/me")
def me():
    return "Tomasz Pietrzak"


# TASK 02
@app.route("/<function_name>/<int:a>/<int:b>")
def function(function_name, a, b):
    if function_name == "add":
        return str(a + b)
    elif function_name == "subtract":
        return str(a - b)
    else:
        return """Invalid function. Use 'add' or 'subtract'.
        Example: /add/5/3 or /subtract/10/4"""


# TASK 03, 04
@app.route("/movies")
def movies():
    movies_list = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]
    title = "My favorite movies"
    return render_template("movies.html", movies=movies_list, title=title)


# TASK 06
@app.route("/book")
def book():
    book_items = {
        "title": "Ender's Game",
        "author": "Orson Scott Card",
        "year": 1985,
        "genre": "Science Fiction",
    }
    return render_template(
        "book.html",
        title=book_items["title"],
        author=book_items["author"],
        year=book_items["year"],
        genre=book_items["genre"],
    )


if __name__ == "__main__":
    app.run(debug=True)
