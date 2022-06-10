"""Seed file to make sample data for db."""


from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Make sample Pets
Pet.query.delete()

lucky = Pet(name='Lucky', species='Dog', 
photo_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/labrador-puppy-royalty-free-image-1626252338.jpg?crop=0.667xw:1.00xh;0.173xw,0&resize=640:*')

spot = Pet(name='Spot', species='Dog', 
photo_url='https://thehappypuppysite.com/wp-content/uploads/2015/09/The-Siberian-Husky-HP-long.jpg', age=1)

ralph = Pet(name='Ralph', species='Cat', 
photo_url='https://images.unsplash.com/photo-1595433707802-6b2626ef1c91?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1yZWxhdGVkfDN8fHxlbnwwfHx8fA%3D%3D&w=1000&q=80', age=1)

spikey = Pet(name='Spikey', species='Porcupine', 
photo_url='https://ymcagbw.org/sites/default/files/styles/node_blog/public/2020-03/porcupine.jpg.webp?itok=qfWuotpv', notes='Needs a haircut!')


db.session.add_all([lucky,spot,ralph,spikey])
db.session.commit()
