import tkinter as tk
from tkinter import ttk


def add():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


def remove():
    selected_task = listbox.curselection()
    if selected_task:
        index = int(selected_task[0])
        del tasks[index]
        listbox.delete(index)


app = tk.Tk()
app.title("To-Do App")

m_frame = ttk.Frame(app)
m_frame.pack(padx=10, pady=10)

tasks = []

listbox = tk.Listbox(m_frame, font=("Calipri", 15), bg="gray30", fg="white")
listbox.pack()

entry = tk.Entry(app, width=20, bg="black", fg="white", font=("Arial", 15))
entry.pack()

b_add = tk.Button(m_frame, text="Add New Task", command=add, width = 30)
b_add.pack()

b_del = tk.Button(m_frame, text="Delete Task", command=remove,width = 30)
b_del.pack()

app.mainloop()
