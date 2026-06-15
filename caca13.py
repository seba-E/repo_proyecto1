import tkinter as tk
from tkinter import ttk
import ctypes

# Tell Windows this app is DPI-aware (must be done BEFORE creating the window)
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # 1 = system DPI aware
    # Or use 2 for per-monitor DPI awareness (better for multi-monitor setups):
    # ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    pass

root = tk.Tk()
root.title("Crisp GUI Example")

# Get the actual scaling factor and apply it to Tk's scaling
scale_factor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
root.tk.call('tk', 'scaling', scale_factor)

root.geometry("800x600")

label = ttk.Label(root, text="Enter your name:", font=("Segoe UI", 11))
label.pack(pady=10)

entry = ttk.Entry(root, width=30, font=("Segoe UI", 11))
entry.pack(pady=5)

def on_submit():
    result_label.config(text=f"Hello, {entry.get()}!")

submit_btn = ttk.Button(root, text="Submit", command=on_submit)
submit_btn.pack(pady=10)

result_label = ttk.Label(root, text="", font=("Segoe UI", 11))
result_label.pack(pady=10)

root.mainloop()