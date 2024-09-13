import tkinter
from customtkinter import *
import customtkinter as ctk
from PIL import Image
from tkcalendar import DateEntry
from tkintermapview import TkinterMapView

app = ctk.CTk()
app.title('TRADMIN')
app.geometry('1366x768')
app.resizable(0, 0)

# set_appearance_mode('light')

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

CTkLabel(master=grid, text='Status', font=('Arial Bold', 17), text_color='#0B2F4F', justify='left').grid(row=2, column=0, sticky='w', pady=(38, 0))

status_var = tkinter.IntVar(value=0)

CTkRadioButton(master=grid, variable=status_var, value=0, text='Confirmed', font=('Arial Bold', 14), text_color="#0B2F4F", fg_color="#517BF4", border_color="#517BF4", hover_color="#0B2F4F").grid(row=3, column=0, sticky="w", pady=(16,0))
CTkRadioButton(master=grid, variable=status_var, value=0, text='Pending', font=('Arial Bold', 14), text_color="#0B2F4F", fg_color="#517BF4", border_color="#517BF4", hover_color="#0B2F4F").grid(row=4, column=0, sticky="w", pady=(16,0))
CTkRadioButton(master=grid, variable=status_var, value=0, text='Cancelled', font=('Arial Bold', 14), text_color="#0B2F4F", fg_color="#517BF4", border_color="#517BF4", hover_color="#0B2F4F").grid(row=5, column=0, sticky="w", pady=(16,0))

CTkLabel(master=grid, text="Available vehicles", font=("Arial Bold", 17), text_color="#0B2F4F", justify="left").grid(row=6, column=0, sticky="w", pady=(42, 0))

coasterbusimg = Image.open('Coaster bus.JPG')
coasterbus = CTkImage(dark_image=coasterbusimg, light_image=coasterbusimg)
CTkButton(master=sidebar, image=coasterbus, text="Coaster Bus", text_color='#FFFFFF', font=("Arial Bold", 14), hover_color="#0B2F4F", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))
corollaimg = Image.open('Corolla.JPG')
corolla = CTkImage(dark_image=corollaimg, light_image=corollaimg)
CTkButton(master=sidebar, image=corolla, text="Corolla", text_color='#FFFFFF', font=("Arial Bold", 14), hover_color="#0B2F4F", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))
hiaceimg = Image.open('Hiace.JPG')
hiace = CTkImage(dark_image=hiaceimg, light_image=hiaceimg)
CTkButton(master=sidebar, image=hiace, text="Hiace", text_color='#FFFFFF', font=("Arial Bold", 14), hover_color="#0B2F4F", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))
hondaaccordimg = Image.open('Honda Accord.JPG')
hondaaccord = CTkImage(dark_image=hondaaccordimg, light_image=hondaaccordimg)
CTkButton(master=sidebar, image=hondaaccord, text="Honda Accord", text_color='#FFFFFF', font=("Arial Bold", 14), hover_color="#0B2F4F", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))
siennaimg = Image.open('Sienna.JPG')
sienna = CTkImage(dark_image=siennaimg, light_image=siennaimg)
CTkButton(master=sidebar, image=sienna, text="Sienna", text_color='#FFFFFF', font=("Arial Bold", 14), hover_color="#0B2F4F", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))
volvoimg = Image.open('Volvo.JPG')
volvo = CTkImage(dark_image=volvoimg, light_image=volvoimg)
CTkButton(master=sidebar, image=volvo, text="Volvo", text_color='#FFFFFF', font=("Arial Bold", 14), hover_color="#0B2F4F", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

bottomframe = CTkFrame(master=app, fg_color='#FFFFFF', width=650, height=200, corner_radius=0)
bottomframe.pack_propagate(0)
bottomframe.pack(fill='x', anchor='w', side='bottom')

grid = CTkFrame(master=bottomframe, fg_color='transparent')
grid.pack(fill= 'both', padx=27, pady=(31,0))

CTkLabel(master=grid, text="FROM:", font=("Arial Bold", 17), text_color="#0B2F4F", justify="left").grid(row=0, column=0, sticky="w")
CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300).grid(row=1, column=0, ipady=10)
CTkLabel(master=grid, text="TO:", font=("Arial Bold", 17), text_color="#0B2F4F", justify="left").grid(row=0, column=1, sticky="w", padx=(25,0))
CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300).grid(row=1, column=1, ipady=10, padx=(24,0))
CTkLabel(master=grid, text="DATE:", font=("Arial Bold", 17), text_color="#0B2F4F", justify="left").grid(row=0, column=2, sticky="w", padx=(30,0))
# CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300).grid(row=1, column=2, ipady=10, padx=(30,0))
# Create the date entry using tkcalendar
date_entry = DateEntry(master=grid, width=16, background='darkblue', foreground='white', borderwidth=2, date_pattern='y-mm-dd')
date_entry.grid(row=1, column=2, ipady=10, padx=(30, 0))

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

CTkButton(master=historyframe, text="View all", text_color="#474747", font=("Arial Bold", 14),  fg_color="transparent", hover_color="#0B2F4F", width=100, height=10).pack(anchor="nw", padx=27, pady=(10, 0))

# Add the search entry directly below the text description in the same frame (historyframe)
search_entry = CTkEntry(master=historyframe, width=300, placeholder_text="Search")
search_entry.pack(anchor="nw", padx=27, pady=(10,0))  # Use pack instead of grid to align with the previous elements

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