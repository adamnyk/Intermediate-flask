from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://t4.ftcdn.net/jpg/01/09/55/57/360_F_109555726_MbLWroPqwqdG8xoLumIJMVQervQpA8nN.jpg"

def connect_db(app):
    db.app = app
    db.init_app(app)



# MODELS GO BELOW!


class Pet(db.Model):
    """Pets Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.Text, default=DEFAULT_IMAGE_URL)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<Pet {self.id} {self.name} {self.species} {self.available}>"
