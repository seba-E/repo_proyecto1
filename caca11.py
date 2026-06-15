import tkinter as tk
import ctypes

# Fix blurry windows on Windows 8 / 10 / 11
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    # Fallback for older Windows setups
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except:
        pass

root = tk.Tk()
root.geometry("400x300")

label = tk.Label(root, text="Crisp High-Resolution Text", font=("Arial", 14))
label.pack(pady=20)

root.mainloop()
