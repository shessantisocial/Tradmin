import customtkinter as ctk
import tkinter as tk

# Initialize the main window
def initialize_app():
    app = ctk.CTk()
    app.title("Page Navigation Example")
    app.geometry("400x300")

    # Create frames for different pages
    frame1 = create_page1(app)
    frame2 = create_page2(app)

    # Function to switch frames
    def show_frame(frame):
        frame1.pack_forget()
        frame2.pack_forget()
        frame.pack(fill="both", expand=True)

    # Initially show the first frame
    show_frame(frame1)

    # Attach frame switching functions to buttons
    def go_to_page1():
        show_frame(frame1)

    def go_to_page2():
        show_frame(frame2)

    # Add navigation buttons to frames
    add_navigation_buttons(frame1, go_to_page2)
    add_navigation_buttons(frame2, go_to_page1)

    # Start the main loop
    app.mainloop()

# Create the first page
def create_page1(parent):
    frame = ctk.CTkFrame(parent)
    label = ctk.CTkLabel(frame, text="This is Page 1")
    label.pack(pady=20)

    return frame

# Create the second page
def create_page2(parent):
    frame = ctk.CTkFrame(parent)
    label = ctk.CTkLabel(frame, text="This is Page 2")
    label.pack(pady=20)

    return frame

# Add navigation buttons to a frame
def add_navigation_buttons(frame, navigate_function):
    button_text = "Go to Page 2" if "Page 1" in frame.winfo_children()[0].cget("text") else "Go to Page 1"
    button = ctk.CTkButton(frame, text=button_text, command=navigate_function)
    button.pack(pady=10)

# Run the application
if __name__ == "__main__":
    initialize_app()
