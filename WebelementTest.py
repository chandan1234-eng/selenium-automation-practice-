from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

#verify username field dispalyed 
time.sleep(2)
assert username.is_displayed()
assert username.is_enabled()
time.sleep(2)
 
#verify login_button.is displayed()
assert login_button.is_displayed()
assert login_button.is_enabled()
time.sleep(2)

username.send_keys("standard_user")
password.send_keys("secret_sauce")
time.sleep(2)
 
#click login
login_button.click()

time.sleep(2)


title = driver.find_element(By.CLASS_NAME, "title")

assert title.text == "Products"

print("Login test passed")


driver.quit()