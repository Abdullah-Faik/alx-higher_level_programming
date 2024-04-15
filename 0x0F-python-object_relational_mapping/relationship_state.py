#!/usr/bin/python3
"""
Contains the class definition of a State and
an instance Base = declarative_base()
"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


class State(Base):
    """
    The definition os State class.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City',
        cascade='all, delete',
        backref='state'
    )
