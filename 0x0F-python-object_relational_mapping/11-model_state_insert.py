#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    session = Session(engine)

    state = State()
    state.name = 'Louisiana'

    session.add(state)
    session.commit()

    print(state.id)

    session.close()
