import pydirectinput
import pyautogui
from time import sleep as wait

print('''
██▄   ▄█    ▄▄▄▄▄   ▄█▄    ████▄ █▄▄▄▄ ██▄          ▄▄▄▄▄   █ ▄▄  ██   █▀▄▀█     ▄█▄    ██   █    █     ▄███▄   █▄▄▄▄ 
█  █  ██   █     ▀▄ █▀ ▀▄  █   █ █  ▄▀ █  █        █     ▀▄ █   █ █ █  █ █ █     █▀ ▀▄  █ █  █    █     █▀   ▀  █  ▄▀ 
█   █ ██ ▄  ▀▀▀▀▄   █   ▀  █   █ █▀▀▌  █   █     ▄  ▀▀▀▀▄   █▀▀▀  █▄▄█ █ ▄ █     █   ▀  █▄▄█ █    █     ██▄▄    █▀▀▌  
█  █  ▐█  ▀▄▄▄▄▀    █▄  ▄▀ ▀████ █  █  █  █       ▀▄▄▄▄▀    █     █  █ █   █     █▄  ▄▀ █  █ ███▄ ███▄  █▄   ▄▀ █  █  
███▀   ▐            ▀███▀          █   ███▀                  █       █    █      ▀███▀     █     ▀    ▀ ▀███▀     █   
                                  ▀                           ▀     █    ▀                █                      ▀    
By arc for Windows.
You must be using the Discord APP (NOT on a browser), be in fullscreen, and go to DM's with the target.
''')

wait(0.25)

print("Warning, you cannot stop the program until all the calls have been completed.")
missedcalls = int(input("\nHow many calls would you like to spam? -> "))

for _ in range(missedcalls):
    pyautogui.moveTo(1528, 41)
    pydirectinput.doubleClick()
    pyautogui.moveTo(1223, 212)
    pyautogui.doubleClick()
    pyautogui.moveTo(1571, 38)
    pyautogui.doubleClick()
