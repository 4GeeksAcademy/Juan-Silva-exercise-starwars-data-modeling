import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)

class Planets(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    climate = Column(String(80), nullable=False)  
    description = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    name = Column(String(80), nullable=False)
    orbital_period = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    terrain = Column(String(80), nullable=False)  

class Characters (Base):
    __tablename__='characters'
    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=False)
    gender = Column(String(60), nullable=False)
    mass = Column(Integer, nullable=False) 
    name = Column(String(60), nullable=False)   

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
