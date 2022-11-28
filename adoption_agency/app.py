from flask import Flask, request, render_template, redirect, flash, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, DEFAULT_IMAGE_URL
from forms import PetForm, EditPetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adopt_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "chickenzarecool21837"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)
app.app_context().push()

connect_db(app)


@app.route("/")
def home_page():
    """Render home page"""
    pets = Pet.query.all()
    return render_template("list_pets.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Renders pet form (GET) or pet snack form submission (POST)""" 
    form = PetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        img_url = form.img_url.data or None
        age = form.age.data or None
        notes = form.notes.data or None
        
        new_pet = Pet(name=name, species=species, img_url=img_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Added new pet: {name}")
        return redirect(url_for('home_page'))
    else:
        return render_template("add_pet_form.html", form=form)


@app.route("/<int:id>", methods=["GET", "POST"])
def view_pet(id):
    pet = Pet.query.get_or_404(id)
    form=EditPetForm(obj=pet)
    
    if form.validate_on_submit():

        pet.img_url = form.img_url.data 
        pet.notes = form.notes.data 
        pet.available = form.available.data 
        
        db.session.add(pet)
        db.session.commit()
        flash(f"Edited pet: {pet.name}")
        return redirect(url_for('home_page'))
    else: 
        return render_template("view_pet.html", pet=pet, form=form)


@app.route("/<int:id>/delete", methods=["POST"])
def delete_pet(id):
    pet = Pet.query.get_or_404(id)

    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for("home_page"))
    
