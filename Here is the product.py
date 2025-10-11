from tkinter import *

root = Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")

lbl = Label(text="Product Calculator", fg="white", bg="#072F5F", height=2, width=300)
lbl.pack()


lbl1 = Label(text="Enter first number:", bg="#3895D3")
lbl1.pack()
entry1 = Entry()
entry1.pack()


lbl2 = Label(text="Enter second number:", bg="#3895D3")
lbl2.pack()
entry2 = Entry()
entry2.pack()


text_box = Text(height=4, width=40)
text_box.pack()


def calculate():
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        result = n1 * n2
        text_box.delete(1.0, END)
        text_box.insert(END, "\nFirst Number: {n1}\nSecond Number: {n2}\n\nProduct = {result}")
    

# Button
btn = Button(text="Calculate", command=calculate, bg="#1261a0", fg="white")
btn.pack(pady=10)

root.mainloop()
