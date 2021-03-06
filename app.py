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

# NB - most of this follows the Code Institute Mini Project in syntax and logic


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

        # the ""on the left is what gets put into the database, 
        # the ("") on the right is what gets taken from the form
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "image_url": request.form.get("image_url"),
            "user_bio": request.form.get("user_bio")
        }
        mongo.db.users.insert_one(register)
        
        session["user"] = request.form.get("username").lower()
        flash("You have been successfully registered, congratulations!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/edit_profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):

    if request.method == "POST":
        
        update_register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "image_url": request.form.get("image_url"),
            "user_bio": request.form.get("user_bio")
        }
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        mongo.db.users.update({"_id": ObjectId(user_id)}, update_register)
        flash("Profile Successfully Edited")
        review = mongo.db.reviews.find()
        return redirect(url_for("profile", username=username, review=review))
        
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    categories = mongo.db.category.find().sort("category_name", 1)
    ratings = mongo.db.rating.find().sort("rating", 1)
    visits = mongo.db.visit.find().sort("type", 1)
    users = mongo.db.users.find().sort("username")

    return render_template(
        "edit_profile.html", categories=categories,
        visits=visits, ratings=ratings, users=users, user=user)


@app.route("/delete_review/<user_id>")
def delete_profile(user_id):
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("User Successfully Deleted")
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return redirect(url_for("login", username=username, user=user))


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


@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    review = mongo.db.reviews.find()
    user_image = mongo.db.users.find_one(
        {"username": session["user"]})["image_url"]
    reviews = mongo.db.reviews.find().sort("place_rating")
    user_bio = mongo.db.users.find_one(
        {"username": session["user"]})["user_bio"]
    
    users = mongo.db.users.find().sort("username")
    user = mongo.db.users.find()
    
    if session["user"]:
        return render_template(
            "profile.html", username=username,
            review=review, reviews=reviews,
            user_image=user_image, user_bio=user_bio, users=users, user=user)

    return redirect(url_for("login"))


@app.route("/reviews")
def reviews():
    reviews = mongo.db.reviews.find().sort("visit_date")
    users = mongo.db.users.find().sort("username")
    return render_template("reviews.html", reviews=reviews, users=users)


@app.route("/search", methods=["GET", "POST"])
def search():
    search = request.form.get("search")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": search}}))
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
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, review)
        flash("Review Successfully Edited")
        return redirect(url_for("profile", username=username, review=review))
        
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    categories = mongo.db.category.find().sort("category_name", 1)
    ratings = mongo.db.rating.find().sort("rating", 1)
    visits = mongo.db.visit.find().sort("type", 1)

    return render_template(
        "edit_review.html", review=review,
        categories=categories, visits=visits, ratings=ratings,)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return redirect(url_for("profile", username=username, review=review))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
