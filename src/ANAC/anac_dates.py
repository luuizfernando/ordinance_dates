import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
import time

from selenium.common.exceptions import NoSuchElementException

BROWSER = webdriver.Chrome()
BROWSER.maximize_window()
CIADS = 0

pyautogui.click(x=1224, y=1058)
while CIADS < 3468:
    try:
        pyautogui.click(x=149, y=269)
        pyautogui.click(x=252, y=198)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(1)
        CIAD = pyperclip.paste()
        
        pyautogui.click(x=1273, y=1054)
        BROWSER.get("https://pergamum.anac.gov.br/")
        time.sleep(5)
        BROWSER.find_element(By.NAME, 'q').send_keys(CIAD)
        pyautogui.hotkey("enter")
        time.sleep(5)
        try:
            element = BROWSER.find_element(By.CLASS_NAME, 's16.negrito.preto80.hover1.link')
            date = element.text
            pyperclip.copy(date)
        except NoSuchElementException:
            error_message = "There are no ordinances for the specified CIAD"
            pyperclip.copy(error_message)
        
        pyautogui.click(x=1224, y=1058)
        time.sleep(1)
        pyautogui.click(x=1488, y=269)
        time.sleep(1)
        pyautogui.click(x=252, y=198)
        time.sleep(1)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.click(x=1910, y=972)

    except NoSuchElementException as e:
        print(f"Selenium error: {e}")
    
    CIADS += 1