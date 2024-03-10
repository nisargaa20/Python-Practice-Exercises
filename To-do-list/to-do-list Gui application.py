import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        todo_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a task from the list
def remove_task():
    try:
        selected_index = todo_list.curselection()[0]
        todo_list.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Function to move a task up in the list
def move_up():
    try:
        selected_index = todo_list.curselection()[0]
        if selected_index > 0:
            task = todo_list.get(selected_index)
            todo_list.delete(selected_index)
            todo_list.insert(selected_index - 1, task)
            todo_list.selection_set(selected_index - 1)
    except IndexError:
        pass

# Function to move a task down in the list
def move_down():
    try:
        selected_index = todo_list.curselection()[0]
        if selected_index < todo_list.size() - 1:
            task = todo_list.get(selected_index)
            todo_list.delete(selected_index)
            todo_list.insert(selected_index + 1, task)
            todo_list.selection_set(selected_index + 1)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create input field and buttons
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=5, pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.grid(row=1, column=0, padx=5, pady=5)

up_button = tk.Button(root, text="Move Up", command=move_up)
up_button.grid(row=1, column=1, padx=5, pady=5)

down_button = tk.Button(root, text="Move Down", command=move_down)
down_button.grid(row=1, column=2, padx=5, pady=5)

# Create listbox to display tasks
todo_list = tk.Listbox(root, width=50)
todo_list.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Run the main event loop
root.mainloop()
