import sqlite3

def createdatabase():
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

def insert_user(email, password):
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO users (email, password) VALUES (?, ?)
    ''', (email, password))

    conn.commit()
    conn.close()

def check_user(email, password):
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM users WHERE email = ?
    ''', (email,))

    user = cursor.fetchone()
    if user and user[2] == password:  # user[2] refers to the 'password' field
        return True
    return False

    conn.close()




    # if user:
    #     hashed_password = user
    #     if bcrypt.checkpw(password.encode(), hashed_password):
    #         return True
    # return False