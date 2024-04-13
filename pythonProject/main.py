import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import pyautogui
import time
import win32gui
import win32con

def find_window_by_title(title):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
    return hwnd

def open_obs():
    os.system("start /d \"C:\\Program Files\\obs-studio\\bin\\64bit\" obs64.exe")

def open_bakkes_mod():
    subprocess.Popen([r"C:\Program Files\BakkesMod\BakkesMod.exe"])

def open_console_and_run_node():
    try:
        # Get the current user's username
        username = os.getlogin()

        # Construct the relay path
        relay_path = r"C:\Users\{}\Documents\Rocket League Dynamic Overlay\overlay.html".format(username)

        # Construct the command to run Node.js in the command prompt
        command = 'start /d "{}" cmd /k node ./ws-relay.js'.format(relay_path)

        # Use subprocess to open a command prompt and run the command
        subprocess.Popen(['cmd.exe', '/c', command])
        time.sleep(3)  # Wait for the command prompt to open and Node.js script to run

        # Simulate pressing Enter using pyautogui
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')

    except Exception as ex:
        ex.printStackTrace()
        messagebox.showerror("Error", "Error executing commands: " + str(ex))

def open_apps_and_run_commands():
    open_console_and_run_node()  # Run Node.js script first
    time.sleep(5)  # Wait for Node.js script to start (adjust as needed)

    open_obs()
    time.sleep(5)  # Wait for OBS Studio to open
    open_bakkes_mod()
    time.sleep(5)  # Wait for BakkesMod to open

    rocket_league_title = "Rocket League (64-bit, DX11, Cooked)"
    rocket_league_hwnd = find_window_by_title(rocket_league_title)

    if not rocket_league_hwnd:
        messagebox.showerror("Error", "Rocket League window not found. Open Rocket League first.")
        return

    time.sleep(1)  # Wait for window activation

    # Run F6 command and subsequent commands
    pyautogui.press('f6')
    time.sleep(1)  # Wait for F6 command to run
    pyautogui.typewrite('plugin')
    time.sleep(1)  # Adjust sleep time as needed
    pyautogui.typewrite(' load')
    time.sleep(1)  # Adjust sleep time as needed
    pyautogui.typewrite(' sos')
    time.sleep(3)  # Wait after typing 'sos'

    pyautogui.press('enter')

# Create GUI
root = tk.Tk()
root.title("Rocket League Automation")

# Add label
label = tk.Label(root, text="Please open Rocket League first.", pady=10)
label.pack()

# Add button
button = tk.Button(root, text="Automate Rocket League", command=open_apps_and_run_commands)
button.pack()

# Run the GUI
root.mainloop()
