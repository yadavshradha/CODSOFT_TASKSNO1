from tkinter import *
import random
import string


window = Tk()
window.title("Password Generator")

# Full Screen
window.attributes("-fullscreen", True)

window.config(bg="lightblue")


def generate():
    length = length_box.get()

    if length.isdigit():
        length = int(length)

        characters = string.ascii_letters + string.digits + "!@#$%&*"

        password = ""

        for i in range(length):
            password += random.choice(characters)

        result.delete(0, END)
        result.insert(0, password)

    else:
        result.delete(0, END)
        result.insert(0, "Enter number")


def clear():
    length_box.delete(0, END)
    result.delete(0, END)


def exit_screen():
    window.attributes("-fullscreen", False)


# Title
Label(window,
      text="Password Generator",
      font=("Arial", 40),
      bg="lightblue").pack(pady=60)


# Input
Label(window,
      text="Enter Password Length",
      font=("Arial", 25),
      bg="lightblue").pack()

length_box = Entry(window,
                   font=("Arial", 25),
                   justify="center")
length_box.pack(pady=20)


# Output
Label(window,
      text="Generated Password",
      font=("Arial", 25),
      bg="lightblue").pack()

result = Entry(window,
               font=("Arial", 25),
               justify="center",
               width=25)
result.pack(pady=30)


# Buttons
Button(window,
       text="Generate Password",
       font=("Arial", 20),
       width=20,
       height=2,
       command=generate).pack(pady=10)


Button(window,
       text="Clear",
       font=("Arial", 20),
       width=20,
       height=2,
       command=clear).pack(pady=10)


Button(window,
       text="Exit Full Screen",
       font=("Arial", 15),
       command=exit_screen).pack(pady=20)


# Creator Name
Label(window,
      text="Created by Shradha Yadav",
      font=("Arial", 18),
      bg="lightblue").pack(side=BOTTOM, pady=20)


window.mainloop()
