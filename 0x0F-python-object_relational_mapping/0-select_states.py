#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ =='__main__':
   
    db = MySQLdb.connect(
        host="localhost", user= argv[1], passwd=argv[2], 
        db=argv[3], port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    results = cursor.fetchall()

    for row in results:
        print(row)

    db.close()