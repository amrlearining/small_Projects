import time
import pyautogui

pyautogui.hotkey('win', 's')
pyautogui.typewrite("xamp")
pyautogui.press('enter')
time.sleep(6)
pyautogui.click(346, 109)
pyautogui.click(343, 139)
pyautogui.click(651, 10)

time.sleep(1.5)
pyautogui.hotkey('win', 's')
pyautogui.typewrite("visual")
pyautogui.press('enter')
time.sleep(1)

pyautogui.hotkey('winleft', '1')
time.sleep(1)
pyautogui.hotkey('ctrl', 'n')
time.sleep(1)
pyautogui.hotkey('ctrl', 'e')
pyautogui.typewrite(["backspace"])
time.sleep(1)
pyautogui.typewrite("localhost/eCommerce/") 
pyautogui.press("enter")

time.sleep(1)

pyautogui.hotkey('ctrl', 't')
time.sleep(0.5)
pyautogui.typewrite("localhost/phpmyadmin/") 
pyautogui.press("enter")

#C:\Users\abu-almonther\AppData\Local\Programs\Python\Python311\Scripts

