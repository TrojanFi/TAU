from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Moje pierdoły\Materiały_PJWSTK_semestr_6\Tau\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")


ruleAgreement = driver.find_element_by_xpath('//*[@id="L2AGLb"]/div')
ruleAgreement.click()
searchGoogle = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
searchGoogle.send_keys("gdzie mieszkają smerfy")
time.sleep(2)
searchGoogleClick = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
searchGoogle.click()
searchGoogle.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)
linkClick = driver.find_element_by_xpath('//*[@id="rso"]/div[2]/div/div/div[1]/a/h3')
linkClick.click()
driver.maximize_window()
ruleAgreementTwo = driver.find_element_by_xpath('/html/body/div[14]/div[1]/div[2]/div/div[4]/button[2]')
ruleAgreementTwo.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 820)")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0)")
time.sleep(4)
# advertise = driver.find_element_by_xpath('//*[@id="gtm_ryz_popup--similar-box"]/div[2]/span')
# advertise.click()
searchQuestion = driver.find_element_by_xpath('//*[@id="headerQuestionForm"]/input')
searchQuestion.send_keys('Ile lat ma papa smerf ?')
searchQuestionClick = driver.find_element_by_xpath('//*[@id="headerQuestionForm"]/a[1]/h3')
searchQuestionClick.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 220)")
email = driver.find_element_by_xpath('//*[@id="main-content"]/section/form/div[1]/div/input')
email.send_keys("MojaPoczta@Gamil.com")
password = driver.find_element_by_xpath('//*[@id="main-content"]/section/form/div[2]/div/input')
password.send_keys("mojeshasłojestsuper")
rememberMe = driver.find_element_by_xpath('//*[@id="remeber-me"]')
rememberMe.click()
time.sleep(3)
login = driver.find_element_by_xpath('//*[@id="main-content"]/section/form/div[4]/input[5]')
login.click()
time.sleep(2)
driver.minimize_window()
driver.quit()