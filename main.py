import ctypes
import pywintypes
import time
import keyboard
from keyboard import block_key
import os
from playsound import playsound
import screen_brightness_control as sbc


# Constants
brightness = sbc.get_brightness()
# set the brightness to X % for the primary monitor
sbc.set_brightness(100, display=0)
sbc.set_brightness(100, display=1)
BRIGHTNESS_DIM = 0
BREAK_INTERVAL = 1 * 60  # 20 minutes in seconds


# Define the path to the background music file
music_file_path = r"C:\Users\svafa\Downloads\Marconi Union - Weightless (Official Video).mp3"

# show brightness for each detected monitor
monitors = sbc.list_monitors()
print("monitors", monitors)

# Function to lock the keys
def lock_keys():
    keyboard.block_all()

def unlock_keys():
    keyboard.block_all()

# Function to play background music
def play_music():
    playsound(music_file_path)

# Function to dim the screen brightness
def dim_screen():
    sbc.fade_brightness(0, display=0)
    sbc.fade_brightness(0, display=1)

def get_current_brightness():
    x = sbc.get_brightness(display=0)
    y = sbc.get_brightness(display=1)

    return x, y

dim_screen()
print(get_current_brightness())
# # Main loop
# while True:
#     # Dim the screen brightness
#     dim_screen()
#
#     # Lock the keys
#     lock_keys()
#
#     # Play background music
#     play_music()
#
#     # Wait for the break interval
#     time.sleep(BREAK_INTERVAL)
#
#     # Restore the screen brightness
#     SetMonitorBrightness(hPhysicalMonitor, 100)
#
#     # Unblock the keys
#     unlock_keys()
#
#     # Stop the background music
#     os.system("taskkill /im wmplayer.exe /f")  # Terminate Windows Media Player process
#
#     # Wait for a few seconds before starting the next break interval
#     time.sleep(5)
