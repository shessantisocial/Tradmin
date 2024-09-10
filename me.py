from customtkinter import *
import customtkinter as ctk

app = ctk.CTk()
app.title('Tradmin')
app.geometry("1366x768")
app.resizable(0,0)

# frame1 = CTkFrame(master=app, width=300, fg_color='#517BF4')
# frame1.pack_propagate(0)
# frame1.pack(side='top', expand=True, fill='x', pady=100)

# label1 = CTkLabel(master=app, text='Welcome to Tradmin!', text_color='#0B2F4F', anchor='w', justify='left', font=('Arial Bold', 24))
# label1.pack(anchor='w')

frame = CTkFrame(master=app, fg_color='#517BF4', width=176, height=650, corner_radius=0)
frame.pack_propagate(0)
frame.pack(side='left', anchor='w', fill='y')



# frame1 = CTkFrame(master=app, fg_color='#517BF4', width=176, height=650, corner_radius=0)
# frame1.pack_propagate(0)
# frame1.pack(side='left', anchor='w', fill='y')

# label1 = CTkLabel(master=app, text='Welcome to Tradmin!', text_color='#0B2F4F', anchor='w', justify='left', font=('Arial Bold', 24))
# label1.pack(anchor='w')

# frame2 = CTkFrame(master=app, fg_color='#0B2F4F')
# frame2.pack(side='bottom', expand=True, fill="both")

# frame3 = CTkFrame(master=app, fg_color='#517BF4')
# frame3.pack(side='top', expand=True, fill="x")

# frame4 = CTkFrame(master=app, fg_color='#7E7E7E')
# frame4.pack(side='right', expand=True, fill="x")

# # Get the screen width and height
# screen_width = app.winfo_screenwidth()
# screen_height = app.winfo_screenheight()

# # Set the window geometry to the screen size
# app.geometry(f"{screen_width}x{screen_height}")

# # Set the window to be full-screen
# app.attributes('-fullscreen', True)
app.mainloop() 