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

# Top frame
upperframe = CTkFrame(master=app, fg_color='#FFFFFF', width=650, height=85, corner_radius=0)
upperframe.pack_propagate(0)
upperframe.pack(fill='x', anchor='w', side='top')

upperlabel = CTkLabel(master=upperframe, text='Welcome', font=('Arial Bold', 28), text_color='#0B2F4F')
upperlabel.pack(anchor='nw', pady=(29, 0), padx=27)

# Sidebar frame
sidebar = CTkFrame(master=app, fg_color='#FFFFFF', width=190, height=650, corner_radius=0)
sidebar.pack_propagate(0)
sidebar.pack(fill="y", anchor="w", side="left")

grid = CTkFrame(master=sidebar, fg_color='transparent')
grid.pack(fill='both', padx=27, pady=(31, 0))

CTkLabel(master=grid, text='Status', font=('Arial Bold', 17), text_color='#0B2F4F', justify='left').grid(row=2, column=0, sticky='w', pady=(38, 0))
status_var = tkinter.IntVar(value=0)

CTkRadioButton(master=grid, variable=status_var, value=0, text='Confirmed', font=('Arial Bold', 14), text_color="#0B2F4F", fg_color="#517BF4", border_color="#517BF4", hover_color="#0B2F4F").grid(row=3, column=0, sticky="w", pady=(16, 0))
CTkRadioButton(master=grid, variable=status_var, value=0, text='Pending', font=('Arial Bold', 14), text_color="#0B2F4F", fg_color="#517BF4", border_color="#517BF4", hover_color="#0B2F4F").grid(row=4, column=0, sticky="w", pady=(16, 0))
CTkRadioButton(master=grid, variable=status_var, value=0, text='Cancelled', font=('Arial Bold', 14), text_color="#0B2F4F", fg_color="#517BF4", border_color="#517BF4", hover_color="#0B2F4F").grid(row=5, column=0, sticky="w", pady=(16, 0))

CTkLabel(master=grid, text="Available vehicles", font=("Arial Bold", 17), text_color="#0B2F4F", justify="left").grid(row=6, column=0, sticky="w", pady=(42, 0))

# Bottom frame divided into two parts
bottom_frame = CTkFrame(master=app, fg_color='#FFFFFF')
bottom_frame.pack(fill='both', expand=True, anchor='w', side='top', pady=(20, 0))

# Frame for the form elements
form_frame = CTkFrame(master=bottom_frame, fg_color='#FFFFFF')
form_frame.pack(fill="both", expand=True, side="left", padx=20)

grid = CTkFrame(master=form_frame, fg_color='transparent')
grid.pack(fill='both', padx=27, pady=(31, 0))

CTkLabel(master=grid, text="FROM:", font=("Arial Bold", 17), text_color="#0B2F4F", justify="left").grid(row=0, column=0, sticky="w")
CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300).grid(row=1, column=0, ipady=10)

CTkLabel(master=grid, text="TO:", font=("Arial Bold", 17), text_color="#0B2F4F", justify="left").grid(row=0, column=1, sticky="w", padx=(25, 0))
CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300).grid(row=1, column=1, ipady=10, padx=(24, 0))

CTkLabel(master=grid, text="DATE:", font=("Arial Bold", 17), text_color="#0B2F4F", justify="left").grid(row=0, column=2, sticky="w", padx=(30, 0))
date_entry = DateEntry(master=grid, width=16, background='darkblue', foreground='white', borderwidth=2, date_pattern='y-mm-dd')
date_entry.grid(row=1, column=2, ipady=10, padx=(30, 0))

# Map frame (to take the right half of the remaining space)
map_frame = CTkFrame(master=bottom_frame, fg_color='#FFFFFF')
map_frame.pack(fill="both", expand=True, side="left", padx=20)

# Create and configure the map widget
map_widget = TkinterMapView(map_frame, width=600, height=500, corner_radius=10)
map_widget.pack(fill='both', expand=True, padx=10, pady=10)

# Set map to Nigeria (Abuja) by default
map_widget.set_position(9.0820, 7.4960)  # Coordinates of Abuja, Nigeria
map_widget.set_zoom(10)  # Set zoom level
map_widget.set_marker(9.0820, 7.4960, text="Abuja")

app.mainloop()
