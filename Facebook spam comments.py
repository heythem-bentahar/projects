from selenium import webdriver
#from selenium.webdriver.chrome.remote_connection import ChromeRemoteConnection
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
PATH = r"C:\Users\admin\Desktop\Project\chromedriver.exe" #chromdriver path
options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(PATH, options=options)
driver.get("https://www.facebook.com")
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")

username.send_keys("your email")             # facebook email
password.send_keys("your pass", Keys.RETURN) # facebook password

driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])
driver.get("the target post") #target post link

time.sleep(8)

try:
    element = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[5]/div[2]/div/div/div/div/form/div/div/div[2]/div/div/div/div'))
    )
    spam = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[5]/div[2]/div/div/div/div/form/div/div/div[2]/div/div/div/div')

finally:
    time.sleep(1)
while True:

    spam.send_keys("comment you want to send") #spam comment 
