from tkinter import Listbox, Scrollbar, END, VERTICAL
from customtkinter import *
import customtkinter as ctk
from PIL import Image
from tkcalendar import DateEntry
from tkintermapview import TkinterMapView
from details import *


app = ctk.CTk()
app.title('TRADMIN')
app.geometry('1366x768')
app.resizable(0, 0)

# set_appearance_mode('dark')

upperframe = CTkFrame(master=app, fg_color='#FFFFFF', width=650, height=85, corner_radius=0)
upperframe.pack_propagate(0)
upperframe.pack(fill='x', anchor='w', side='top')

upperlabel = CTkLabel(master=upperframe, text='Welcome', font=('Arial Bold', 28), text_color='#0B2F4F')
upperlabel.pack(anchor='nw', pady=(29,0), padx=27)

sidebar = CTkFrame(master=app, fg_color='#FFFFFF', width=190, height=650, corner_radius=0)
sidebar.pack_propagate(0)
sidebar.pack(fill="y", anchor="w", side="left")

grid = CTkFrame(master=sidebar, fg_color='transparent')
grid.pack(fill= 'both', padx=27, pady=(31,0))

CTkLabel(master=grid, text='Status', font=('Arial Bold', 17), text_color='#0B2F4F', justify='left').grid(row=2, column=0, sticky='nw', pady=(2, 0))

status_var = tkinter.IntVar(value=0)

CTkRadioButton(master=grid, variable=status_var, value=1, text='Confirmed', font=('Arial Bold', 14), text_color="#0B2F4F", fg_color="#517BF4", border_color="#517BF4", hover_color="#0B2F4F").grid(row=3, column=0, sticky="w", pady=(10,0))
CTkRadioButton(master=grid, variable=status_var, value=2, text='Pending', font=('Arial Bold', 14), text_color="#0B2F4F", fg_color="#517BF4", border_color="#517BF4", hover_color="#0B2F4F").grid(row=4, column=0, sticky="w", pady=(10,0))
CTkRadioButton(master=grid, variable=status_var, value=3, text='Cancelled', font=('Arial Bold', 14), text_color="#0B2F4F", fg_color="#517BF4", border_color="#517BF4", hover_color="#0B2F4F").grid(row=5, column=0, sticky="w", pady=(10,0))

# Declare a variable to store the selected vehicle
selected_vehicle = tkinter.StringVar(value="No vehicle selected")

# Function to update the selected vehicle
def select_vehicle(vehicle_name):
    global selected_vehicle
    selected_vehicle.set(vehicle_name)  # Update the selected vehicle

# Function to display the selected status
def show_status():
    global history_listbox  # Ensure history_listbox is accessible here

    selected_status = status_var.get()
    # selected_vehicle = "No vehicle selected"  # Update this with the correct selected vehicle logic
    selected_date = date_entry.get()  # Get the selected date from DateEntry widget

    # if selected_status == 1:
    #     print("Status: Confirmed")
    # elif selected_status == 2:
    #     print("Status: Pending")
    # elif selected_status == 3:
    #     print("Status: Cancelled")

    if selected_status == 1:
        status_text = "Confirmed"
    elif selected_status == 2:
        status_text = "Pending"
    elif selected_status == 3:
        status_text = "Cancelled"
    else:
        status_text = "No status selected"
        
    # Add the selection to the history Listbox
    history_entry = f"Vehicle: {selected_vehicle.get()}, Status: {status_text}, Date: {selected_date}"
    history_listbox.insert(tkinter.END, history_entry)        
        
# Add a button to display the status
CTkButton(master=grid, text="Check Status", font=('Arial Bold', 14), text_color="#FFFFFF", command=show_status).grid(row=6, column=0, pady=(0, 0))

CTkLabel(master=grid, text="Available vehicles", font=("Arial Bold", 17), text_color="#0B2F4F", justify="left").grid(row=6, column=0, sticky="w", pady=(78, 0))

# Function to update the selected vehicle and open the popup window
def select_vehicle_and_popup(vehicle_name, popup_command):
    select_vehicle(vehicle_name)  # Update the selected vehicle
    popup_command()  # Open the respective popup window

# Modify the vehicle buttons to call both select_vehicle and the pop-up command

coasterbusimg = Image.open('Coaster bus.JPG')
coasterbus = CTkImage(dark_image=coasterbusimg, light_image=coasterbusimg)
CTkButton(master=sidebar, image=coasterbus, text="Coaster Bus", text_color='#FFFFFF', font=("Arial Bold", 14), hover_color="#0B2F4F", anchor="w", command=lambda: select_vehicle_and_popup("Coaster Bus", coasterpopup)).pack(anchor="center", ipady=5, pady=(16, 0))
corollaimg = Image.open('Corolla.JPG')
corolla = CTkImage(dark_image=corollaimg, light_image=corollaimg)
CTkButton(master=sidebar, image=corolla, text="Corolla", text_color='#FFFFFF', font=("Arial Bold", 14), hover_color="#0B2F4F", anchor="w", command=lambda: select_vehicle_and_popup("Corolla", corollapopup)).pack(anchor="center", ipady=5, pady=(16, 0))
hiaceimg = Image.open('Hiace.JPG')
hiace = CTkImage(dark_image=hiaceimg, light_image=hiaceimg)
CTkButton(master=sidebar, image=hiace, text="Hiace", text_color='#FFFFFF', font=("Arial Bold", 14), hover_color="#0B2F4F", anchor="w", command=lambda: select_vehicle_and_popup("Hiace", hiacepopup)).pack(anchor="center", ipady=5, pady=(16, 0))
hondaaccordimg = Image.open('Honda Accord.JPG')
hondaaccord = CTkImage(dark_image=hondaaccordimg, light_image=hondaaccordimg)
CTkButton(master=sidebar, image=hondaaccord, text="Honda Accord", text_color='#FFFFFF', font=("Arial Bold", 14), hover_color="#0B2F4F", anchor="w", command=lambda: select_vehicle_and_popup("Honda Accord", hondapopup)).pack(anchor="center", ipady=5, pady=(16, 0))
siennaimg = Image.open('Sienna.JPG')
sienna = CTkImage(dark_image=siennaimg, light_image=siennaimg)
CTkButton(master=sidebar, image=sienna, text="Sienna", text_color='#FFFFFF', font=("Arial Bold", 14), hover_color="#0B2F4F", anchor="w", command=lambda: select_vehicle_and_popup("Sienna", siennapopup)).pack(anchor="center", ipady=5, pady=(16, 0))
volvoimg = Image.open('Volvo.JPG')
volvo = CTkImage(dark_image=volvoimg, light_image=volvoimg)
CTkButton(master=sidebar, image=volvo, text="Volvo", text_color='#FFFFFF', font=("Arial Bold", 14), hover_color="#0B2F4F", anchor="w", command=lambda: select_vehicle_and_popup("Sienna", siennapopup)).pack(anchor="center", ipady=5, pady=(16, 0))


bottomframe = CTkFrame(master=app, fg_color='#FFFFFF', width=650, height=200, corner_radius=0)
bottomframe.pack_propagate(0)
bottomframe.pack(fill='x', anchor='w', side='bottom')

grid = CTkFrame(master=bottomframe, fg_color='transparent')
grid.pack(fill= 'both', padx=27, pady=(31,0))

CTkLabel(master=grid, text="FROM:", font=("Arial Bold", 17), text_color="#0B2F4F", justify="left").grid(row=0, column=0, sticky="w")
# CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300).grid(row=1, column=0, ipady=10)
# CTkLabel(master=grid, text="TO:", font=("Arial Bold", 17), text_color="#0B2F4F", justify="left").grid(row=0, column=1, sticky="w", padx=(25,0))
# CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300).grid(row=1, column=1, ipady=10, padx=(24,0))
# CTkLabel(master=grid, text="DATE:", font=("Arial Bold", 17), text_color="#0B2F4F", justify="left").grid(row=0, column=2, sticky="w", padx=(30,0))

# Create a frame to hold the "From" Listbox and scrollbar
# fromframe = ctk.CTkFrame(master=grid)
# fromframe.grid(row=1, column=0, sticky="nw")

# fromlabel = ctk.CTkLabel(master=grid, text="FROM:", font=("Arial Bold", 17), text_color="#0B2F4F")
# fromlabel.grid(row=0, column=0, sticky="w")

from_listbox = Listbox(master=grid, height=10)
from_listbox.grid(row=1, column=0, sticky="nsew")
from_scrollbar = Scrollbar(master=grid, orient=VERTICAL, command=from_listbox.yview)
from_scrollbar.grid(row=1, column=0, sticky='ns', padx=(200, 0))  # Adjust as necessary
from_listbox.config(yscrollcommand=from_scrollbar.set)

# # Create a scrollbar for the "From" list
# fromscrollbar = Scrollbar(bottomframe, orient=VERTICAL)
# fromscrollbar.pack(side='right', fill='y')
# # fromscrollbar.grid(row=1, column=0, sticky='ns')

# # Create a Listbox for the "From" list and attach the scrollbar
# from_listbox = Listbox(bottomframe, height=10, yscrollcommand=fromscrollbar.set)
# from_listbox.pack(side='left', fill='y')
# # from_listbox.grid(row=1, column=0, sticky='nsew')

# # Configure the scrollbar to work with the Listbox
# fromscrollbar.config(command=from_listbox.yview)

# Populate the "From" Listbox with a list of places
fromplaces = ['Lagos', 'Oyo', 'Osun', 'Kwara', 'Ondo', 'Ogun', 'Abuja', 'Port-Harcourt', 'Kogi']
for place in fromplaces:
    from_listbox.insert(END, place)

# bottomframe = CTkFrame(master=app, fg_color='#FFFFFF', width=650, height=200, corner_radius=0)
# bottomframe.pack_propagate(0)
# bottomframe.pack(fill='x', anchor='w', side='bottom')

# grid = CTkFrame(master=bottomframe, fg_color='transparent')
# grid.pack(fill= 'both', padx=27, pady=(31,0))

CTkLabel(master=grid, text="TO:", font=("Arial Bold", 17), text_color="#0B2F4F", justify="left").grid(row=0, column=1, sticky="w", padx=(25,0))
# to_frame = ctk.CTkFrame(master=grid)
# to_frame.grid(row=1, column=1, sticky="nw", padx=(25, 0))

# to_label = ctk.CTkLabel(master=grid, text="TO:", font=("Arial Bold", 17), text_color="#0B2F4F")
# to_label.grid(row=0, column=1, sticky="w", padx=(25, 0))

# # Create a scrollbar for the "To" list
# to_scrollbar = Scrollbar(bottomframe, orient=VERTICAL)
# to_scrollbar.pack(side='right', fill='y')

# # Create a Listbox for the "To" list and attach the scrollbar
# to_listbox = Listbox(bottomframe, height=10, yscrollcommand=to_scrollbar.set)
# to_listbox.pack(side='left', fill='y')

# # Configure the scrollbar to work with the Listbox
# to_scrollbar.config(command=to_listbox.yview)

to_listbox = Listbox(master=grid, height=10)
to_listbox.grid(row=1, column=1, sticky="nsew")
to_scrollbar = Scrollbar(master=grid, orient=VERTICAL, command=to_listbox.yview)
to_scrollbar.grid(row=1, column=1, sticky='ns', padx=(200, 0))  # Adjust as necessary
to_listbox.config(yscrollcommand=to_scrollbar.set)

# Populate the "To" Listbox with a list of places
toplaces = ['Lagos', 'Oyo', 'Osun', 'Kwara', 'Ondo', 'Ogun', 'Abuja', 'Port-Harcourt', 'Kogi']
for place in toplaces:
    to_listbox.insert(END, place)    

# CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300).grid(row=1, column=2, ipady=10, padx=(30,0))
# Create the date entry using tkcalendar

CTkLabel(master=grid, text="DATE:", font=("Arial Bold", 17), text_color="#0B2F4F").grid(row=0, column=2, sticky="w", padx=(30, 0))
date_entry = DateEntry(master=grid, width=16, background='darkblue', foreground='white', borderwidth=2, date_pattern='yy-mm-dd')
date_entry.grid(row=1, column=2, ipady=5, padx=(30, 0), pady=(0, 10))

# Configure grid weights to allow resizing
grid.columnconfigure(0, weight=1)
grid.columnconfigure(1, weight=1)
grid.columnconfigure(2, weight=1)

mapframe = CTkFrame(master=app, fg_color='#FFFFFF', width=550, height=510, corner_radius=0)
mapframe.pack_propagate(0)
mapframe.pack(fill='x', anchor='w', side='right')

mapwidget = TkinterMapView(master=mapframe, width=550, height=510, corner_radius=0)
mapwidget.pack()

mapwidget.set_position(9.0820, 7.4960)  # Coordinates of Abuja, Nigeria
mapwidget.set_zoom(10)  # Set zoom level
mapwidget.set_marker(9.0820, 7.4960, text="Abuja")

# historyframe = CTkFrame(master=app, fg_color='#FFFFFF', width=650, height=510, corner_radius=0)
# historyframe.pack_propagate(0)
# historyframe.pack(fill='x', anchor='w', side='left')

# historylabel = CTkLabel(master=historyframe, text="HISTORY", font=('Arial Bold', 21), text_color='#0B2F4F')
# historylabel.pack(anchor='nw', pady=(29, 0), padx=27)
# CTkLabel(master=historyframe, text="View your team's trips and transactions.", font=("Arial Bold", 17), text_color='#0B2F4F').pack(anchor="nw", pady=(25,0), padx=27)

# search_entry = CTkEntry(master=historylabel, width=300, placeholder_text="Search")
# search_entry.grid(row=2, column=0, columnspan=2, padx=(0, 10), pady=(10,0))

historyframe = CTkFrame(master=app, fg_color='#FFFFFF', width=650, height=510, corner_radius=0)
historyframe.pack_propagate(0)
historyframe.pack(fill='x', anchor='w', side='left')
historylabel = CTkLabel(master=historyframe, text="HISTORY", font=('Arial Bold', 21), text_color='#0B2F4F')
historylabel.pack(anchor='nw', pady=(29, 0), padx=27)

# Label for the description
CTkLabel(master=historyframe, text="View your team's trips and transactions.", font=("Arial Bold", 17), text_color='#0B2F4F').pack(anchor="nw", pady=(25,0), padx=27)

search_entry = CTkEntry(master=historyframe, width=300, placeholder_text="Search")
search_entry.pack(anchor="nw", padx=27, pady=(10,0))

# Declare history_listbox as global so other functions can access it
global history_listbox
history_listbox = tkinter.Listbox(master=historyframe, height=10, font=("Arial", 12))
history_listbox.pack(anchor="nw", padx=27, pady=(10, 0), fill="x")


# CTkButton(master=historyframe, text="View all", text_color="#474747", font=("Arial Bold", 14),  fg_color="transparent", hover_color="#0B2F4F", width=100, height=10).pack(anchor="nw", padx=27, pady=(10, 0), side="left")
# button2 = CTkButton(master=historyframe, text="Luxury", text_color="#474747", fg_color="#517BF4", hover_color="#0B2F4F", font=("Arial Bold", 14))
# button2.pack(anchor="nw", padx=(10, 0), pady=(10, 0), side="left")

  
# CTkButton(master=historyframe, text="View all", text_color="#FFFFFF", font=("Arial Bold", 14), hover_color="#0B2F4F").pack(anchor="w", padx=(0, 0), pady=(0, 0))
# CTkButton(master=historyframe, text="Luxury", text_color="#FFFFFF", font=("Arial Bold", 14), hover_color="#0B2F4F", anchor="center").pack(anchor="center", ipady=5, pady=(60, 0))


# grid = CTkFrame(master= bottomframe, fg_color='transparent')
# grid.pack(fill='both', packx=27, pady=(31,0))

# CTkLabel(master=grid, text='To: ', font=('Arial Bold', 17), text_color='#0B2F4F', justify='left').grid(row=0, column=0, sticky='w')
# CTkEntry(master=grid, fg_color='#0B2F4F', border_width=0, width=300).grid(row=1, column=0, ipady=10)

# sidebarstatus = CTkLabel(master=app, fg_color='#0B2F4F', width=176, height=120, corner_radius=0)
# sidebarstatus.pack_propagate(0)
# sidebarstatus.pack(side='left')

app.mainloop()