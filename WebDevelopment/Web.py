from flask import Flask, render_template, url_for, send_from_directory
import os

app = Flask(__name__)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/about")
def about(name=None):
    return render_template("about.html", name=name)


@app.route("/blog")
def blog(name=None):
    return "Blog Page"


@app.route("/<username>/<int:post_id>")
def show_user_profile(username=None, post_id=None):
    return render_template("about.html", name=username, post_id=post_id)


# @app.route("/blog/2020/dogs")
# def blog2():
#     return "This is my dog"
