import sqlite3
conn= sqlite3.connect("celebrities.db")
cursor =conn.cursor()
## creating a table

sql1 = "create table celebs(celebID integer PRIMARY KEY, firstname text, lastname text, age integer, email text, photo text, bio text)"
cursor.execute(sql1)

sql = "create table members(memberID integer PRIMARY KEY, firstname text, lastname text, age integer, email text, bio text)"
cursor.execute(sql)

login="create table member_login(memberID integer PRIMARY KEY, username text, password text)"
cursor.execute(login)

conn.commit()
conn.close
