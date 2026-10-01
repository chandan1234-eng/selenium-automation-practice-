from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome() 

driver.get("https://www.saucedemo.com/")

#find username 
username = driver.find_element(By.ID, "user-name")

#find password 
password = driver.find_element(By.ID, "password")

#find login buttton
login_button = driver.find_element(By.ID, "login-button")

#enter credentials 
username.send_keys("standard_user")
password.send_keys("secret_sauce")

#click login

login_button.click()

time.sleep(3)

driver.quit()