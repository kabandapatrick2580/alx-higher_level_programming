#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves a list of states
from the 'states' table, ordering them by ID in ascending order.

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
from sys import argv

if __name__ == '__main__':
    # Check if all required command-line arguments are provided
    if len(argv) != 4:
        exit(1)

    # Get command-line arguments
    username, password, database = argv[1:4]

    try:
        db = MySQLdb.connect(
                host="localhost",
                user=argv[1],
                passwd=argv[2],
                db=argv[3],
                port=3306
                )
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        results = cursor.fetchall()

        for row in results:
            print(row)

    except MySQLdb.Error as err:
        # Handle any MySQL database errors and print an error message
        print("Error:", err)

    finally:
        # Ensure that the database connection is closed, whether or not an
        # error occurred
        if 'db' in locals():
            db.close()
