from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

@app.route("/reviews", methods=["GET", "POST"])
def reviews_page():
    if request.method == "POST":
        name = request.form["name"]
        text = request.form["review"]
        new_review = Review(name=name, text=text)
        db.session.add(new_review)
        db.session.commit()
        return redirect("/reviews")
    
    all_reviews = Review.query.all()
    return render_template("reviews.html", reviews=all_reviews)

if _name_ == "_main_":
    app.run(debug=True)