#!/usr/bin/python3
"""
A script to print the State object with the name passed as an
argument from the database hbtn_0e_6_usa using SQLAlchemy.

Usage:
    python script.py <username> <password> <database> <state_name>

Arguments:
    <username>: MySQL username for database access.
    <password>: MySQL password for database access.
    <database>: Name of the MySQL database to connect to.
    <state_name>: Name of the state to search for.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def find_state_id_by_name(username, password, database, state_name):
    """
    Find and print the State ID by state name from the database.

    Args:
        username (str): MySQL username for database access.
        password (str): MySQL password for database access.
        database (str): Name of the MySQL database to connect to.
        state_name (str): Name of the state to search for.
    """
    try:
        # Create a database engine and establish a connection
        engine = create_engine(
                f'mysql://{username}:{password}@localhost:3306/{database}')

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query and fetch the State object with the provided state name
        state = session.query(State).filter_by(name=state_name).first()

        if state:
            # Print the id of the State object
            print(state.id)
        else:
            # Print 'Not found' if no state matches the search criteria
            print('Not found')

    except Exception as e:
        # Handle any errors and print an error message
        print(f"Error: {e}")

    finally:
        # Close the session and the database connection
        if 'session' in locals():
            session.close()


if __name__ == "__main__":
    # Check for the correct number of command-line arguments (4)
    import sys

    if len(sys.argv) != 5:
        print("Usage: {} <username> <password>"
              "<database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the command-line arguments
    username, password, database, state_name = sys.argv[1:5]

    # Call the find_state_id_by_name function with the provided arguments
    find_state_id_by_name(username, password, database, state_name)
