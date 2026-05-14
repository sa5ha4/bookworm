import sqlite3

def savienot():
    conn = sqlite3.connect('biblioteka.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gramatas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nosaukums TEXT,
            autors TEXT,
            gads INTEGER
        )
    ''')
    conn.commit()
    return conn, cursor

def start_pievienot(cursor, conn):
    cursor.execute('INSERT INTO gramatas (nosaukums, autors, gads) VALUES ("The Institute", "Stephen King", "2019")')
    cursor.execute('INSERT INTO gramatas (nosaukums, autors, gads) VALUES ("Dracula", "Bram Stoker", "1897")')
    cursor.execute('INSERT INTO gramatas (nosaukums, autors, gads) VALUES ("The Mystery of the Sea", "Bram Stoker", "1902")')
    cursor.execute('INSERT INTO gramatas (nosaukums, autors, gads) VALUES ("Under the Dome", "Stephen King", "2009")')
    cursor.execute('INSERT INTO gramatas (nosaukums, autors, gads) VALUES ("In the Vault", "Howard Phillips Lovecraft", "1925")')
    conn.commit()

def pievienot(cursor, conn, nosaukums, autors, gads):
    cursor.execute('INSERT INTO gramatas (nosaukums, autors, gads) VALUES (?, ?, ?)',
                    (nosaukums, autors, gads))
    conn.commit()
    print(f"{nosaukums} pievienots!")

def apskatit(cursor):
    cursor.execute('SELECT * FROM gramatas')
    gramatas = cursor.fetchall()
    if not gramatas:
        print('Nav nevienas grāmatas.')
    for k in gramatas:
        print(f'ID: {k[0]} | Nosaukums: {k[1]} | Autors: {k[2]} | Gads: {k[3]}')

def atrast(cursor, autors):
    cursor.execute('SELECT * FROM gramatas WHERE autors = ?',
                   (autors,))
    
    gramata = cursor.fetchall()
    if not gramata:
        print("Nav grāmatas no šī autora")
    else:
        for k in gramata:
            print(f'ID: {k[0]} | Nosaukums: {k[1]} | Autors: {k[2]} | Gads: {k[3]}')

def dzest(cursor, conn, gramatas_id):
    cursor.execute('DELETE FROM gramatas WHERE id = ?', (gramatas_id,))
    conn.commit()
    print('Gramata dzēsta!')

def karto(cursor):
    cursor.execute('SELECT * FROM gramatas ORDER BY gads')
    gramatas = cursor.fetchall()
    for k in gramatas:
        print(f'ID: {k[0]} | Nosaukums: {k[1]} | Autors: {k[2]} | Gads: {k[3]}')

def pec_2000(cursor):
    cursor.execute('SELECT * FROM gramatas WHERE gads > 2000')
    gramatas = cursor.fetchall()
    for k in gramatas:
        print(f'ID: {k[0]} | Nosaukums: {k[1]} | Autors: {k[2]} | Gads: {k[3]}')

conn, cursor = savienot()
#start_pievienot(cursor, conn)

while True:
    print('\n1. Pievienot gramātu')
    print('2. Apskatīt visus')
    print('3. Dzest')
    print('4. Atrast')
    print('5. Izkārtots saraksts')
    print('6. Izdotas pēc 2000. gada')
    print('7. Iziet')
    izvele = input('Izvēlies: ')

    if izvele == '1':
        n = input('Nosaukums: ')
        a = input('Autors: ')
        g = input('Gads:')
        pievienot(cursor, conn, n, a, g)
    elif izvele == '2':
        apskatit(cursor)
    elif izvele == '3':
        i = int(input('Grāmatas ID: '))
        dzest(cursor, conn, i)
    elif izvele == '4':
        a = input('Autors: ')
        atrast(cursor, a)
    elif izvele == '5':
        karto(cursor)
    elif izvele == '6':
        pec_2000(cursor)
    elif izvele == '7':
        break

conn.close()
