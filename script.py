import time
import pyautogui

# Function to simulate the DuckyScript behavior
def open_cmd_and_run_python():
    # Wait for half a second to ensure system is ready
    time.sleep(0.5)
    
    # Simulate Windows key + R to open the Run dialog
    pyautogui.hotkey('win', 'r')
    
    # Wait for the Run dialog to open
    time.sleep(0.5)
    
    # Type "cmd" to open Command Prompt
    pyautogui.write('cmd')
    
    # Press Enter to open Command Prompt
    pyautogui.press('enter')
    
    # Wait for the Command Prompt to open
    time.sleep(0.5)
    
    # Type the Python command
    pyautogui.write('python -c "import pyautogui; print(\'ABCDEFGHI\')"')
    
    # Press Enter to execute the command
    pyautogui.press('enter')

# Run the function
open_cmd_and_run_python()

