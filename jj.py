from customtkinter import *
import customtkinter as ctk
import sqlite3
import bcrypt

app = ctk.CTk()
app.title('Login')
app.geometry('456x360')
app.config(bg='#001220')

font1 = ('Helvetica', 25, 'Bold')
font2 = ('Arial', 17, 'Bold')
font3 = ('Arial', 13, 'Bold')
font4 = ('Arial', 14, 'Bold', 'underline')

c = sqlite3.connect('data.db')
cursor = c.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                   email TEXT NOT NULL UNIQUE,
                   password TEXT NOT NULL)''')

frame1 = ctk.CTkFrame(master=app, bg_color='#001220', fg_color='#001220', width=470, height=360)
frame1.place(x=0, y=0)

sideimg = ImageTk.PhotoImage(file='sideimage.jpeg')
sideimglabel = Label(frame1, image=sideimg, bg='#001220')
sideimglabel.place(x=0, y=0)

app.mainloop()