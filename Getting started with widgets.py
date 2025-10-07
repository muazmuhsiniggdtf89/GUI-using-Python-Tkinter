from tkinter import *
from datetime import date

root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

# Label at the top
lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=2, width=300)
lbl.pack()

# Label and entry for name
name_lbl = Label(text="Full Name", bg="#3895D3")
name_lbl.pack()

name_entry = Entry()
name_entry.pack()

# Text box for output
text_box = Text(height=5, width=40)
text_box.pack()

# Function for button click
def display():
    name = name_entry.get()
    message = "Welcome to the Application!\nToday's date is: "
    greet = "Hello " + name + "\n\n"
    
    # Clear old text before inserting new
    text_box.delete(1.0, END)
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, str(date.today()))

# Button
btn = Button(text="Begin", command=display, height=1, bg="#1261a0", fg='white')
btn.pack(pady=10)

root.mainloop()
