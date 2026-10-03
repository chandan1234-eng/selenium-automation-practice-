from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

parent = driver.current_window_handle

driver.execute_script("window.open('https://www.wikipedia.org');")

handles  = driver.window_handles

print("numbewr of tabs : ", len(handles))

driver.switch_to.window(handles[1])

print("child url :", driver.current_url)

driver.quit()

