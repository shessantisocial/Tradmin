import sqlite3


# Create a connection to the SQLite database
# This will create the database file 'user_data.db' if it doesn't exist
conn = sqlite3.connect('user_data.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store user data if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

def signup_user():
    email = entry1.get()
    password = entry2.get()
    confirm_password = entry3.get()

    if password == confirm_password:
        try:
            conn = sqlite3.connect('user_data.db')
            cursor = conn.cursor()

            # Insert user data into the database
            cursor.execute('''
            INSERT INTO users (email, password) VALUES (?, ?)
            ''', (email, password))

            conn.commit()
            conn.close()

            # Show success message or redirect to login page
            CTkMessagebox.show_info("Signup Success", "Your account has been created successfully!")
            open_login()

        except sqlite3.IntegrityError:
            CTkMessagebox.show_error("Signup Error", "Email already exists. Please use a different email.")

    else:
        CTkMessagebox.show_error("Signup Error", "Passwords do not match.")


def login_user():
    email = entry1.get()
    password = entry2.get()

    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Check if the user exists in the database
    cursor.execute('''
    SELECT * FROM users WHERE email = ? AND password = ?
    ''', (email, password))

    user = cursor.fetchone()
    conn.close()

    if user:
        # Login successful, show success message or redirect to another page
        CTkMessagebox.show_info("Login Success", f"Welcome {email}!")
    else:
        # Login failed, show error message
        CTkMessagebox.show_error("Login Error", "Invalid email or password. Please try again.")


button1 = CTkButton(master=frame, text='LOGIN', fg_color='#517BF4', hover_color='#001222', font=('Arial Bold', 12), text_color='#ffffff', width=225, command=login_user)


button1 = CTkButton(master=frame, text='SIGNUP', fg_color='#517BF4', hover_color='#001222', font=('Arial Bold', 12), text_color='#ffffff', width=225, corner_radius=14, command=signup_user)
