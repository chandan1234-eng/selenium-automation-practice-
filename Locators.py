from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")

print("Username field found")



# example 
#from selenium.webdriver.common.by import By
driver .find_element(By.ID, "user-name")
driver.find_element(By.ID,"password")
driver.find_element(By.ID, "login-button")

driver.quit()


