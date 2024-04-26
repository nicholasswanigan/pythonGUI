# Rocket League Overlay README

## Introduction

This script automates the process of setting up OBS Studio, launching BakkesMod, focusing on the Rocket League window, and executing specific commands within Rocket League all in an attempt to provide live rendering of everyone's stats for a more interactive viewing experience.

## Installation

1. **Download Game Launcher**
   - Download Epic Games or a compatible game launcher to download and launch Rocket League.

2. **Download Components**
   - Download the following components:
     - BakkesMod.zip
     - Node.js
     - OBS Studio
     - Python GUI
     - Rocket_League_Overlay

3. **USB Drive Setup**
   - Plugin a USB drive and reformat it:
     - Right-click on the USB drive, format it with exFAT (Default) file system, and name it "K" (D: drive type).

4. **Extract Components**
   - Extract all downloaded components to the formatted USB drive.

## Usage

1. **Launch Rocket League**
   - Open Rocket League to reach the main intro screen.

2. **Run Overlay**
   - Navigate to the USB drive location and run the main program (double-click).

3. **Handling Issues**
   - Ensure Caps Lock is off.
   - Don't touch anything after pressing the "Run Overlay" button until OBS Studio pops up.
   - If anything goes wrong, close everything except Rocket League and return to the main screen.

4. **Running the Overlay**
   - Click the "Run Overlay" button in the main program (blue feather icon).
   - Wait for OBS Studio to open.
   - In Rocket League, a black window should open with the text "plugin load sos" (press F6 and type manually if not).
   - Click next to the text and press Enter.
   - Close the black window.
   - In OBS Studio, refresh the overlay source in the quick edit toolbar under the main display screen.
   	- In testing we did find we needed to change the source of overlay to this <file:///D:/Rocket_League_Overlay/Rocket%20League%20DO/Rocket%20League%20Dynamic%20Overlay/overlay.html> (without the <>) this is because we changed that location of the relay server last min. 
   - The sence should be set for you to join the match.

## Post-Game Actions

After the game ends:
- Display a winning screen or hide the overlay to use default winning animations.
	- There will be a full-screen stat sheet after everygame so you will have time to make adjustments in OBS Studio.

## Components

1. **Node.js Instance**
   - Node.js is a JavaScript runtime used to build server-side applications.

2. **OBS Studio**
   - OBS Studio is used for video recording and live streaming.

3. **BakkesMod**
   - BakkesMod is a third-party mod for Rocket League, providing additional features and functionality.

4. **Rocket_League_Overlay (JavaScript)**
   - This component is a self-built JavaScript overlay for displaying real-time stats in Rocket League.

5. **pythonGUI (Python Code)**
   - The pythonGUI component contains the main Python code for controlling and managing the overlay.

6. **Main Program**
   - The main program wraps up all components and orchestrates their interactions.

## Making Changes 

1. **Changing the RunOverlay GUI**
   - Open the pythonGUI code in a code editor and then rebuild the program after your done

2. **Changing the Overlay Style**
   - Drill into the Rocket_League_Overlay folder and open the "D:\Rocket_League_Overlay\Rocket League DO\Rocket League Dynamic Overlay" in a code editor and make changes through there

## Support and Feedback

For questions or if issues arise feel free to email myself or one of contibuter:

Nick Swanigan (nickswanigan04@gmail.com)

We will be working on improvements and better designs within the code this summer (2024)
