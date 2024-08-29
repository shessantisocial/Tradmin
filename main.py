import sqlite3

con = sqlite3.connect('bus.db')

c = con.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user
           (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                email TEXT,
                password TEXT
           )
        ''')

# c = con.execute("INSERT INTO user_reg (username, email) VALUES (?,?)", (username, email))

def user_reg(username,
             email,
             password):
    c.execute(
        "INSERT INTO user_reg (username, email, password) VALUES (?,?,?)",
          (username,
            email,
            password)
    )
    con.commit()
    return "New user created successfully"

def get_all():
    c.execute("SELECT * FROM user")
    rows = c.fetchall()
    return rows

def get_by_id(username):
    c.execute("SELECT * FROM user WHERE username=?", (username,))
    row = c.fetchone()
    return row

def update(id,
           username,
           email,
           password):
    c.execute("UPDATE user SET username=?, email=?, password=? WHERE id=?",
              username,
              email,
              password,
              id  )
    return "User successfully updated."
    
def delete(username):
    c.execute("DELETE FROM user WHERE username=?", (username,))
    con.commit()
    return "User has been deleted successfully."