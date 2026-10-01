from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.CSS_SELECTOR, "#user-name")

username.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, "#password")

password.send_keys("secret_sauce")

login = driver.find_element(By.CSS_SELECTOR, "#login-button")

login.click()
time.sleep(2)

driver.quit()