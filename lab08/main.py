from selenium import webdriver
from selenium.webdriver.common.by import By
import time
PATH = "C:\Moje pierdoły\Materiały_PJWSTK_semestr_6\Tau\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")

driver.find_element(By.XPATH, "").get_attribute("src")
menuGov = driver.find_element_by_class_name("govpl__menu-opener")
menuGov.click()
time.sleep(2)
coronaNews = driver.find_element_by_id("govpl-i-covid19")
coronaNews.click()
driver.maximize_window()
learnMore = driver.find_element_by_id('unit-submenu-0')
learnMore.click()
time.sleep(2)
driver.quit()