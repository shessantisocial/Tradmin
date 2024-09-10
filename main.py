from customtkinter import *
import customtkinter as ctk
from PIL import Image

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

sidebarframe = CTkFrame(master=app, fg_color='#FFFFFF', width=190, height=650, corner_radius=0)
sidebarframe.pack_propagate(0)
sidebarframe.pack(fill="y", anchor="w", side="left")

bottomframe = CTkFrame(master=app, fg_color='#FFFFFF', width=650, height=200, corner_radius=0)
bottomframe.pack_propagate(0)
bottomframe.pack(fill='x', anchor='w', side='bottom')

CTkLabel(master=bottomframe, text='To: ', font=('Arial Bold', 17), text_color='#0B2F4F', justify='left').grid(row=0, column=0, sticky='w')

# sidebarstatus = CTkLabel(master=app, fg_color='#0B2F4F', width=176, height=120, corner_radius=0)
# sidebarstatus.pack_propagate(0)
# sidebarstatus.pack(side='left')

app.mainloop()