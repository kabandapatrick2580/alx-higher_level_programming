#!/usr/bin/python3
"""
A script to change the name of a State object in the database hbtn_0e_6_usa
using SQLAlchemy.

Usage:
    python script.py <username> <password> <database>

Arguments:
    <username>: MySQL username for database access.
    <password>: MySQL password for database access.
    <database>: Name of the MySQL database to connect to.

The script connects to a MySQL server running on localhost at port 3306,
changes the name of the State object with id=2 to "New Mexico".
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def rename_state(username, password, database):
    """
    Rename the State object with id=2 to "New Mexico".

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

        # Query and fetch the State object with id=2
        updated_state = session.query(State).filter_by(id=2).first()

        if updated_state:
            # Update the name of the State object
            updated_state.name = "New Mexico"
            session.commit()
        else:
            # Print an error message if the State object is not found
            print("State with id=2 not found")

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

    # Call the change_state_name function with the provided arguments
    rename_state(username, password, database)
