import sqlite3
from tg2 import PROVODKI, PLAN
from fuzzywuzzy import fuzz

db = sqlite3.connect('ID.db', check_same_thread = False)
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS wiring (wir TEXT)""")
db.commit()
c = 0

sql.execute("""CREATE TABLE IF NOT EXISTS plan (pl TEXT)""")
db.commit()


for i in PROVODKI:
    sql.execute(f"SELECT wir FROM wiring WHERE wir = '{i}' ")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO wiring VALUES (?)", (i,))
        db.commit()
        c += 1
        print(f'Itera{c}')

print(len(PROVODKI))
b = 0
for user in sql.execute("SELECT wir FROM wiring"):
    print(user)
    b += 1
print(b)
p=0
for i in PLAN:
    sql.execute(f"SELECT pl FROM plan WHERE pl='{i}'")
    if sql.fetchone() is None:
        sql.execute("INSERT INTO plan VALUES (?)", (i,))
        db.commit()
        p += 1

        print(f'yg{p}')
print(len(PLAN))
for pll in sql.execute("SELECT pl FROM plan"):
    print(pll)


