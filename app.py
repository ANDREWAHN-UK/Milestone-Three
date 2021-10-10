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
    review = mongo.db.reviews.find()
    reviews = mongo.db.reviews.find().sort("place_rating")
    
    if session["user"]:
        return render_template(
            "profile.html", username=username, review=review, reviews=reviews)

    return redirect(url_for("login"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/reviews")
def reviews():
    reviews = mongo.db.reviews.find().sort("visit_date")
    return render_template("reviews.html", reviews=reviews)

@app.route("/logout")
def logout():
    flash("Goodbye, thanks for visiting")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/create_review", methods=["GET", "POST"])
def create_review():

    if request.method == "POST":
        
        review = {
            "category_name": request.form.get("category_name"),
            "image_url": request.form.get("image_url"),
            "place_rating": request.form.get("place_rating"),
            "place_review": request.form.get("place_review"),
            "visit_date": request.form.get("visit_date"),
            "visit_type": request.form.get("visit_type"),
            "place_name": request.form.get("place_name"),
            "created_by": session["user"]
        }
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("profile", username=username, review=review))

    categories = mongo.db.category.find().sort("category_name", 1)
    ratings = mongo.db.rating.find().sort("rating", 1)
    visits = mongo.db.visit.find().sort("type", 1)
    
    return render_template(
        "create_review.html",
        categories=categories, visits=visits, ratings=ratings, )


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    review = mongo.db.find_one({"_id": ObjectId(review_id)})
    categories = mongo.db.category.find().sort("category_name", 1)
    ratings = mongo.db.rating.find().sort("rating", 1)
    visits = mongo.db.visit.find().sort("type", 1)
    return render_template(
        "edit_review.html", categories=categories,
        visits=visits, ratings=ratings, review=review)
 

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
