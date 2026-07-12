import tkinter as tk

# Create the main window
root = tk.Tk()

# Window title
root.title("To-Do List Application")

# Window size
root.geometry("700x500")

# Prevent resizing
root.resizable(False, False)

# Heading
heading = tk.Label(
    root,
    text="TO-DO LIST APPLICATION",
    font=("Arial", 22, "bold")
)
heading.pack(pady=20)

# Run the application
root.mainloop()
