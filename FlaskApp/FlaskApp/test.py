import sqlite3

conn = sqlite3.connect("sample.db")
cur = conn.cursor()
cur.execute("INSERT INTO test_table(test_column) VALUES('TEST')")
conn.commit()
conn.close()
