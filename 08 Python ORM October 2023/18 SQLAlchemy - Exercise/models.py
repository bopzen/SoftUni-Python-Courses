from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
from main import engine

Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String, nullable=False)
    ingredients = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)
    chef_id = Column(Integer, ForeignKey('chefs.id'), nullable=False)
    chef = relationship('Chef', back_populates='recipes')


class Chef(Base):
    __tablename__ = 'chefs'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String, nullable=False)
    recipes = relationship('Recipe', back_populates='chef')



Base.metadata.create_all(engine)