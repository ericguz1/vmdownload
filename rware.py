import pyautogui
import time

# Wait a moment before executing
time.sleep(2)

# Open a message box indicating the system has been hacked
pyautogui.alert("Uh oh, you've been hacked!", "Ransomware")

# Ask for the password
password = pyautogui.password("Enter password to unlock:")

# Check if the password is correct
if password == "water":
    pyautogui.alert("Unlocked!", "Success")
else:
    pyautogui.alert("Incorrect password!", "Error")
