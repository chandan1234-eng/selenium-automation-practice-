#get window handle ()
#driver.current_window_handle


#example 
from selenium import webdriver

driver  = webdriver.Chrome()
driver.get("https://www.google.com")

parent_window = driver.current_window_handle
all_window = driver.window_handles

print("parnet window: " , parent_window)
print("all windows: " , all_window)

#switching betweeen windows 
#open new window/tab using java script 
driver.execute_script("window.open('https://www.example.com');")

windows = driver.window_handles

for window in windows:
    if window != parent_window:
        driver.switch_to.window(window)
        break

print("current url: " , driver.current_url)

driver.quit()
