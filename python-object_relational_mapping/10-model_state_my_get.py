#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Capture the command-line arguments
    MYSQL_USERNAME = sys.argv[1]
    MYSQL_PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]
    STATE_NAME = sys.argv[4]

    # Create the engine and bind it to the metadata of the Base class
    engine = create_engine(
        f'mysql+mysqldb://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@localhost/'
        f'{DATABASE_NAME}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()

    # Query the database for the state
    state = session.query(State).filter(State.name == STATE_NAME).first()

    # Print the result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
