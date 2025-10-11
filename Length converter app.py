from tkinter import *

root = Tk()
root.title("Length Converter App")
root.geometry("400x300")
root.config(bg="#d0efff")


frame = Frame(root, height=200, width=360, bg="#d0efff")
frame.pack(pady=20)


lbl1 = Label(frame, text="Enter length in metre:", bg="#057c85", fg="white", width=25, pady=5)
lbl1.pack(pady=10)


num_entry = Entry(frame, width=20)
num_entry.pack(pady=5)


textbox = Text(root, height=3, width=30, bg="#BEBEBE", fg="black")
textbox.pack(pady=10)


def display():
    
        meter = float(num_entry.get())
        km = meter / 1000
        textbox.delete("1.0", END)
        textbox.insert(END, f"\n{meter} metre = {km} kilometre")
    


btn = Button(root, text="Convert to Kilometre", command=display, bg="red", fg="white")
btn.pack(pady=10)

root.mainloop()
