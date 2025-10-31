import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.config(bg="#8099CA")

choices = ["Rock", "Paper", "Scissors"]


title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), fg="white", bg="#8099CA")
title.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="yellow", bg="#8099CA")
result_label.pack(pady=20)

YOUR_CHOICE_label = tk.Label(root, text="", font=("Arial", 12), fg="lightblue", bg="#8099CA")
YOUR_CHOICE_label.pack()

Computer_choice_label = tk.Label(root, text="", font=("Arial", 12), fg="lightgreen", bg="#8099CA")
Computer_choice_label.pack()

def play(YOUR_CHOICE):
    Computer_choice = random.choice(choices)
    YOUR_CHOICE_label.config(text="You chose: {YOUR_CHOICE}")
    Computer_choice_label.config(text="Computer chose: {Computer_choice}")

    if YOUR_CHOICE == Computer_choice:
        result = "It's a tie!"
    elif (YOUR_CHOICE == "Rock" and Computer_choice == "Scissors") or \
         (YOUR_CHOICE == "Paper" and Computer_choice == "Rock") or \
         (YOUR_CHOICE == "Scissors" and Computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"
    
    result_label.config(text=result)


for choice in choices:
    button = tk.Button(root, text=choice, width=12, height=2,bg="#61afef", fg="white", font=("Arial", 12, "bold"),
                       command=lambda c=choice: play(c))
    button.pack(pady=5)

root.mainloop()
