from typing import List

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import relationship

Base: DeclarativeMeta = declarative_base()


class ColourFamily(Base):
    __tablename__ = 'colour_families'

    colour_family_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(Text, nullable=False)

    colours: List['Colour'] = relationship('Colour', backref='colour_family', uselist=True)


class Colour(Base):
    __tablename__ = 'colours'

    colour_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    lego_id = Column(Integer, nullable=False)
    name = Column(Text, nullable=False)
    red = Column(Integer, nullable=False)
    green = Column(Integer, nullable=False)
    blue = Column(Integer, nullable=False)
    colour_family_id = Column(Integer, ForeignKey(ColourFamily.colour_family_id), nullable=False)

    bricks: List['Brick'] = relationship('Brick', backref='colour', uselist=True)


class Brick(Base):
    __tablename__ = 'bricks'

    brick_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(Text, nullable=False)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    colour_id = Column(Integer, ForeignKey(Colour.colour_id), nullable=False)
