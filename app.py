
from flask import Flask, request, render_template,  redirect, flash, session ,jsonify
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm
from models import db,  connect_db, Pet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    """Homepage displaying Pet information."""
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """GET, POST for adding a new Pet."""
    form = AddPetForm()
    if form.validate_on_submit():
        pet = Pet(name=form.name.data, species=form.species.data, photo_url=form.photo_url.data,
                  age=form.age.data, notes=form.notes.data )
        db.session.add(pet)
        db.session.commit()
        return redirect('/')          
    
    else:
        return render_template('add.html', form=form)

@app.route('/<int:pet_id>', methods=["GET"])
def show_pet_information(pet_id):
    pet = Pet.query.get(pet_id)
    return render_template('pet_info.html', pet=pet)

@app.route('/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet_information(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    form = AddPetForm()

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        
        return redirect(f'/{pet_id}')
    else:
        return render_template('edit.html', form=form ,pet=pet)


@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)