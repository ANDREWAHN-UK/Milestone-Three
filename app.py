import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/go_home")
def go_home():
    reviews = mongo.db.reviews.find()
    return render_template("home.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
      
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("This username already exists, please choose another")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        
        session["user"] = request.form.get("username").lower()
        flash("You have been successfully registered, congratulations!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Hello, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                flash("Incorrect username/password, please try again")
                return redirect(url_for("login"))
      
        else:
            flash("Incorrect username/password, please try again")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/logout")
def logout():
    flash("Goodbye, thanks for visiting")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/create_review", methods=["GET", "POST"])
def create_review():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        # these pick up the id names in the form on create_review.html
        review = {
            "title": request.form.get("title"),             
            "image_url": request.form.get("image_url"),
            "created_by": session["user"],
            "location": request.form.get("location"),            
            "date_picker": request.form.get("date_picker"),
            "place_type": request.form.get("place_type"),
            "rating": request.form.get("rating"),
            "review": request.form.get("review"),
            "date": datetime.datetime.now().strftime("%d %B, %Y")
        }
        mongo.db.blog.insert_one(reviews)
        flash("Review added successfully")
        return redirect(url_for("create_review"))

    posts = mongo.db.blog.find()
    return render_template(
        "create_review.html", posts=posts, page_title="Create Review")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
