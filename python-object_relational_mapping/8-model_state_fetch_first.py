#!/usr/bin/python3
"""
This script prints the first State object from the database hbtn_0e_6_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
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

    # Connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@localhost/{DATABASE_NAME}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first state
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
