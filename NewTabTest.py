# opening  new windoiw tab 
#driver.switch_to.new_window("tab")

from selenium import webdriver
import time 

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

parent = driver.current_window_handle

driver.switch_to.new_window("tab")

driver.get("https://www.google.com")

print("current url : ", driver.current_url)

print("total windowa /tabs : ", len(driver.window_handles))

driver.quit()
