import MySQLdb
db = MySQLdb.connect(host="localhost", user="patrick", passwd="Bijdad@1234", db="hbtn_0e_0_usa", port=3306)

cursor = db.cursor()

cursor.execute("SELECT * FROM states")

results = cursor.fetchall()

for row in results:
    print(row)

db.close()