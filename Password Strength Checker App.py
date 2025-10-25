from tkinter import *

def check_strength():
    password = entry.get()
    length = len(password)

    if length <= 5:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "yellow"
    
    elif 9 <= length <= 12:
        strength = "Strong"
        color = "lightgreen"
    else:
        strength = "Very Strong"
        color = "darkgreen"
    result_label.config(text=f"Strength:{strength}", bg=color)

root = Tk()
root.title("Password Strength Cheker App")
root.geometry("400x400")
root.config(bg="#d0efff")

frame = Frame(root, bg="#b0e0e6", height=300, width=360 )
frame.pack(pady=40)

lbl = Label(frame, text="Enter your Password: ",font=("Arial", 12, "bold"), bg= "#4682b4",fg="white", pady=5)
lbl.pack(pady=10)

entry = Entry(frame, show="*", font=("Arial", 12), width=25,justify="center")
entry.pack(pady=10)

btn = Button(frame, text="Check Strength", font=("Arial", 11, "bold"), bg="#1e90ff", fg="white", command=check_strength)
btn.pack(pady=10)

result_label = Label(frame, text="", font=("Arial", 12, "bold"), width=25, height=2)
result_label.pack(pady=10)

root.mainloop()
    
