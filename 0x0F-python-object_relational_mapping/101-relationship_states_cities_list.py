#!/usr/bin/python3
"""
A script that lists all State objects and corresponding City objects from the
database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def display_states_and_cities(username, password, database):
    """
    List all State objects and their corresponding City objects from the
    database.

    Args:
        username (str): MySQL username for database access.
        password (str): MySQL password for database access.
        database (str): Name of the MySQL database to connect to.
    """
    try:
        # Create a database engine and establish a connection
        engine = create_engine(
                f'mysql://{username}:{password}@localhost:3306/{database}')

        # Create all tables defined in the Base
        Base.metadata.create_all(engine)

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the database to get all State objects and their
        # corresponding City objects
        states = session.query(State).order_by(State.id, City.id).all()

        # Iterate through the results and print each State and its City objects
        for state in states:
            print(f"{state.name}:")
            for city in state.cities:
                print(f"    {city.id}: {city.name}")

    except Exception as e:
        # Handle any errors and print an error message
        print(f"Error: {e}")

    finally:
        # Close the session and the database connection
        if 'session' in locals():
            session.close()


if __name__ == "__main__":
    # Check for the correct number of command-line arguments (3)
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the command-line arguments
    username, password, database = sys.argv[1:4]

    # Call the list_states_and_cities function with the provided arguments
    display_states_and_cities(username, password, database)
