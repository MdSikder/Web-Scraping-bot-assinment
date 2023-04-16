import time

from selenium import webdriver

# Create a webdriver instance (you may need to specify the path to your webdriver)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the cart page on Flipkart
driver.get('https://www.flipkart.com/viewcart?exploreMode=true&preference=FLIPKART')
time.sleep(5)

# Collect product names and prices
product_names = []
product_prices = []

# Find the elements that contain product names and prices
name_elements = driver.find_elements(By.XPATH, '//div[@class="_2QcLo-"]/div[1]/a[1]')
price_elements = driver.find_elements(By.XPATH, '//div[@class="_2QcLo-"]/div[1]/a[2]/div[1]')

# Extract text from name and price elements
for name_element, price_element in zip(name_elements, price_elements):
    product_names.append(name_element.text)
    product_prices.append(price_element.text)

# Print the collected product names and prices
for name, price in zip(product_names, product_prices):
    print('Product Name:', name)
    print('Product Price:', price)
    print('---')

# Close the webdriver
driver.close()
