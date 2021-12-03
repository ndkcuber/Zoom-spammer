#ndkcuber is the bezt :)))

import pyautogui
import random
import subprocess
import datetime
import time

#not done yet lmao
def join_room(m_id,m_pass):
	subprocess.call("C:\\Users\\ndkcu\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
	while True:
		join_btn = pyautogui.locateOnScreen('join_button.png')
		if join_btn != None:
			pyautogui.click(join_btn)
			break
		else:
			print("Could not find join button")
			time.sleep(1)
	while True:
		fm_id =	pyautogui.locateOnScreen('fm_id.png')
		if fm_id != None:
			pyautogui.click(fm_id)
			pyautogui.typewrite(m_id)
			pyautogui.click(pyautogui.locateOnScreen('join_button2.png'))
			break
		else:
			print("Could not find id feild")
			time.sleep(2)
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