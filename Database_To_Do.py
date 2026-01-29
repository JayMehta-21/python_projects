import sqlite3
file="database_todo.db"

def create_table():
    conn=sqlite3.connect(file)
    cursor=conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS TASKS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                TASK TEXT NOT NULL
                )
    ''')
    conn.commit()
    conn.close()
create_table()