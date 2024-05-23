import tkinter as tk
import random

def check_guess():
    global attempts
    user_guess = int(entry.get())
    attempts += 1
    if user_guess < secret_number:
        result_label.config(text="Too low! Try again.")
    elif user_guess > secret_number:
        result_label.config(text="Too high! Try again.")
    else:
        result_label.config(text=f"Congratulations! You won in {attempts} attempts.")
        attempts = 0

root = tk.Tk()
root.title("Guess the Number")

secret_number = random.randint(1, 100)
attempts = 0

welcome_label = tk.Label(root, text="Welcome to the guessing game!")
welcome_label.pack()

instruction_label = tk.Label(root, text="I'm thinking of a number between 1 and 100.")
instruction_label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Check", command=check_guess)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()