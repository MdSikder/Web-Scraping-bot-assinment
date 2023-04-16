from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import Keys
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Define the search parameter and sort parameter from a data source
search_query = "shoes"
sort_parameter = "Price - Low to High"

# Set up the Chrome driver

# Navigate to the flipkart website
# options = Options()
# options.headless = True
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# open the flipkart website
driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(1)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

cross = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/button')
cross.click()
time.sleep(2)
# locate the search box and search button, and enter "shoes"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("shoes")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Sort by price - low to high
sort_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='Price -- Low to High']"))
)
sort_dropdown.click()
time.sleep(3)

# Click on the second and third available products and add to cart
product1_name = driver.find_element(By.XPATH, "(//a[contains(@href,'/p/')])[5]").text
product1 = driver.find_element(By.XPATH, "(//a[contains(@href,'/p/')])[5]")
product1.click()
time.sleep(5)

p = driver.current_window_handle
parent = driver.window_handles[0]
chld = driver.window_handles[1]
driver.switch_to.window(chld)

# driver.refresh()
time.sleep(2)
add_to_cart1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add to cart']"))
)

try:
    size_loc = "//a[normalize-space()='10']"
    size = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, size_loc))
    )
    size.click()
    time.sleep(4)
except NoSuchElementException:
    print("An exception occurred")
    pass

except TimeoutException:
    print("TimeoutException exception occurred")
    pass
except StaleElementReferenceException:
    print("StaleElementReferenceException exception occurred")
    pass

add_to_cart1.click()
time.sleep(5)

driver.switch_to.window(parent)
time.sleep(5)
product2 = driver.find_element(By.XPATH, "(//a[contains(@href,'/p/')])[8]")
product2.click()

chld2 = driver.window_handles[2]
driver.switch_to.window(chld2)
driver.refresh()
time.sleep(3)

# add_to_cart2 = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//button[text()='ADD TO CART']"))
# )
time.sleep(3)

try:
    size_loc = "//a[normalize-space()='10']"
    size = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, size_loc))
    )
    size.click()
    time.sleep(8)
except NoSuchElementException:
    print("An exception occurred")

except TimeoutException:
    print("TimeoutException exception occurred")
except StaleElementReferenceException:
    print("StaleElementReferenceException exception occurred")

driver.refresh()
time.sleep(3)
add_to_cart2 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add to cart']"))
)
add_to_cart2.click()
time.sleep(5)
driver.switch_to.window(parent)
time.sleep(5)

# Go to cart and validate products and prices
cart = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Cart']"))
)
cart.click()
time.sleep(3)

product_1_name = driver.find_element(By.XPATH,
                                     "//*[@id='container']/div/div[2]/div/div/div[1]/div/div[3]/div/div[1]/div[1]/div[1]/a").text
print(product_1_name)

try:
    assert product_1_name == product1_name
    time.sleep(2)
except AssertionError:
    print("Product-1 name does not match")

product_1_price = driver.find_element(By.XPATH,
                                      "//*[@id='container']/div/div[2]/div/div/div[1]/div/div[3]/div/div[1]/div[1]/span[2]").text
print(product_1_name, 'price is', product_1_price)

product_2_name = driver.find_element(By.XPATH,
                                     "//*[@id='container']/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[1]/div[1]/a").text
print(product_2_name)

try:
    assert product_2_name == product_2_name
    time.sleep(2)
except AssertionError:
    print("Product-2 name does not match")

product_2_price = driver.find_element(By.XPATH,
                                      "//*[@id='container']/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[1]/span[2]").text
print(product_2_name, 'price is', product_2_price)

price1 = [float(product_1_price.replace('₹', '').replace(',', ''))]
price2 = [float(product_2_price.replace('₹', '').replace(',', ''))]

both_price_sum = price1 + price2
print("after sum prices are :", both_price_sum)

total_price = driver.find_element(By.XPATH,
                                  "//*[@id='container']/div/div[2]/div/div/div[2]/div[1]/div/div/div/div[4]/div/div[2]/span/div/div/div[2]/span").text
print(total_price)
total = [float(total_price.replace('₹', '').replace(',', ''))]
time.sleep(2)

try:
    assert total == both_price_sum
    time.sleep(2)
except AssertionError:
    print("AssertionError exception occurred")


# # Collect product names and prices
# product_names = []
# product_prices = []
#
# # Find the elements that contain product names and prices
# name_elements = driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]/div/div/div[1]/div/div[3]/div/div[1]/div[1]/div[1]/a")
# price_elements = driver.find_elements(By.XPATH, '//*[@id="container"]/div/div[2]/div/div[1]/div[1]/div/div[3]/div/div[1]/div[1]/span[2]')
# time.sleep(2)
# Extract text from name and price elements
# for name_element, price_element in zip(name_elements, price_elements):
#     product_names.append(name_element.text)
#     product_prices.append(price_element.text)
#
# # Print the collected product names and prices
# for name, price in zip(product_names, product_prices):
#     print('Product Name:', name)
#     print('Product Price:', price)
#     print('---')


# Extract text from name and price elements
# for name_element, price_element in zip(name_elements, price_elements):
#     product_names.append(name_element.text)
#     product_prices.append(price_element.text)
#
# # Print the collected product names and prices
# for name, price in zip(product_names, product_prices):
#     print('Product Name:', name)
#     print('Product Price:', price)
#     print('---')
#
# time.sleep(3)


# Get all the product names and prices
# product_names = driver.find_elements(By.XPATH, "//a[normalize-space()='density Running Shoes For Men']")
# print(product_names)
# # product_prices = driver.find_elements(By.XPATH, "//div[@class='_30jeq3 _1_WHN1']")
# time.sleep(3)

# Validate the correct products and prices are added to the cart
# try:
#     assert product_names[1].text == "Product 2 name"
#     # assert product_names[0].text == "Product 2 name"
# except AssertionError:
#     print("AssertionError exception occurred")
# assert product_prices[0].text == "Product 2 price"
# assert product_names[1].text == "Product 3 name"
# assert product_prices[1].text == "Product 3 price"
#
# # Get the total sum and validate
# total_sum = driver.find_element(By.XPATH, "//div[@class='_3xFhiH']")
# assert total_sum.text == "Total sum"
