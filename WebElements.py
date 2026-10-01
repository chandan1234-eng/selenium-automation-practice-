#comon web element method  
#username.send_keys("standard_user")
#login-button.click()
# text  = element.text
#element.clear()
#element.is_displayed()
#element.is_enabled()
#element.is_selected()


#Web element Testing example 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")

print("displayed: ", username.is_displayed())
print("Enabled" ,username.is_enabled() )
time.sleep(2)
username.clear()
time.sleep(2)

username.send_keys("standard_user")
time.sleep(2)



# find elements
# input = driver.find(By.TAG_NAME, "Input")


# Testing all buttons 
buttons = driver.find_elements(By.TAG_NAME, "input")
print("toal elements: ", len(buttons))
time.sleep(2)


for element in buttons:
    print("element type : ", element.get_attribute("type"))


time.sleep(2)

driver.quit()
