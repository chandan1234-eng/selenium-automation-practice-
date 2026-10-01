from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Browser setup
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

print("Title:", driver.title)
print("URL:", driver.current_url)


# Login using different locators
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.CLASS_NAME, "submit-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

login_button.click()
time.sleep(2)


# Verify login
print("\nLogin URL:", driver.current_url)

if "inventory.html" in driver.current_url:
    print("Login: PASSED")
else:
    print("Login: FAILED")


# Locate page heading using XPath
products_heading = driver.find_element(
    By.XPATH,
    "//span[normalize-space(text())='Products']"
)

print("Page:", products_heading.text)


# CSS Selector
products = driver.find_elements(
    By.CSS_SELECTOR,
    ".inventory_item"
)

print("Total products:", len(products))

for product in products:
    name = product.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    )
    price = product.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    )

    print(name.text, "-", price.text)


# XPath functions
first_product = driver.find_element(
    By.XPATH,
    "(//div[contains(@class, 'inventory_item')])[1]"
)

product_name = first_product.find_element(
    By.XPATH,
    ".//div[starts-with(@class, 'inventory_item_name')]"
)

print("First product:", product_name.text)


# Parent and child relationship
product_container = driver.find_element(
    By.XPATH,
    "(//div[@class='inventory_item'])[1]"
)

add_to_cart = product_container.find_element(
    By.TAG_NAME,
    "button"
)

add_to_cart.click()
time.sleep(1)


# Cart
cart = driver.find_element(
    By.CLASS_NAME,
    "shopping_cart_link"
)

cart.click()
time.sleep(1)

cart_items = driver.find_elements(
    By.CLASS_NAME,
    "cart_item"
)

print("\nCart items:", len(cart_items))

if len(cart_items) == 1:
    print("Cart: PASSED")
else:
    print("Cart: FAILED")


# Checkout
checkout = driver.find_element(
    By.ID,
    "checkout"
)

checkout.click()

first_name = driver.find_element(By.ID, "first-name")
last_name = driver.find_element(By.ID, "last-name")
postal_code = driver.find_element(By.ID, "postal-code")

first_name.send_keys("Chandan")
last_name.send_keys("Sah")
postal_code.send_keys("44600")

driver.find_element(
    By.ID,
    "continue"
).click()

time.sleep(1)


# Checkout overview
overview = driver.find_element(
    By.XPATH,
    "//span[normalize-space(text())='Checkout: Overview']"
)

print("Checkout:", overview.text)


# Complete order
driver.find_element(By.ID, "finish").click()
time.sleep(1)


# Verify order completion
success_message = driver.find_element(
    By.XPATH,
    "//h2[contains(text(), 'Thank you')]"
)

print("Order:", success_message.text)

if "Thank you" in success_message.text:
    print("Checkout: PASSED")
else:
    print("Checkout: FAILED")


# Browser navigation practice
driver.refresh()
driver.back()
driver.forward()


# Close browser
driver.quit()

print("\nDay 33 Selenium practice completed.")