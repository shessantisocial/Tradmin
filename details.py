import tkinter
from customtkinter import *
import customtkinter as ctk
from PIL import Image


def coasterpopup():

    popup = CTkToplevel()
    popup.title("Coaster Bus Details")
    popup.geometry("300x200")

    coasterimg = Image.open('Coaster bus.JPG')
    coasterimage = CTkImage(dark_image=coasterimg, light_image=coasterimg, size=(150, 80))

    image_label = CTkLabel(master=popup, image=coasterimage, text="")
    image_label.pack(pady=10)

    detail_label = CTkLabel(master=popup, text="This is a Coaster Bus. \nIt has 30 seats and is \nideal for group trips.", font=("Arial", 14), text_color="#0B2F4F")
    detail_label.pack(pady=20)

    ok_button = CTkButton(master=popup, text="Okay", command=popup.destroy, text_color="#FFFFFF", fg_color="#517BF4", hover_color="#0B2F4F", width=100)
    ok_button.pack(pady=20)

    popup.grab_set()  # Ensure the popup is modal (prevents interaction with main window until closed)

def corollapopup():
    corolladetails = CTkToplevel()
    corolladetails.title("Corolla Car Details")
    corolladetails.geometry("300x200")

    corollaimg = Image.open('Corolla.JPG')
    corollaimage = CTkImage(dark_image=corollaimg, light_image=corollaimg, size=(150, 80))

    image_label = CTkLabel(master=corolladetails, image=corollaimage, text="")
    image_label.pack(pady=10)

    CTkLabel(master=corolladetails, text="This is a Corolla Car. \nIt has 4 seats and is \nideal for personal or family trips.", font=("Arial", 14), text_color="#0B2F4F").pack(pady=20)
    CTkButton(master=corolladetails, text="Okay", command=corolladetails.destroy, text_color="#FFFFFF", fg_color="#517BF4", hover_color="#0B2F4F", width=100).pack(pady=20) 

    corolladetails.grab_set()  

def hiacepopup():
    hiacedetails = CTkToplevel()
    hiacedetails.title("Hiace Bus Details")
    hiacedetails.geometry("300x200")

    hiaceimg = Image.open('Hiace.JPG')
    hiaceimage = CTkImage(dark_image=hiaceimg, light_image=hiaceimg, size=(150, 80))

    image_label = CTkLabel(master=hiacedetails, image=hiaceimage, text="")
    image_label.pack(pady=10)    

    CTkLabel(master=hiacedetails, text="This is a luxury Hiace Bus. \nIt has a total of 32 seats and is \nideal for tourists or family trips.", font=("Arial", 14), text_color="#0B2F4F").pack(pady=20)
    CTkButton(master=hiacedetails, text="Okay", command=hiacedetails.destroy, text_color="#FFFFFF", fg_color="#517BF4", hover_color="#0B2F4F", width=100).pack(pady=20) 

    hiacedetails.grab_set()   

def hondapopup():
    hondadetails = CTkToplevel()
    hondadetails.title("Honda Accorrd Details")
    hondadetails.geometry("300x200")

    hondaimg = Image.open('Honda Accord.JPG')
    hondaimage = CTkImage(dark_image=hondaimg, light_image=hondaimg, size=(150, 80))

    image_label = CTkLabel(master=hondadetails, image=hondaimage, text="")
    image_label.pack(pady=10)    

    CTkLabel(master=hondadetails, text="This is a Honda Accord Car. \nIt has 5 seats and is \nideal for personal or group trips.", font=("Arial", 14), text_color="#0B2F4F").pack(pady=20)
    CTkButton(master=hondadetails, text="Okay", command=hondadetails.destroy, text_color="#FFFFFF", fg_color="#517BF4", hover_color="#0B2F4F", width=100).pack(pady=20)

    hondadetails.grab_set()
                    
def siennapopup():
    siennadetails = CTkToplevel()
    siennadetails.title("Sienna Details")
    siennadetails.geometry("300x200")

    siennaimg = Image.open('Sienna.JPG')
    siennaimage = CTkImage(dark_image=siennaimg, light_image=siennaimg, size=(150, 80))

    image_label = CTkLabel(master=siennadetails, image=siennaimage, text="")
    image_label.pack(pady=10)   

    CTkLabel(master=siennadetails, text="This is a luxury Sienna Car. \nIt has 8 passenger seats and is \nideal for tourists or group trips.", font=("Arial", 14), text_color="#0B2F4F").pack(pady=20)
    CTkButton(master=siennadetails, text="Okay", command=siennadetails.destroy, text_color="#FFFFFF", fg_color="#517BF4", hover_color="#0B2F4F", width=100).pack(pady=20)

    siennadetails.grab_set()   

def volvopopup():
    volvodetails = CTkToplevel()
    volvodetails.title("Sienna Details")
    volvodetails.geometry("300x200")

    volvoimg = Image.open('Volvo.JPG')
    volvoimage = CTkImage(dark_image=volvoimg, light_image=volvoimg, size=(80, 80))

    image_label = CTkLabel(master=volvodetails, image=volvoimage, text="")
    image_label.pack(pady=10)    

    CTkLabel(master=volvodetails, text="This is a luxury Volvo Car. \nIt has 5 passenger seats and is \nideal for personal or family trips.", font=("Arial", 14), text_color="#0B2F4F").pack(pady=20)
    CTkButton(master=volvodetails, text="Okay", command=volvodetails.destroy, text_color="#FFFFFF", fg_color="#517BF4", hover_color="#0B2F4F", width=100).pack(pady=20)

    volvodetails.grab_set()

    