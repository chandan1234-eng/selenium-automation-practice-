from selenium import webdriver
import time

driver = webdriver.Chrome()


# open url 

driver.get("https://www.google.com/")
#small testing program 
time.sleep(1)

driver.quit()


#Testingg example 

driver =  webdriver.Edge()
driver.get("https://www.saucedemo.com/")

print(driver.title)

# get current url 
print(driver.current_url)


#testing example 

expected_url = "https://www.saucedemo.com/"
driver.get(expected_url)
actual_url = driver.current_url


#Get source page 
source = driver.page_source
print(source)



# validate 
assert actual_url == expected_url


#small testing 
if "Swag Labs" in source:
    print("text found")
else:
    print("text not found")

driver.close()

#close the webiste - 
driver.quit()
