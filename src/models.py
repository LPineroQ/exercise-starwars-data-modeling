import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    email = Column(String(250), nullable=False)
    nickname = Column(String(120), nullable=False)

class Post(Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    img = Column(String(300))
    comment = Column(String(300))
    user_id = Column(Integer, ForeignKey('user.id'))
    relationship(User)

class Planets(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    description = Column(String(500))
    url = Column(String(200))
    surface_water = Column(Integer)
    terrain = Column(String(120))
    climate = Column(String(120))
    population = Column(Integer)
    gravity = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)

class People(Base):
    __tablename__= 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    description = Column(String(300))
    url = Column(String(120))
    homeworld = Column(String(120))
    gender = Column(String(50))
    birth_year = Column(Integer)
    eye_color = Column(String(120))
    skin_color = Column(String(120))
    hair_color = Column(String(120))
    mass = Column(Integer)
    height = Column(Integer)

class Vehicles(Base):
    __tablename__= 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    description = Column(String(300))
    url = Column(String(120))
    model = Column(String(120))
    starship_class = Column(String(120))
    manufacturer = Column(String(120))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    hyperdrive_rating = Column(Integer)
    MGLT = Column(Integer)
    cargo_capacities = Column(Integer)
    consumables = Column(Integer)
    pilots = Column(String(120))

class favorites(Base):
    __tablename__= 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    Planet_id= Column(Integer, ForeignKey('planets.id'), nullable=True)
    People_id= Column(Integer, ForeignKey('people.id'), nullable=True)
    Vehicles_id= Column(Integer, ForeignKey('vehicles.id'), nullable=True)




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')