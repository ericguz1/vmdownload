import tkinter as tk
from tkinter import simpledialog, messagebox
import pyautogui
import time

# Function to handle the password prompt and blocking behavior
def lock_screen():
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # Make window full screen
    root.attributes('-topmost', True)  # Keep window on top of all others
    root.protocol("WM_DELETE_WINDOW", disable_event)  # Disable the close button

    label = tk.Label(root, text="Uh oh, you've been hacked!", font=("Arial", 24))
    label.pack(pady=100)

    password = simpledialog.askstring("Password", "Enter password to unlock:", show='*')
    
    if password == "water":
        messagebox.showinfo("Success", "Unlocked!")
        root.destroy()  # Close the window if the password is correct
    else:
        messagebox.showerror("Error", "Incorrect password!")
        lock_screen()  # Keep asking for the password if incorrect

    root.mainloop()

# Disable close event to prevent window closure
def disable_event():
    pass

# Add a delay before executing
time.sleep(2)

# Run the lock screen
lock_screen()
