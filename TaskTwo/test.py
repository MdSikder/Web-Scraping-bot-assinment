from selenium import webdriver
from selenium.common import NoSuchElementException
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
product1 = driver.find_element(By.XPATH, "(//a[contains(@href,'/p/')])[2]")
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

# try:
#     cross = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, "//a[normalize-space()='10']"))
#     cross.click()
#     WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, "//a[normalize-space()='10']"))
#     # size.click()
#     time.sleep(2)
# except NoSuchElementException:
#     print("An exception occurred")


add_to_cart1.click()
time.sleep(4)


driver.switch_to.window(parent)
time.sleep(5)
product2 = driver.find_element(By.XPATH, "(//a[contains(@href,'/p/')])[3]")
product2.click()
add_to_cart2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='ADD TO CART']"))
)
add_to_cart2.click()
# driver.back()

# # Go to cart and validate products and prices
# cart = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[@class='_3ko_Ud']"))
# )
# cart.click()
#
# # Get all the product names and prices
# product_names = driver.find_elements(By.XPATH, "//a[@class='_2Kn22P']")
# product_prices = driver.find_elements(By.XPATH, "//div[@class='_30jeq3 _1_WHN1']")
#
# # Validate the correct products and prices are added to the cart
# assert product_names[0].text == "Product 2 name"
# assert product_prices[0].text == "Product 2 price"
# assert product_names[1].text == "Product 3 name"
# assert product_prices[1].text == "Product 3 price"
#
# # Get the total sum and validate
# total_sum = driver.find_element(By.XPATH, "//div[@class='_3xFhiH']")
# assert total_sum.text == "Total sum"
