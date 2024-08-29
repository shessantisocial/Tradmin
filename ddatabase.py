import sqlite3
import bcrypt

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

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cursor.execute('''
    INSERT INTO users (email, password) VALUES (?, ?)
    ''', (email, hashed_password))

    conn.commit()
    conn.close()

def check_user(email, password):
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM users WHERE email = ?
    ''', (email,))

    user = cursor.fetchone()
    conn.close()

    if user:
        hashed_password = user
        if bcrypt.checkpw(password.encode(), hashed_password):
            return True
    return False