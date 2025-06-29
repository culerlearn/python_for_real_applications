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


def save_expenses():
    if not expense_list:
        messagebox.showinfo("Notice", "No expenses to save.")
        return
    with open("expenses.csv", "w") as file:
        for item, amount in expense_list:
            file.write(f"{item},{amount}")
    messagebox.showinfo("Saved", "Expenses saved to expenses.csv.")


def load_expenses():
    try:
        with open("expenses.csv", "r") as file:
            expense_list.clear()
            expense_box.delete(0, tk.END)
            for line in file:
                item, amount = line.strip().split(",")
                expense_list.append((item, float(amount)))
                expense_box.insert(tk.END, f"{item} - ₦{amount}")
        messagebox.showinfo("Loaded", "Expenses loaded.")
    except FileNotFoundError:
        messagebox.showerror("Error", "expenses.csv not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not load data: {e}")


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
tk.Button(root, text="Save", command=save_expenses).pack(pady=5)
tk.Button(root, text="Load", command=load_expenses).pack(pady=5)

# Listbox to display items
expense_box = tk.Listbox(root, width=40)
expense_box.pack(pady=10)

root.mainloop()

############
