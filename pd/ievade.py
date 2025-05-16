import sqlite3
DB = 'students.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
dati = []
for i in range(5):
    print(f'\nIevadi {i+1}. ierakstu:')
    vards = input('Vārds: ')
    kurs = input('Kurss: ')
    kredits = int(input('Kredīts: '))
    dati.append((vards, kurs, kredits))
cursor.executemany('''
    INSERT INTO studijas (vards, kurs, kredits)
    VALUES (?, ?, ?)               
''', dati)
conn.commit()
conn.close()
print('Tika pievienoti 5 ieraksti.')