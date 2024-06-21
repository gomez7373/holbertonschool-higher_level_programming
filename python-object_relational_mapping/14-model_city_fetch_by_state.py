#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Capture the command-line arguments
    MYSQL_USERNAME = sys.argv[1]
    MYSQL_PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]

    # Create the engine and bind it to the metadata of the Base class
    engine = create_engine(f'mysql+mysqldb://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@localhost/{DATABASE_NAME}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()

    # Query all City objects and sort them by cities.id
    cities = session.query(City).join(State).order_by(City.id).all()

    # Print the results
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

