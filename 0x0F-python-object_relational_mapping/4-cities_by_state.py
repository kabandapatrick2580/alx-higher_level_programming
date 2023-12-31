#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves information about cities,
including their IDs, names, and the corresponding state names from the 'cities'
and 'states' tables. The script expects three command-line arguments: MySQL
username, MySQL password, and MySQL database name.

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

        # Construct the SQL query to retrieve city information with a JOIN operation
        query = """
            SELECT cities.id, cities.name AS city_name, states.name AS state_name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id;
        """

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the results
        results = cursor.fetchall()

        # Display the results with the desired format
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        # Handle any MySQL database errors and print an error message
        print("MySQL Error: {}".format(e))

    finally:
        # Close the database connection
        if 'db' in locals() and db:
            db.close()
