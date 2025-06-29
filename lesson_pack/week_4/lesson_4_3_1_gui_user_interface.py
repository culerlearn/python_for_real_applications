import tkinter as tk
from tkinter import messagebox

# Initial User Interface (UI) ###########################################
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
amount_entry.pack()

# Action Buttons (logic will be added soon!)
tk.Button(root, text="Add Expense").pack(pady=5)
tk.Button(root, text="Save").pack(pady=5)
tk.Button(root, text="Load").pack(pady=5)

# Listbox to display items
expense_box = tk.Listbox(root, width=40)
expense_box.pack(pady=10)

root.mainloop()

############
