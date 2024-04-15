import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import pyautogui
import time
import win32gui
import win32con

# Finds window by its title
def find_window_by_title(title):
    try:
        hwnd = win32gui.FindWindow(None, title)
        if hwnd:
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            win32gui.SetForegroundWindow(hwnd)
        return hwnd
    except Exception as e:
        print("Error:", e)
        return None


# Opens OBS
def open_obs():
    os.system("start /d \"C:\\Program Files\\obs-studio\\bin\\64bit\" obs64.exe")

# Opens BakkesMod
def open_bakkes_mod():
    os.system("start /d \"C:\\Program Files\\BakkesMod\" BakkesMod.exe")

# Opens command prompt, navigates to file path, connects to the relay server via node, and completes the prompts
def open_console_and_run_node():
    try:
        relay_path = r"C:\Users\{}\Documents\Rocket_League_Overlay\Rocket League DO\relayserverandplugin\SOS Relay Server (run in cmd with node)\sos-ws-relay-master".format(
            os.getlogin())

        # Construct the command to change directory and run node.js
        command = 'cmd /k "cd {} && node ./ws-relay.js"'.format(relay_path)

        # Open command prompt and run node.js
        os.system("start " + command)

        # Simulate pressing Enter 3 times
        for _ in range(4):
            pyautogui.press('enter')
            time.sleep(1)

    except Exception as ex:
        print("Error:", ex)

# Finds Rocket League window based on window title text
def focus_rocket_league_window():
    rocket_league_title = "Rocket League (64-bit, DX11, Cooked)"
    find_window_by_title(rocket_league_title)

def open_apps_and_run_commands():
    open_console_and_run_node()  # Run Node.js script first

    open_bakkes_mod()
    time.sleep(11)  # Wait for BakkesMod to inject DLL files

    focus_rocket_league_window()  # Bring Rocket League window to foreground
    time.sleep(10)  # Wait for BakkesMod to fully integrate with Rocket League

    # Run F6 command
    pyautogui.press('f6')
    time.sleep(1)  # Wait for F6 command to run

    # Types out "plugin load sos"
    # Must be done this way or you risk missing letters by entering in all at once
    command = "plugin load sos"
    for c in command:
        pyautogui.press(c)
        time.sleep(0.1)

    pyautogui.press('enter') #not working

    open_obs()

# Create GUI
root = tk.Tk()
root.title("OTC eSports Rocket League Overlay")

# Set the initial size of the window
root.geometry("400x100")

# Add label
label_text = tk.StringVar(value="Run Overlay")
label = tk.Label(root, textvariable=label_text, pady=10)
label.pack()

# Function to update label text and run commands
def update_label_and_run_commands():
    label_text.set("Building overlay... \n\n Please wait for OBS")
    root.update_idletasks()  # Update GUI to show the new label text
    open_apps_and_run_commands()

# Add button
button = tk.Button(root, text="Run Overlay", command=update_label_and_run_commands)
button.pack()


# Run the GUI
root.mainloop()
