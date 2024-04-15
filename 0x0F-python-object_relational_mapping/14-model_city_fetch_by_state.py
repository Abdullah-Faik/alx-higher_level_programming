#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    session = Session(engine)

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')

    session.commit()
    session.close()
