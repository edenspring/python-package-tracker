from flask import Flask, render_template, redirect
from config import Config
from app.shipping_form import PackageForm
from map.map import map
from flask_migrate import Migrate
from app.models import db, Package

app = Flask(__name__)


app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def root():
  packages = Package.query.all()
  print(packages[0])
  return render_template("package_status.html", packages=packages)

@app.route("/new-package", methods=["GET", "POST"])
def package():
  form = PackageForm()
  cities = [city for city in map.keys()]
  form.origin.choices = cities
  form.destination.choices = cities
  if form.validate_on_submit():
    data = form.to_dict()
    if data["submit"]:
      new_package = Package(sender=data["sender_name"],
                                recipient=data["recipient_name"],
                                origin=data["origin"],
                                destination=data["destination"],
                                location=data["origin"])
      db.session.add(new_package)
      db.session.commit()
      Package.advance_all_locations()
    return redirect("/")
  return render_template("shipping_request.html", form=form)
