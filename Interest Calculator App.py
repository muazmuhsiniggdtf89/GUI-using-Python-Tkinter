from tkinter import *
from tkinter import ttk

# Function to calculate interests
def calculate_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        # Simple Interest
        simple_interest = (p * t * r) / 100

        # Compound Interest
        compound_interest = p * ((1 + r / 100) ** t) - p

        result_label.config(
            text=f"Simple Interest: {simple_interest:2f}\nCompound Interest: {compound_interest:2f}"
        )
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.config(bg="#f8f9fa")  

frame = Frame(root, bg="#dbeafe", padx=20, pady=20)
frame.pack(pady=40)


Label(frame, text="Principal:", bg="#dbeafe", fg="#1e3a8a", font=("Arial", 10, "bold")).grid(row=0, column=0, pady=5)
principal_entry = Entry(frame, bg="#f1f5f9", fg="#1e293b", relief=SUNKEN)
principal_entry.grid(row=0, column=1, pady=5)

Label(frame, text="Time (in years):", bg="#dbeafe", fg="#1e3a8a", font=("Arial", 10, "bold")).grid(row=1, column=0,  pady=5)
time_entry = Entry(frame, bg="#f1f5f9", fg="#1e293b", relief=SUNKEN)
time_entry.grid(row=1, column=1, pady=5)

Label(frame, text="Rate of Interest (%):", bg="#dbeafe", fg="#1e3a8a", font=("Arial", 10, "bold")).grid(row=2, column=0,  pady=5)
rate_entry = Entry(frame, bg="#f1f5f9", fg="#1e293b", relief=SUNKEN)
rate_entry.grid(row=2, column=1, pady=5)


calc_button = Button(
    frame,
    text="Calculate",
    bg="#2563eb",     
    fg="white",
    command=calculate_interest,
    relief=SUNKEN,
    padx=10,
    pady=4
)
calc_button.grid(row=3, columnspan=2, pady=10)


result_label = Label(root, text="", bg="#f8f9fa", font=("Arial", 10, "bold"), fg="#0f766e")
result_label.pack()

root.mainloop()
