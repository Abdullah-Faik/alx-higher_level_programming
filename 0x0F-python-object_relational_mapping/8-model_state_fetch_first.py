#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
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

    first_state = session.query(State).order_by(State.id).first()

    print(
        f'{first_state.id}: {first_state.name}' if first_state is not None
        else 'Nothing'
    )

    session.close()
