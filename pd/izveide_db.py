import sqlite3
DB = 'students.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS studijas (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               vards TEXT NOT NULL,
               kurs TEXT NOT NULL,
               kredits INTEGER NOT NULL
               )
''')
conn.commit()
conn.close()
print('Tabula Studijas izveidota')