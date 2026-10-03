from selenium import webdriver

driver = webdriver.Chrome()

#open parent 
driver.get("https://www.saucedemo.com/")
parent = driver.current_window_handle

#open new tab 
driver.switch_to.new_window('tab')

child = driver.current_window_handle

driver.get("https://www.google.com")

print("child title: ", driver.title)

#close child 
driver.close()

#return to parent 
driver.switch_to.new_window(parent)

print("parent url : ", driver.current_url)

driver.quit()