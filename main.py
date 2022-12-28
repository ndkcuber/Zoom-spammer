#ndkcuber is the bezt :)))

import pyautogui
import random
import subprocess
import datetime
import time

def spammer():
	while True:
		activate_chat = pyautogui.locateOnScreen('type_message_here.png')
		if activate_chat != None:
			pyautogui.click(activate_chat)
			text_file = open('text.txt','r')
			lines = text_file.readlines()
			for line in lines:
				pyautogui.typewrite(line)
				pyautogui.press('enter')
			break
		else:
			print('cannot find message field')


spammer()
#main client
#type command here to run the client
