import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Basic GUI Example")
root.geometry("400x300")

# Label
label = ttk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Entry
entry = ttk.Entry(root, width=30)
entry.pack(pady=5)

# Function for button click
def on_submit():
    name = entry.get()
    result_label.config(text=f"Hello, {name}!")

# Button
submit_btn = ttk.Button(root, text="Submit", command=on_submit)
submit_btn.pack(pady=10)

# Result label
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

# Checkbutton
check_var = tk.BooleanVar()
check = ttk.Checkbutton(root, text="Subscribe to newsletter", variable=check_var)
check.pack(pady=5)

# Radio buttons
radio_var = tk.StringVar(value="A")
ttk.Radiobutton(root, text="Option A", variable=radio_var, value="A").pack()
ttk.Radiobutton(root, text="Option B", variable=radio_var, value="B").pack()

# Combobox (dropdown)
combo = ttk.Combobox(root, values=["Item 1", "Item 2", "Item 3"])
combo.pack(pady=10)
combo.current(0)

root.mainloop()