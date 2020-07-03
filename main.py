import pyautogui
import keyboard

while True:
     print(pyautogui.position())

     if keyboard.is_pressed('ENTER'):
          break