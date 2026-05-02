import tkinter as tk
from tkinter import ttk

transactions = [
    (749.17, "Investment Return"),
    (-11.54, "Utilities"),
    (-247.58, "Online Shopping"),
    (981.17, "Investment Return"),
    (-410.65, "Rent"),
    (310.60, "Rent"),
    (563.70, "Gift"),
    (220.79, "Salary"),
    (-49.85, "Car Maintenance"),
    (308.49, "Salary"),
    (-205.55, "Car Maintenance"),
    (870.64, "Salary"),
    (-881.51, "Utilities"),
    (518.14, "Salary"),
    (-264.66, "Groceries"),
]

starting_balance = 2450.00


def calculate_balance():
    total = starting_balance
    for amount, _ in transactions:
        total += amount
    return total


def calculate_income():
    return sum(amount for amount, _ in transactions if amount > 0)


def calculate_expenses():
    return sum(amount for amount, _ in transactions if amount < 0)


root = tk.Tk()
root.title("Rustic Bank Dashboard")
root.geometry("760x560")
root.configure(bg="#1f1712")
root.resizable(False, False)

root.lift()
root.focus_force()

title = tk.Label(
    root,
    text="Rustic Bank",
    font=("Georgia", 28, "bold"),
    bg="#1f1712",
    fg="#f4d35e"
)
title.pack(pady=(20, 5))

subtitle = tk.Label(
    root,
    text="Personal Finance Dashboard",
    font=("Georgia", 12),
    bg="#1f1712",
    fg="#d8c3a5"
)
subtitle.pack(pady=(0, 20))

cards_frame = tk.Frame(root, bg="#1f1712")
cards_frame.pack(pady=10)

def create_card(parent, title, value):
    card = tk.Frame(parent, bg="#3b2f2f", width=210, height=100, highlightbackground="#8b5e34", highlightthickness=2)
    card.pack(side="left", padx=10)
    card.pack_propagate(False)

    tk.Label(
        card,
        text=title,
        font=("Georgia", 11),
        bg="#3b2f2f",
        fg="#d8c3a5"
    ).pack(pady=(15, 5))

    tk.Label(
        card,
        text=value,
        font=("Georgia", 18, "bold"),
        bg="#3b2f2f",
        fg="#fff3b0"
    ).pack()

create_card(cards_frame, "Current Balance", f"${calculate_balance():,.2f}")
create_card(cards_frame, "Total Income", f"${calculate_income():,.2f}")
create_card(cards_frame, "Total Expenses", f"${abs(calculate_expenses()):,.2f}")

table_frame = tk.Frame(root, bg="#1f1712")
table_frame.pack(pady=25)

style = ttk.Style()
style.theme_use("default")
style.configure(
    "Treeview",
    background="#2f241f",
    foreground="#f7ede2",
    rowheight=28,
    fieldbackground="#2f241f",
    font=("Georgia", 10)
)
style.configure(
    "Treeview.Heading",
    background="#8b5e34",
    foreground="white",
    font=("Georgia", 11, "bold")
)

table = ttk.Treeview(
    table_frame,
    columns=("amount", "category", "type"),
    show="headings",
    height=10
)

table.heading("amount", text="Amount")
table.heading("category", text="Category")
table.heading("type", text="Type")

table.column("amount", width=160, anchor="center")
table.column("category", width=260, anchor="center")
table.column("type", width=160, anchor="center")

table.pack()

for amount, category in transactions:
    transaction_type = "Deposit" if amount > 0 else "Withdrawal"
    table.insert(
        "",
        "end",
        values=(f"${amount:,.2f}", category, transaction_type)
    )

footer = tk.Label(
    root,
    text="Demo banking dashboard using fake transaction data",
    font=("Georgia", 10),
    bg="#1f1712",
    fg="#a68a64"
)
footer.pack(pady=10)

root.mainloop()