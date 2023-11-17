#!/usr/bin/python3
import MySQLdb
import sys
# Check if all required command-line arguments are provided
if len(sys.argv) != 4:
    sys.exit(1)

# Get command-line arguments
username, password, database = sys.argv[1:4]


try:
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
    cursor = db.cursor()

    query = ("SELECT cities.id, cities.name AS city_name, states.name AS state_name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id;")
    # Execute the SQL query
    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results with the desired format
    for row in results:
        print(row)

except MySQLdb.Error as e:
    print("MySQL Error: {}".format(e))

finally:
    # Close the database connection
    if 'db' in locals() and db:
        db.close()
