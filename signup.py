from customtkinter import *
import customtkinter as ctk
from PIL import Image

app = ctk.CTk()
app.title('Signup page')
app.geometry("750x480")
app.resizable(0,0)

sideimg = Image.open('3.jpeg')
emailimg= Image.open('emailimage.jpeg')
passimg = Image.open('passwordimage.jpeg')

sideimage=CTkImage(dark_image=sideimg, light_image=sideimg, size=(446,490))
emailimage = CTkImage(dark_image=emailimg, light_image=emailimg, size=(20,20))
passimage = CTkImage(dark_image=passimg, light_image=passimg, size=(17,17))

CTkLabel(master=app, text='', image=sideimage).pack(expand=True, side='right')

frame= CTkFrame(master=app, width=300, height=480, fg_color='#ffffff')
frame.pack_propagate(0)
frame.pack(expand=True, side='left')

label1 = CTkLabel(master=frame, text='Create your Account', text_color='#0b2f4f', anchor='w', justify='left', font=('Arial Bold', 24))
label1.pack(anchor='w', pady=(50,0), padx=(25,0))

label3 = CTkLabel(master=frame, text='E-Mail:', text_color='#0b2f4f', anchor='w', justify='left', font=('Arial Bold', 14), image=emailimage, compound='left')
label3.pack(anchor='w', pady=(38,0), padx=(25,0))
entry1 = CTkEntry(master=frame, width=225,fg_color='#EEEEEE', border_color='#517BF4', border_width=1, text_color='#000000', placeholder_text='Enter your email address', corner_radius=14)
entry1.pack(anchor='w', padx=(25,0))

label4 = CTkLabel(master=frame, text='Password:', text_color='#0b2f4f', anchor='w', justify='left', font=('Arial Bold', 14), image=passimage, compound='left')
label4.pack(anchor='w', pady=(21,0), padx=(25,0))
entry2 = CTkEntry(master=frame, width=225, fg_color='#EEEEEE', border_color='#517BF4', border_width=1, text_color='#000000', placeholder_text='Enter your password',show='*', corner_radius=14)
entry2.pack(anchor='w', padx=(25,0))
label5 = CTkLabel(master=frame, text='Confirm password:', text_color='#0b2f4f', anchor='w', justify='left', font=('Arial Bold', 14), image=passimage, compound='left')
label5.pack(anchor='w', pady=(21,0), padx=(25,0))
entry3 = CTkEntry(master=frame, width=225, fg_color='#EEEEEE', border_color='#517BF4', border_width=1, text_color='#000000', placeholder_text='Confirm password',show='*', corner_radius=14)
entry3.pack(anchor='w', padx=(25,0))

button1 = CTkButton(master=frame, text='SIGNUP', fg_color='#517BF4', hover_color='#001222', font=('Arial Bold', 12), text_color='#ffffff', width=225, corner_radius=14)
button1.pack(anchor='w', pady=(40,0), padx=(25,0))

app.mainloop()

