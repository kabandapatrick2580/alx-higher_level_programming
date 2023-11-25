#!/usr/bin/python3
"""
thescript to list all State objects containing the letter 'a' from
the database hbtn_0e_6_usa using SQLAlchemy.

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


def filter_states_by_letter(username, password, database):
    """
    Filter all State objects containing the letter 'a' from the database.

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

        # Query and fetch all State objects containing 'a', sorted by id
        states_with_a = session.query(State).filter(
                State.name.like('%a%')).order_by(State.id).all()

        # Iterate through the results and print each State object
        for state in states_with_a:
            print(f'{state.id}: {state.name}')

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

    # Call the list_states_with_letter_a function with the provided arguments
    filter_states_by_letter(username, password, database)
