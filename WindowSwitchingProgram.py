#switching betweeen windows 
#syntax = driver.switch_to_window(handle)

from selenium import webdriver 

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

parent  = driver.current_window_handle


#open new window/tab using java script 
driver.execute_script("window.open('https://www.saucedemo.com/inventory.html');")

windows = driver.window_handles

for window in windows:
    if window != parent:
        driver.switch_to.window(window)
        break


print("current url: ", driver.current_url)
driver.quit()