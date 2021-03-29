from selenium import webdriver
import time
PATH = "C:\Moje pierdoły\Materiały_PJWSTK_semestr_6\Tau\geckodriver.exe"

driver = webdriver.Firefox(PATH)

driver.get("https://gov.pl")

menuGov = driver.find_element_by_class_name("govpl__menu-opener")
menuGov.click()
time.sleep(2)
coronaNews = driver.find_element_by_id("govpl-i-covid19")
coronaNews.click()
driver.maximize_window()
time.sleep(2)
learnMore = driver.find_element_by_id('unit-submenu-0')
learnMore.click()
time.sleep(2)
driver.quit()