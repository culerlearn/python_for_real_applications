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
