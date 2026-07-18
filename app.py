from tkinter import *
import random
import string


window = Tk()
window.title("Password Generator")
window.geometry("400x350")
window.config(bg="lightblue")


def generate():
    length = int(size_entry.get())

    characters = string.ascii_letters + string.digits + "@#$%&*"

    password = ""

    for i in range(length):
        password += random.choice(characters)

    result.delete(0, END)
    result.insert(0, password)


def clear():
    result.delete(0, END)
    size_entry.delete(0, END)


# Title
Label(window,
      text="Password Generator",
      font=("Arial", 20),
      bg="lightblue").pack(pady=20)


# Password length
Label(window,
      text="Enter Password Length",
      font=("Arial", 12),
      bg="lightblue").pack()

size_entry = Entry(window,
                   font=("Arial", 15),
                   justify="center")
size_entry.pack(pady=10)


# Result
result = Entry(window,
               font=("Arial", 15),
               justify="center")
result.pack(pady=15)


# Buttons
Button(window,
       text="Generate Password",
       font=("Arial", 12),
       command=generate).pack(pady=5)


Button(window,
       text="Clear",
       font=("Arial", 12),
       command=clear).pack(pady=5)


# Name
Label(window,
      text="Created by Shradha Yadav",
      bg="lightblue",
      font=("Arial", 10)).pack(side=BOTTOM, pady=10)


window.mainloop()