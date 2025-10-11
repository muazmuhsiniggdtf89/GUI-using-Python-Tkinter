from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

messagebox.showwarning("Window Name", "Text to be displayed")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

button = Button(root, text ="Scan for Virus", command = msg)
button.place(x=40, y= 80)

root.mainloop()
