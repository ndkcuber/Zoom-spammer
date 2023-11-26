#dongkha is the bezt :)))

import pyautogui
import random
import subprocess
import datetime
import time
import pyperclip

def spammer():
    while True:
        activate_chat = pyautogui.locateOnScreen('type_message_here.png')
        if activate_chat is not None:
            pyautogui.click(activate_chat)
            with open('text.txt', 'r', encoding='utf-8') as text_file:
                lines = text_file.readlines()
                for line in lines:
                    pyperclip.copy(line.strip())  # strip to remove newline characters
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('v')
                    pyautogui.keyUp('ctrl')
                    pyautogui.press('enter')
            break
        else:
            print('cannot find message field!')

spammer()

#main client
#type command here to run the client
