from tkinter import *
from datetime import date

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")


frame = Frame(root, height=200, width=360, bg="#d0efff")
frame.pack(pady=20)


lbl1 = Label(frame, text="Full Name", bg="#3895D3", fg='white', width=15, pady=5)
lbl1.pack(pady=5)
name_entry = Entry(frame, width=25)
name_entry.pack(pady=5)

lbl2 = Label(frame, text="Birth Date (DD)", bg="#3895D3", fg='white', width=15, pady=5)
lbl2.pack(pady=5)
date_entry = Entry(frame, width=25)
date_entry.pack(pady=5)

lbl3 = Label(frame, text="Birth Month (MM)", bg="#3895D3", fg='white', width=15, pady=5)
lbl3.pack(pady=5)
month_entry = Entry(frame, width=25)
month_entry.pack(pady=5)

lbl4 = Label(frame, text="Birth Year (YYYY)", bg="#3895D3", fg='white', width=15, pady=5)
lbl4.pack(pady=5)
year_entry = Entry(frame, width=25)
year_entry.pack(pady=5)


textbox = Text(root, height=3, width=35, bg="#BEBEBE", fg="black")
textbox.pack(pady=15)


def calculate_age():
    name = name_entry.get()
    day = int(date_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    today = date.today()
    age = today.year - year  # simple difference (no month/day check)

    textbox.delete("1.0", END)
    textbox.insert(END, f"Hello {name}!\nYou are {age} years old.")


btn = Button(root, text="Calculate Age", command=calculate_age, bg="red", fg="white", width=18, pady=5)
btn.pack(pady=10)

root.mainloop()
