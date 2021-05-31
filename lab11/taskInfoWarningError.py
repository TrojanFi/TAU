from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import logging
logging.basicConfig(filename='InfoWaringErrorTest.log',level=logging.INFO,format='%(levelname)s:%(message)s')
PATH = "C:\Moje pierdoły\Materiały_PJWSTK_semestr_6\Tau\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://gov.pl")

menuGov = driver.find_element_by_class_name("govpl__menu-opener")
menuGov.click()
time.sleep(2)
coronaNews = driver.find_element_by_id("govpl-i-covid19")
coronaNews.click()
driver.maximize_window()
logging.info("Maximum Widow size open properly")
learnMore = driver.find_element_by_id('unit-submenu-0')
learnMore.click()
logging.warning("ooh! watch out! there is not a lot of space on your computer")
time.sleep(2)
logging.error("Page was closed due to the unknown problem :(")
driver.quit()


