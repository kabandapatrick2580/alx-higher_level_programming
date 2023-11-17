#!/usr/bin/python3
"""
This script connects to Mysql database and retirieves information about cities
from the 'cities' table based on a specific state name. The script expects four
command-line arguments

Usage:
    ./script.py <username <password> <database> <state_name>

Arguments:
    usernmae: MySQL username
    password: MySQL Password
    database: MySQL database name

Example:
    ./script.py root secret mydatabase California
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # scheck if all the required command-lines are there
    if len(sys.argv) != 5:
        print("Usage: {} <user> <pwd> <Db> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # get command-line arguments
    username, password, database, state = sys.argv[1:5]

    try:
        # connect to the MySQL SERVER
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
            )
        cursor = db.cursor()

        # Sthe SQL cmd with param'tized qury to filter the states by name
        command = "SELECT name FROM cities WHERE state_id = (SELECT id FROM states WHERE name LIKE %s)"

        # Execute the SQL Query with the parameter
        cursor.execute(command, (state,))

        # Fetch all the results
        results = cursor.fetchall()

        # Display the results
        cities = ' ,'.join(row[0] for row in results)
        print(cities)

    except MySQLdb.Error as err:
        # handle any MySQL database errors and print an error message
        print("MySql Error:", err)

    finally:
        # ensure that the database is closed, whether or not an
        # error occured
        if 'db' in locals():
            db.close()
