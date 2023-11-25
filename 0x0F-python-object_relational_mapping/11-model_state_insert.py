#!/usr/bin/python3
"""
A script to insert the State object "Louisiana" into the
database hbtn_0e_6_usa using SQLAlchemy.

Usage:
    python script.py <username> <password> <database>

Arguments:
    <username>: MySQL username for database access.
    <password>: MySQL password for database access.
    <database>: Name of the MySQL database to connect to.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def insert_state_record(username, password, database):
    """
    Insert the State object "Louisiana" into the database and print its
    states.id.

    Args:
        username (str): MySQL username for database access.
        password (str): MySQL password for database access.
        database (str): Name of the MySQL database to connect to.
    """
    try:
        # Create a database engine and establish a connection
        engine = create_engine(
                f'mysql://{username}:{password}@localhost:3306/{database}')

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create a new State object for Louisiana
        newstate = State(name="Louisiana")

        # Add the new State object to the database
        session.add(newstate)
        session.commit()

        # Print the id of the newly created State object
        print(newstate.id)

    except Exception as e:
        # Handle any errors and print an error message
        print(f"Error: {e}")

    finally:
        # Close the session and the database connection
        if 'session' in locals():
            session.close()


if __name__ == "__main__":
    # Check for the correct number of command-line arguments (3)
    import sys

    if len(sys.argv) != 4:
        print(
            "Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the command-line arguments
    username, password, database = sys.argv[1:4]

    # Call the insert_state_record function with the provided arguments
    insert_state_record(username, password, database)
