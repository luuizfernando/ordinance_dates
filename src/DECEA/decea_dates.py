import pyautogui
import pyperclip
import time

from selenium.common.exceptions import NoSuchElementException

time.sleep(1)
CIADS = 0

pyautogui.click(x=1270, y=1059)
while CIADS < 3468:
    pyautogui.click(x=149, y=269)
    time.sleep(.5)
    pyautogui.click(x=252, y=198)
    time.sleep(.5)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(.5)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(.5)
    pyautogui.click(x=1011, y=1055)
    time.sleep(.5)
    pyautogui.click(x=960, y=540)
    time.sleep(.5)
    pyautogui.scroll(-600)
    time.sleep(.5)
    pyautogui.click(x=874, y=483)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("backspace")
    time.sleep(.5)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(.5)
    pyautogui.click(x=1445, y=493)
    time.sleep(.5)
    pyautogui.moveTo(x=779, y=631)
    pyautogui.dragTo(900, 631, 1, button='left')
    pyautogui.hotkey("ctrl", "c")
    pyautogui.click(x=1270, y=1059)
    pyautogui.click(x=878, y=269)
    pyautogui.click(x=252, y=198)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.click(x=1909, y=972)
    CIADS += 1