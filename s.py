from customtkinter import *
import customtkinter as ctk
from PIL import Image

def opensignup():
    loginscreen.destroy()
    signupapp()

def loginapp():
    global loginscreen
    loginscreen = ctk.CTk()
    loginscreen.title('Login page')
    loginscreen.geometry("600x480")
    loginscreen.resizable(0,0)

    sideimg = Image.open('1.jpeg')
    emailimg= Image.open('emailimage.jpeg')
    passimg = Image.open('passwordimage.jpeg')
    googleimg = Image.open('googleimage.jpeg')

    sideimage=CTkImage(dark_image=sideimg, light_image=sideimg, size=(300,480))
    emailimage = CTkImage(dark_image=emailimg, light_image=emailimg, size=(20,20))
    passimage = CTkImage(dark_image=passimg, light_image=passimg, size=(17,17))
    googleimage= CTkImage(dark_image=googleimg, light_image=googleimg, size=(17,17))

    CTkLabel(master=loginscreen, text='', image=sideimage).pack(expand=True, side='left') 

    frame= CTkFrame(master=loginscreen, width=300, height=480, fg_color='#ffffff')
    frame.pack_propagate(0)
    frame.pack(expand=True, side='right')

    label1 = CTkLabel(master=frame, text='Welcome Back!', text_color='#0b2f4f', anchor='w', justify='left', font=('Arial Bold', 24))
    label1.pack(anchor='w', pady=(50,0), padx=(25,0))
    label2 = CTkLabel(master=frame, text='Sign in to continue', font=('Arial', 12), justify='left', text_color='#7E7E7E', anchor='w')
    label2.pack(anchor='w', padx=(25,0))

    label3 = CTkLabel(master=frame, text='E-Mail:', text_color='#0b2f4f', anchor='w', justify='left', font=('Arial Bold', 14), image=emailimage, compound='left')
    label3.pack(anchor='w', pady=(38,0), padx=(25,0))
    entry1 = CTkEntry(master=frame, width=225,fg_color='#EEEEEE', border_color='#517BF4', border_width=1, text_color='#000000', placeholder_text='glory@gmail.com')
    entry1.pack(anchor='w', padx=(25,0))

    label4 = CTkLabel(master=frame, text='Password:', text_color='#001222', anchor='w', justify='left', font=('Arial Bold', 14), image=passimage, compound='left')
    label4.pack(anchor='w', pady=(21,0), padx=(25,0))
    entry2 = CTkEntry(master=frame, width=225, fg_color='#EEEEEE', border_color='#517BF4', border_width=1, text_color='#000000', show='*')
    entry2.pack(anchor='w', padx=(25,0))

    button1 = CTkButton(master=frame, text='LOGIN', fg_color='#517BF4', hover_color='#001222', font=('Arial Bold', 12), text_color='#ffffff', width=225)
    button1.pack(anchor='w', pady=(40,0), padx=(25,0))
    button2 = CTkButton(master=frame, text='Continue With Google', fg_color='#EEEEEE', hover_color='#EEEEEE', font=('Arial Bold', 9), text_color='#517BF4', width=225, image=googleimage)
    button2.pack(anchor='w', pady=(20,0), padx=(25,0))

    signupbutton = CTkButton(master=frame, text="Don't have an account? Sign up", fg_color='#FFFFFF', hover_color='#FFFFFF',font=('Arial bold', 9), text_color='#517BF4', width=225, command=opensignup)
    signupbutton.pack(anchor='w', pady=(20,0), padx=(25,0))

    loginscreen.mainloop()


from customtkinter import *
import customtkinter as ctk
from PIL import Image

def openlogin():
    signupscreen.destroy()
    loginapp()

def signupapp():
    global signupscreen
    signupscreen = ctk.CTk()
    signupscreen.title('Signup page')
    signupscreen.geometry("750x480")
    signupscreen.resizable(0,0)

    sideimg = Image.open('3.jpeg')
    emailimg= Image.open('emailimage.jpeg')
    passimg = Image.open('passwordimage.jpeg')

    sideimage=CTkImage(dark_image=sideimg, light_image=sideimg, size=(446,490))
    emailimage = CTkImage(dark_image=emailimg, light_image=emailimg, size=(20,20))
    passimage = CTkImage(dark_image=passimg, light_image=passimg, size=(17,17))

    CTkLabel(master=signupscreen, text='', image=sideimage).pack(expand=True, side='right')

    frame= CTkFrame(master=signupscreen, width=300, height=480, fg_color='#ffffff')
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

    loginbutton = CTkButton(master=frame, text='Login', fg_color='#FFFFFF', hover_color='#FFFFFF', font=('Arial Bold', 9), text_color='#517BF4', width=225, corner_radius=14, command=openlogin)
    loginbutton.pack(anchor='w', pady=(20,0), padx=(25,0))

    signupscreen.mainloop()

loginapp()