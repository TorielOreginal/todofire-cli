import sqlite3
import sys

db = sqlite3.connect('todo.db')
c = db.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS todos(
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        done BOOLEAN
    )
''')

while True:
    opr = input('>> ')

    if opr == 'list':
        c.execute('SELECT * FROM todos')
        print(c.fetchall())
    if opr == 'show':
        id = input('Input the todo id: ')
        c.execute('SELECT * FROM todos WHERE id=?', id)
        print(c.fetchall())
    if opr == 'new':
        name = input('Input the todo name: ')
        c.execute('''
            INSERT INTO todos (name, done) VALUES(
                ?,
                ?
            )
        ''', (name, 'FALSE'))
    if opr == 'delete':
        id = input('Input the todo id: ')
        c.execute('DELETE FROM todos WHERE id=?', id)
    if opr == 'done':
        id = input('Input the todo id: ')
        c.execute('UPDATE todos SET done=? WHERE id=?', ('TRUE', id))
    if opr == 'exit':
        db.commit()
        db.close()
        sys.exit(0)
