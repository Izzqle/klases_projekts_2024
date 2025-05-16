import sqlite3
DB = 'students.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
cursor.execute('''
    SELECT id, vards, kurs, kredits FROM studijas
    ORDER BY kredits DESC
    LIMIT 3
''')
top3 = cursor.fetchall()
conn.close()
if top3:
    print('TOP3 rezultāti:')
    for id_,vards, kurs, kredits in top3:
        print(f'{id_}   {vards} {kurs} - {kredits}')
else:
    print('Nav rezultātu.')