import tkinter as tk
from tkinter import messagebox

# Initial User Interface (UI) ###########################################
import tkinter as tk

from tkinter import messagebox

expense_list = []


def add_expense():
    item = item_entry.get()
    amount = amount_entry.get()
    try:
        expense_list.append((item, float(amount)))
        expense_box.insert(tk.END, f"{item} - ₦{amount}")
        item_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number.")


##############################
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

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=5)
tk.Button(root, text="Save").pack(pady=5)
tk.Button(root, text="Load").pack(pady=5)

# Listbox to display items
expense_box = tk.Listbox(root, width=40)
expense_box.pack(pady=10)

root.mainloop()

############
