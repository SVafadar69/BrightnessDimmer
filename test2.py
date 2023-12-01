# possible: code to turn off monitor

import time
import subprocess
import keyboard
import pyttsx3
import win32con
import ctypes
import win32api
import win32gui
from pydub import AudioSegment
from pydub.playback import play
import pygame

music = r"C:\Users\svafadar\Downloads\Marconi Union - Weightless (Official Video)_UfcAVejslrU.mp3"
def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def music_function():
    play_music(music)
    stop_music()


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

def countdown():
    speak("Computer is entering screensaver mode in..")
    for i in range(5, 0, -1):
        speak(f"{str(i)} ...")


def main():
    countdown()
    #speak("Turning off in 5... 4... 3... 2... 1...")


# # Turn off the display using PowerShell
# subprocess.run([
#     'powershell.exe',
#     '-Command',
#     'Add-Type -TypeDefinition \'using System;using System.Runtime.InteropServices;public class DisplayHelper {[DllImport("user32.dll")]public static extern int SendMessage(int hWnd, int hMsg, int wParam, int lParam);}public static class Program {public static void Main() {DisplayHelper.SendMessage(-1, 0x0112, 0xF170, 2);}}\'; [Program]::Main()'
# ])


# Define the Windows API constants and functions
HWND_BROADCAST = 0xFFFF
WM_SYSCOMMAND = 0x0112
SC_MONITORPOWER = 0xF170
MONITOR_OFF = 2
MONITOR_ON = -1
def x():
    win32gui.SendMessage(win32con.HWND_BROADCAST,
                         win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)
    time.sleep(3)
def y():
        #turn on use :-
    win32gui.SendMessage(win32con.HWND_BROADCAST,
                         win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1)


# def countdown():
#     print("Computer is entering screensaver mode in...")
#     for i in range(5, 0, -1):
#         print(f"{i}...")
#         time.sleep(1)
#
# def turn_off_display():
#     # Turn off the display
#     SendMessage = ctypes.windll.user32.SendMessageW
#     SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_OFF)
#
# def turn_on_display():
#     # Turn on the display
#     SendMessage = ctypes.windll.user32.SendMessageW
#     SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_ON)

def move_cursor():
    # Move the mouse cursor by 1 pixel to trigger display turn-on
    x, y = win32api.GetCursorPos()
    win32api.SetCursorPos((x + 1, y))

def main():
    #countdown()
    play_music(music)
    time.sleep(5)
    x()
    y()
    stop_music()
    # turn_off_display()
    # time.sleep(5)  # Wait for 5 seconds (you can adjust the duration as needed)
    # turn_on_display()
    move_cursor()
    print("end")
if __name__ == "__main__":
    main()