import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "students.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    name = entry_name.get()
    roll = entry_roll.get()
    marks = entry_marks.get()

    if name == "" or roll == "" or marks == "":
        messagebox.showerror("Error", "All fields are required")
        return

    students = load_data()
    students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })
    save_data(students)

    messagebox.showinfo("Success", "Student Added Successfully")

    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    entry_marks.delete(0, tk.END)

def view_students():
    students = load_data()
    text_area.delete("1.0", tk.END)

    if not students:
        text_area.insert(tk.END, "No students found")
        return

    for s in students:
        text_area.insert(
            tk.END,
            f"Name: {s['name']} | Roll: {s['roll']} | Marks: {s['marks']}\n"
        )

# -------- GUI DESIGN --------

root = tk.Tk()
root.title("Student Management System")
root.geometry("500x450")

tk.Label(root, text="Student Management System", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Roll Number").pack()
entry_roll = tk.Entry(root)
entry_roll.pack()

tk.Label(root, text="Marks").pack()
entry_marks = tk.Entry(root)
entry_marks.pack()

tk.Button(root, text="Add Student", command=add_student).pack(pady=10)
tk.Button(root, text="View Students", command=view_students).pack()

text_area = tk.Text(root, height=10)
text_area.pack(pady=10)

root.mainloop()
