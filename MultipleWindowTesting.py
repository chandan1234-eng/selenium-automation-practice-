from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.switch_to.new_window("tab")
driver.get("https://www.google.com")

driver.switch_to.new_window("tab")
driver.get("https://www.wikipedia.org")

handles = driver.window_handles

print("total handles :" , len(handles))

for handle in handles:
    driver.switch_to.window(handle)
    print("=========")
    print("title: "  , driver.title)
    print("url: ", driver.current_url)