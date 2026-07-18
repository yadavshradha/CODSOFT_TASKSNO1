from tkinter import *

window = Tk()
window.title("My Calculator")
window.state("zoomed")   # Full screen
window.config(bg="lightblue")


# Display screen
screen = Entry(window, font=("Calibri", 30), bd=5, justify="right")
screen.pack(fill=X, padx=50, pady=40, ipady=20)


def press(num):
    screen.insert(END, num)


def solve():
    try:
        result = eval(screen.get())
        screen.delete(0, END)
        screen.insert(0, result)
    except:
        screen.delete(0, END)
        screen.insert(0, "Error")


def clear_screen():
    screen.delete(0, END)


# Button area
button_frame = Frame(window, bg="lightblue")
button_frame.pack(expand=True)


buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]


row = 0
col = 0

for item in buttons:

    if item == "=":
        Button(button_frame,
               text=item,
               font=("Calibri", 25),
               width=8,
               height=2,
               command=solve).grid(row=row, column=col, padx=10, pady=10)

    else:
        Button(button_frame,
               text=item,
               font=("Calibri", 25),
               width=8,
               height=2,
               command=lambda x=item: press(x)).grid(row=row, column=col, padx=10, pady=10)

    col += 1

    if col == 4:
        col = 0
        row += 1


# Clear button
Button(window,
       text="Clear",
       font=("Calibri", 20),
       width=15,
       height=2,
       bg="orange",
       command=clear_screen).pack(pady=20)


window.mainloop()