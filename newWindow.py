#driver.switch_to.new_window 

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

parent = driver.current_window_handle

driver.switch_to.new_window ("window")
driver.get("https://www.google.com")

print("current url : ", driver.current_url)

driver.quit()