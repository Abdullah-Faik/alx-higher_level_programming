#!/usr/bin/python3
"""
creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    session = Session(engine)

    state = State()
    state.name = 'California'

    session.add(state)
    session.commit()

    city = City()
    city.name = 'San Francisco'
    city.state_id = state.id

    session.add(city)
    session.commit()

    session.close()
