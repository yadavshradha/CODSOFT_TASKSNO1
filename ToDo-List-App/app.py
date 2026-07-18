import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import date


FILE_NAME = "tasks.json"


# ---------------- Data Handling ----------------

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# ---------------- Functions ----------------

def add_task():
    title = task_entry.get()

    if title == "":
        messagebox.showwarning("Warning", "Enter task name")
        return

    task = {
        "title": title,
        "category": category_var.get(),
        "priority": priority_var.get(),
        "completed": False
    }

    tasks.append(task)
    save_tasks()

    task_entry.delete(0, tk.END)
    show_tasks()


def show_tasks():
    task_list.delete(*task_list.get_children())

    for index, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"

        task_list.insert(
            "",
            tk.END,
            iid=index,
            values=(
                task["title"],
                task["category"],
                task["priority"],
                status
            )
        )

    update_count()


def edit_task():
    selected = task_list.selection()

    if not selected:
        messagebox.showwarning("Warning", "Please select a task.")
        return

    index = int(selected[0])

    title = task_entry.get().strip()

    if title == "":
        messagebox.showwarning("Warning", "Enter task name.")
        return

    tasks[index]["title"] = title
    tasks[index]["category"] = category_var.get()
    tasks[index]["priority"] = priority_var.get()

    save_tasks()
    show_tasks()

    task_entry.delete(0, tk.END)
    
def delete_task():
    selected = task_list.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task")
        return

    index = int(selected[0])

    tasks.pop(index)

    save_tasks()
    show_tasks()


def mark_completed():
    selected = task_list.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task")
        return

    index = int(selected[0])

    tasks[index]["completed"] = True

    save_tasks()
    show_tasks()


def update_count():

    total = len(tasks)

    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    pending = total - completed

    count_label.config(
        text=f"Total Tasks: {total}     Completed: {completed}     Pending: {pending}"
    )


# ---------------- GUI ----------------

root = tk.Tk()

root.title("LifeFlow - Daily Planner")
root.geometry("750x600")
root.resizable(False, False)


tasks = load_tasks()


# Title

title = tk.Label(
    root,
    text="LifeFlow - Daily Planner",
    font=("Arial", 22, "bold")
)

title.pack(pady=10)


# Date

date_label = tk.Label(
    root,
    text="Date: " + str(date.today()),
    font=("Arial", 12)
)

date_label.pack()


# Input Frame

input_frame = tk.Frame(root)

input_frame.pack(pady=15)


tk.Label(
    input_frame,
    text="Task Name:"
).grid(row=0, column=0)


task_entry = tk.Entry(
    input_frame,
    width=30
)

task_entry.grid(row=0, column=1, padx=10)



# Category

tk.Label(
    input_frame,
    text="Category:"
).grid(row=1,column=0,pady=5)


category_var = tk.StringVar()

category_box = ttk.Combobox(
    input_frame,
    textvariable=category_var,
    values=[
        "Study",
        "Work",
        "Shopping",
        "Health",
        "Personal",
        "Travel"
    ]
)

category_box.current(0)

category_box.grid(
    row=1,
    column=1
)



# Priority

tk.Label(
    input_frame,
    text="Priority:"
).grid(row=2,column=0,pady=5)


priority_var = tk.StringVar()

priority_box = ttk.Combobox(
    input_frame,
    textvariable=priority_var,
    values=[
        "High",
        "Medium",
        "Low"
    ]
)

priority_box.current(1)

priority_box.grid(
    row=2,
    column=1
)



# Buttons with colors

button_frame = tk.Frame(root)

button_frame.pack(pady=10)


tk.Button(
    button_frame,
    text="Add Task",
    width=15,
    command=add_task,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold")
).grid(row=0,column=0,padx=5)



tk.Button(
    button_frame,
    text="Edit Task",
    width=15,
    command=edit_task,
    bg="#2196F3",
    fg="white",
    font=("Arial", 10, "bold")
).grid(row=0,column=1,padx=5)



tk.Button(
    button_frame,
    text="Delete Task",
    width=15,
    command=delete_task,
    bg="#F44336",
    fg="white",
    font=("Arial", 10, "bold")
).grid(row=0,column=2,padx=5)



tk.Button(
    button_frame,
    text="Mark Completed",
    width=15,
    command=mark_completed,
    bg="#FF9800",
    fg="white",
    font=("Arial", 10, "bold")
).grid(row=0,column=3,padx=5)



# Table

columns = (
    "Task",
    "Category",
    "Priority",
    "Status"
)


task_list = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=12
)


for col in columns:
    task_list.heading(
        col,
        text=col
    )

    task_list.column(
        col,
        width=150
    )


task_list.pack(pady=15)



# Count

count_label = tk.Label(
    root,
    text="",
    font=("Arial",12,"bold")
)

count_label.pack()


show_tasks()


root.mainloop()