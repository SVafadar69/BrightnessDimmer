import ctypes
import time
import keyboard
import os
from playsound import playsound

# Define the Windows API functions
SetMonitorBrightness = ctypes.windll.dxva2.SetMonitorBrightness
GetPhysicalMonitorsFromHMONITOR = ctypes.windll.dxva2.GetPhysicalMonitorsFromHMONITOR
GetMonitorBrightness = ctypes.windll.dxva2.GetMonitorBrightness
LockWorkStation = ctypes.windll.user32.LockWorkStation

# Constants
NULL = 0
MONITOR_DEFAULTTOPRIMARY = 1
BRIGHTNESS_DIM = 0
BREAK_INTERVAL = 20 * 60  # 20 minutes in seconds

# Get the handle to the primary monitor
hMonitor = ctypes.windll.user32.MonitorFromWindow(NULL, MONITOR_DEFAULTTOPRIMARY)

# Get the physical monitors from the handle
physical_monitor_array = ctypes.POINTER(ctypes.c_void_p)()
GetPhysicalMonitorsFromHMONITOR(hMonitor, 1, ctypes.byref(physical_monitor_array))

# Get the handle to the first physical monitor
hPhysicalMonitor = physical_monitor_array.contents.value

# Define the path to the background music file
music_file_path = "path/to/your/music/file.mp3"

# Function to lock the keys
def lock_keys():
    keyboard.block_all()

# Function to play background music
def play_music():
    playsound(music_file_path)

# Function to dim the screen brightness
def dim_screen():
    SetMonitorBrightness(hPhysicalMonitor, BRIGHTNESS_DIM)

# Main loop
while True:
    # Dim the screen brightness
    dim_screen()

    # Lock the keys
    lock_keys()

    # Play background music
    play_music()

    # Wait for the break interval
    time.sleep(BREAK_INTERVAL)

    # Restore the screen brightness
    SetMonitorBrightness(hPhysicalMonitor, 100)

    # Unblock the keys
    keyboard.unblock_all()

    # Stop the background music
    os.system("taskkill /im wmplayer.exe /f")  # Terminate Windows Media Player process

    # Wait for a few seconds before starting the next break interval
    time.sleep(5)
