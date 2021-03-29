from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Moje pierdoły\Materiały_PJWSTK_semestr_6\Tau\msedgedriver.exe"

driver = webdriver.Edge(PATH)

driver.get("https://www.spotify.com/pl/")
driver.maximize_window()
elements = driver.find_elements_by_class_name("svelte-vf0pv9")
elements.__getitem__(8).click()
username = driver.find_element_by_id('login-username')
username.send_keys("bigMaluch56@gmail.com")
password = driver.find_element_by_id('login-password')
password.send_keys("fiatToJestNajlepszy21")
remember = driver.find_element_by_class_name('control-indicator')
remember.click()
time.sleep(3)
loginButton = driver.find_element_by_id('login-button')
loginButton.click()
time.sleep(2)
driver.quit()