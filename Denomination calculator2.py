from tkinter import *
from tkinter import messagebox 
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg ='light blue')
root.geometry('650x400')

upload = Image.open("app_img.jpg")

upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root, text = "Hey user! Welcome to denomination Counter Application.", bg = 'light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg ():
    MsgBox = messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
       topwin( )

button1 = Button(root, text= "Let's get started!", command=msg,bg='brown', fg='white')
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter Total Amount ", bg = 'light grey')
    entry = Entry(top)
    lbl = Label(top, text="HEre are number of notes for each domination", bg='light grey')

    l1 = Label(top, text="1000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')
    l4 = Label(top, text="50", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note1000 = amount // 1000
            amount %= 1000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            amount %= 100
            note50 = amount // 50
            amount %= 50

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)


            t1.insert(END, str(note1000))
            t2.insert(END, str(note500))
            t4.insert(END, str(note100))
            t4.insert(END, str(note50))
        except ValueError:
            messagebox.showerror("Eror", "Please enter a valid number.")

    btn = Button(top, text="Calculate", command=calculator, bg='brown', fg='white')

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    l4.place(x=180, y=290)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    t4.place(x=270, y=290)

    top.mainloop()
root.mainloop()


