import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
import time

from selenium.common.exceptions import NoSuchElementException, WebDriverException

i = 0
while i < 3468:
    try:
        # copy data in excel sheet
        pyautogui.click(x=1205, y=1059)
        pyautogui.click(x=149, y=269)
        pyautogui.click(x=252, y=198)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(1)
        CIAD = pyperclip.paste()

        BROWSER = webdriver.Chrome()
        BROWSER.get("https://pergamum.anac.gov.br/")
        BROWSER.maximize_window()
        time.sleep(5)
        BROWSER.find_element(By.NAME, 'q').send_keys(CIAD)
        pyautogui.hotkey("enter")
        time.sleep(5)
        try:
            element = BROWSER.find_element(By.CLASS_NAME, 's16.negrito.preto80.hover1.link')
            date = element.text
            pyperclip.copy(date)
        except NoSuchElementException:
            raise NoSuchElementException("Tthere are no ordinances for the specified CIAD")
        
        pyautogui.click(x=1205, y=1059)
        pyautogui.click(x=1483, y=269)
        pyautogui.click(x=252, y=198)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.click(x=1911, y=970)

    except NoSuchElementException as e:
        print(f"Selenium error: {e}")
    
    i += 1