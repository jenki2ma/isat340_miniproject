import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor= conn.cursor()
# select statement

sql1 = "select * from celebs"
cursor. execute(sql1)

# getting rows
rows = cursor.fetchall()

#printing

for row in rows:
    print(row)
    

sql = "select * from members"
cursor. execute(sql)
# getting rows
rows = cursor.fetchall()

#printing

for row in rows:
    print(row)
    conn.close
