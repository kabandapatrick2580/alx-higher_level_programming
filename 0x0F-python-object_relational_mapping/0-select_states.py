#!/usr/bin/python3
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
                host="localhost", user=argv[1], passwd=argv[2],
                db=argv[3], port=3306)

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