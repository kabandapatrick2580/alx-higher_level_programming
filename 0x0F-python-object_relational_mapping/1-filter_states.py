#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves a list of states
from the 'states' table,  whose name
starts with 'N'. The script assumes three command-line arguments:
MySQL username, MySQL password, and MySQL database name.

Usage:
    ./script.py <username> <password> <database>

Arguments:
    username: MySQL username
    password: MySQL password
    database: MySQL database name

Example:
    ./script.py root secret mydatabase
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Check if all required command-line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get command-line arguments
    username, password, database = sys.argv[1:4]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
        cursor = db.cursor()

        # Execute the SQL query to select states starting with 'N'
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")

        # Fetch all the results
        results = cursor.fetchall()

        # Display the results
        for row in results:
            print(row)

    except MySQLdb.Error as err:
        # Handle any MySQL database errors and print an error message
        print("MySQL Error:", err)

    finally:
        # Ensure that the database connection is closed, whether or not an
        # error occurred
        if 'db' in locals():
            db.close()
