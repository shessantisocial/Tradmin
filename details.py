import tkinter
from customtkinter import *
import customtkinter as ctk


def coasterpopup():

    # global history_listbox  # Make history_listbox accessible here

    # selected_vehicle = "Coaster Bus"
    # selected_status = status_var.get()
    # selected_date = date_entry.get()

    # # Determine status text based on the status selected
    # if selected_status == 1:
    #     status_text = "Confirmed"
    # elif selected_status == 2:
    #     status_text = "Pending"
    # elif selected_status == 3:
    #     status_text = "Cancelled"
    # else:
    #     status_text = "No status selected"

    # # Update the history Listbox
    # history_entry = f"Vehicle: {selected_vehicle}, Status: {status_text}, Date: {selected_date}"
    # history_listbox.insert(tkinter.END, history_entry)    
    # # Create a new Toplevel window (popup)

    popup = CTkToplevel()
    popup.title("Coaster Bus Details")
    popup.geometry("300x200")

    # Add a label with details inside the popup
    detail_label = CTkLabel(master=popup, text="This is a Coaster Bus. \nIt has 30 seats and is \nideal for group trips.", font=("Arial", 14), text_color="#0B2F4F")
    detail_label.pack(pady=20)

    # Add an 'Okay' button to close the popup
    ok_button = CTkButton(master=popup, text="Close", command=popup.destroy, text_color="#FFFFFF", fg_color="#517BF4", hover_color="#0B2F4F", width=100)
    ok_button.pack(pady=20)

    popup.grab_set()  # Ensure the popup is modal (prevents interaction with main window until closed)

def corollapopup():
    corolladetails = CTkToplevel()
    corolladetails.title("Corolla Car Details")
    corolladetails.geometry("300x200")

    CTkLabel(master=corolladetails, text="This is a Corolla Car. \nIt has 4 seats and is \nideal for personal or family trips.", font=("Arial", 14), text_color="#0B2F4F").pack(pady=20)
    CTkButton(master=corolladetails, text="Close", command=corolladetails.destroy, text_color="#FFFFFF", fg_color="#517BF4", hover_color="#0B2F4F", width=100).pack(pady=20) 

    corolladetails.grab_set()  

def hiacepopup():
    hiacedetails = CTkToplevel()
    hiacedetails.title("Hiace Bus Details")
    hiacedetails.geometry("300x200")

    CTkLabel(master=hiacedetails, text="This is a luxury Hiace Bus. \nIt has a total of 32 seats and is \nideal for tourists or family trips.", font=("Arial", 14), text_color="#0B2F4F").pack(pady=20)
    CTkButton(master=hiacedetails, text="Close", command=hiacedetails.destroy, text_color="#FFFFFF", fg_color="#517BF4", hover_color="#0B2F4F", width=100).pack(pady=20) 

    hiacedetails.grab_set()   

def hondapopup():
    hondadetails = CTkToplevel()
    hondadetails.title("Honda Accorrd Details")
    hondadetails.geometry("300x200")

    CTkLabel(master=hondadetails, text="This is a Honda Accord Car. \nIt has 5 seats and is \nideal for personal or group trips.", font=("Arial", 14), text_color="#0B2F4F").pack(pady=20)
    CTkButton(master=hondadetails, text="Close", command=hondadetails.destroy, text_color="#FFFFFF", fg_color="#517BF4", hover_color="#0B2F4F", width=100).pack(pady=20)

    hondadetails.grab_set()
                    
def siennapopup():
    siennadetails = CTkToplevel()
    siennadetails.title("Sienna Details")
    siennadetails.geometry("300x200")

    CTkLabel(master=siennadetails, text="This is a luxury Sienna Car. \nIt has 8 passenger seats and is \nideal for tourists or group trips.", font=("Arial", 14), text_color="#0B2F4F").pack(pady=20)
    CTkButton(master=siennadetails, text="Close", command=siennadetails.destroy, text_color="#FFFFFF", fg_color="#517BF4", hover_color="#0B2F4F", width=100).pack(pady=20)

    siennadetails.grab_set()   

def volvopopup():
    volvodetails = CTkToplevel()
    volvodetails.title("Sienna Details")
    volvodetails.geometry("300x200")

    CTkLabel(master=volvodetails, text="This is a luxury Volvo Car. \nIt has 5 passenger seats and is \nideal for personal or family trips.", font=("Arial", 14), text_color="#0B2F4F").pack(pady=20)
    CTkButton(master=volvodetails, text="Close", command=volvodetails.destroy, text_color="#FFFFFF", fg_color="#517BF4", hover_color="#0B2F4F", width=100).pack(pady=20)

    volvodetails.grab_set()

    