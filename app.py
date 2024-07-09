
from flask import Flask, request, render_template, redirect, flash, session, url_for
from forms import AddPetForm
from models import db, connect_db, Pet
import random

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://marinasukhova:1111@localhost:5432/adopt"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SECRET_KEY"] = "SECRET!"
from flask_debugtoolbar import DebugToolbarExtension

app.debug = True
debug = DebugToolbarExtension(app)


connect_db(app)

@app.route("/")
def list_pets():
    """list all pets is DB"""
    pets = Pet.query.all()
    random_pets = random.sample(pets, 6)
    return render_template("home_page.html", pets=random_pets)

@app.route("/<int:id>/view")
def show_pet_details(id):
    """show the pet"""
    pet = Pet.query.get_or_404(id)
    return render_template("pet_details.html", pet=pet)

@app.route("/<int:id>/apply")
def apply_for_pet(id):
    pet = Pet.query.get_or_404(id)
    return render_template("pet_application.html", pet=pet)

@app.route('/add/pet', methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url= photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        print("new pet:" , new_pet)
        flash(f"New pet has been added: name is {name}, species is  is ${species} ")
        return redirect(url_for('show_pet_details', id=new_pet.id))
    else:
        return render_template("add_pet.html", form=form)


