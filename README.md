****Rocket League Automation Script****
This script automates the process of opening OBS Studio, BakkesMod, focusing on the Rocket League window, and running specific commands within Rocket League using pyautogui.

How it works
Import Libraries: The script imports necessary libraries such as tkinter for creating the GUI, os for system operations, subprocess for running commands, pyautogui for GUI automation, and win32gui and win32con for managing windows.

Window Management Functions:

find_window_by_title(title): Finds a window by its title and brings it to the foreground.
open_obs(): Opens OBS Studio using the system command.
open_bakkes_mod(): Opens BakkesMod using subprocess.
Running Commands in Console:

open_console_and_run_node(): Opens a command prompt, runs a Node.js script, and simulates pressing Enter using pyautogui.
Main Function:

open_apps_and_run_commands(): Executes the above functions in sequence, waits for each process to complete, and performs GUI automation within Rocket League.
Graphical User Interface (GUI):

The script creates a simple GUI using tkinter with a label instructing the user to open Rocket League first and a button to initiate the automation process.
Usage
Ensure Python and required libraries are installed (tkinter, pyautogui, win32gui, win32con).
Run the script.
Click the "Automate Rocket League" button on the GUI after opening Rocket League.
Note
Make sure to adjust the file paths and sleep times in the code according to your system and requirements.
This script relies on GUI automation and may not work reliably if window positions or sizes change.
