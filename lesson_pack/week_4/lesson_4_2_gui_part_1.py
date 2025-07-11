# Lesson 4.2 GUI App - Part 1: Introduction to GUI with Tkinter

# Creating Your First Tkinter Window   ##################################################
# import tkinter as tk
#
# root = tk.Tk()
# root.title("My First GUI App")
# root.geometry("400x300")
#
# root.mainloop()

# Adding Components (Widgets)  #########################################################
import tkinter as tk
from tkinter import messagebox


def greet_user():
    name = name_entry.get()
    messagebox.showinfo("Greeting", f"Hello, {name}!")


# Create main window
root = tk.Tk()
root.title("Basic GUI")
root.geometry("500x350")

# Add widgets
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

name_entry = tk.Entry(root, width=30)
name_entry.pack()

greet_button = tk.Button(root, text="Greet Me", command=greet_user)
greet_button.pack(pady=20)

root.mainloop()

# Adding Components (Widgets)  #########################################################

import tkinter as tk

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x400")

# Entry for item name
tk.Label(root, text="Item:").pack()
item_entry = tk.Entry(root)
item_entry.pack()
# Entry for amount

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()  # Action Buttons (logic will be added soon!)
tk.Button(root, text="Add Expense").pack(pady=5)
tk.Button(root, text="Save").pack(pady=5)
tk.Button(root, text="Load").pack(pady=5)
# Listbox to display items
expense_box = tk.Listbox(root, width=40)
expense_box.pack(pady=10)

root.mainloop()
