## Rocket League Overlay

This script automates the process of setting up OBS Studio, launching BakkesMod, focusing on the Rocket League window, and executing specific commands within Rocket League using pyautogui.

### How it works

Import Libraries: The script imports necessary libraries such as tkinter for creating the GUI, os for system operations, subprocess for running commands, pyautogui for GUI automation, and win32gui and win32con for managing windows.

### Window Management Functions:

find_window_by_title(title): Locates a window by its title and brings it to the forefront.
open_obs(): Launches OBS Studio using the system command.
open_bakkes_mod(): Opens BakkesMod via subprocess.

### Running Commands in Console:

open_console_and_run_node(): Initiates a command prompt, navigates to a specific file path, connects to the relay server via node.js, and completes the required prompts.

### Main Function:

open_apps_and_run_commands(): Executes the aforementioned functions in sequence, waits for each process to complete, and performs GUI automation within Rocket League.
Graphical User Interface 

### (GUI):

The script generates a simple GUI using tkinter with a label instructing the user to open Rocket League first and a button to start the automation process.

### Usage

Ensure Python and the required libraries (tkinter, pyautogui, win32gui, win32con) are installed.
Run the script.
Click the "Run Overlay" button on the GUI after launching Rocket League.

### Note

Ensure to adjust the file paths and sleep times in the code according to your system and requirements. This script relies on GUI automation and may not work reliably if window positions or sizes change.