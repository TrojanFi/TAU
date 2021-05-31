from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Moje pierdoły\Materiały_PJWSTK_semestr_6\Tau\msedgedriver.exe"

driver = webdriver.Edge(executable_path=PATH)

driver.get("https://www.spotify.com/pl/")
driver.maximize_window()
time.sleep(2)
help = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/header/div/nav/ul/li[2]/a')
help.click()
search = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[1]/div/input')
search.send_keys("Jakie macie zniżki")
time.sleep(2)
acceptCookie = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
acceptCookie.click()
time.sleep(2)
studentPremiumClick = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/ul/li[5]/a')
studentPremiumClick.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 320)")
time.sleep(5)
thanksForHelp = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[2]/div[2]/div[2]/button[1]/div[1]')
thanksForHelp.click()
time.sleep(3)
driver.minimize_window()
driver.quit()