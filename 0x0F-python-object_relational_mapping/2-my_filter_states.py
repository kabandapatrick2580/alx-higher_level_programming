#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves a list of states
from the 'states' table based on a partial match of the state name.
The script expects four command-line arguments: MySQL username, MySQL password,
MySQL database name, and the partial name of the state.

Usage:
    ./script.py <username> <password> <database> <state>

Arguments:
    username: MySQL username
    password: MySQL password
    database: MySQL database name
    state: Partial name of the state for filtering

Example:
    ./script.py root secret mydatabase New
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Check if all required command-line arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <pwd> <Db> <state>".format(sys.argv[0]))
        sys.exit(1)

    # Get command-line arguments
    username, pwd, Db, state = sys.argv[1:5]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
                host="localhost",
                user=username,
                passwd=pwd,
                db=Db,
                port=3306
                )
        cursor = db.cursor()

        # Construct the SQL command with a LIKE clause to filter states by name
        command = "SELECT * FROM states WHERE name LIKE '{}'".format(state)

        # Execute the SQL query
        cursor.execute(command)

        # Fetch all the results
        results = cursor.fetchall()

        # Display the results
        for row in results:
            print(row)
        db.close()
    except MySQLdb.Error as err:
        # Handle any MySQL database errors and print an error message
        print("MySQL Error:", err)

    finally:
        # Ensure that the database connection is closed, whether or not an
        # error occurred
        if 'db' in locals():
            db.close()
