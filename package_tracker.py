from flask import Flask, render_template, redirect
from config import Config
from app.shipping_form import PackageForm
from map.map import map


app = Flask(__name__)

app.config.from_object(Config)

@app.route("/")
def root():
  print("test string")
  return "You made it!"

@app.route("/new-package", methods=["GET", "POST"])
def package():
  form = PackageForm()
  cities = [city for city in map.keys()]
  form.origin.choices = cities
  form.destination.choices = cities
  if form.validate_on_submit():
    data = form.to_dict()
    if data["submit"]:
      return redirect("/")
  return render_template("shipping_request.html", form=form)
