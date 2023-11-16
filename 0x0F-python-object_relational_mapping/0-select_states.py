#!/usr/bin/python3
import MySQLdb
import sys
# Check if all required command-line arguments are provided
if len(sys.argv) != 4:
    sys.exit(1)

# Get command-line arguments
username, password, database = sys.argv[1:4]

db = MySQLdb.connect(host="localhost", user="root", passwd="Bijdad@1234", db="hbtn_0e_0_usa", port=3306)

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id ASC")

results = cursor.fetchall()

for row in results:
    print(row)

db.close()