import sqlite3 as sql3

con = sql3.connect('./data/data.sql')

query = 'SELECT * FROM data WHERE No1 > 104 and No2 < 108'

res = con.execute(query).fetchall()

print(res[:5])

print(len(res))

con.close()