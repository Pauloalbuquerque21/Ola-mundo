import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(5)
pyautogui.write('https://outlook.live.com/mail/0/')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=1753,y=255)
time.sleep(5)
pyautogui.click(x=1823,y=256)

