from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

parent = driver.current_window_handle

driver.switch_to.new_window("tab")
driver.get("https://www.example.com")

print("child opened")

driver.close()

print("back to parent")

print("url : ", driver.current_url)

driver.quit()