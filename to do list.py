# gui_todo.py
import tkinter as tk
from tkinter import messagebox
import sqlite3

def connect_db():
    return sqlite3.connect('tasks.db')

def add_task(title, description, priority, due_date, category):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
    INSERT INTO tasks (title, description, priority, due_date, category, completed)
    VALUES (?, ?, ?, ?, ?, 0)
    ''', (title, description, priority, due_date, category))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Task added successfully!")

# Define other functions as needed for the GUI

def main():
    root = tk.Tk()
    root.title("To-Do List App")
    
    # Add widgets for task input
    tk.Label(root, text="Title").grid(row=0, column=0)
    title_entry = tk.Entry(root)
    title_entry.grid(row=0, column=1)

    tk.Label(root, text="Description").grid(row=1, column=0)
    description_entry = tk.Entry(root)
    description_entry.grid(row=1, column=1)

    tk.Label(root, text="Priority").grid(row=2, column=0)
    priority_entry = tk.Entry(root)
    priority_entry.grid(row=2, column=1)

    tk.Label(root, text="Due Date").grid(row=3, column=0)
    due_date_entry = tk.Entry(root)
    due_date_entry.grid(row=3, column=1)

    tk.Label(root, text="Category").grid(row=4, column=0)
    category_entry = tk.Entry(root)
    category_entry.grid(row=4, column=1)

    def add_task_wrapper():
        add_task(
            title_entry.get(),
            description_entry.get(),
            int(priority_entry.get()),
            due_date_entry.get(),
            category_entry.get()
        )

    tk.Button(root, text="Add Task", command=add_task_wrapper).grid(row=5, columnspan=2)

    # Add other GUI elements as needed

    root.mainloop()

if __name__ == "__main__":
    main()
