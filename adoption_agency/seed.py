"""Seed file to make sample data for adoption db."""

from models import db, Pet
from app import app

db.drop_all()
db.create_all()


# Add pets

tina = Pet(
    name="Tina",
    species="hedgehog",
    img_url="https://nypost.com/wp-content/uploads/sites/2/2021/05/hedgehog.jpg?quality=75&strip=all&w=1488",
    age=4,
    available=False,
)
yuki = Pet(
    name="Yuki",
    species="dog",
    img_url="https://scontent-iad3-1.xx.fbcdn.net/v/t39.30808-6/306992082_10161853861704392_3834033049827520645_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=0debeb&_nc_ohc=68moG2AnxSEAX8MrRI8&_nc_ht=scontent-iad3-1.xx&oh=00_AfClJkJnU2S8l_ZS3oQvcNygpYGweCPIG-yusbcIfnd3wg&oe=63857C75",
    age=1,
    available=False,
)
skunky = Pet(name="Skunky", species="cat")

db.session.add(tina)
db.session.add(yuki)
db.session.add(skunky)

db.session.commit()
