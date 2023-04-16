from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# set up the Chrome driver
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

# wait for the page to load
time.sleep(3)

# locate and click the "Price -- Low to High" sorting option
# sort_button = driver.find_element(By.XPATH, "//div[@class='_1xHtJz']/select/option[text()='Price -- Low to High']")
# sort_button.click()
sort = driver.find_element(By.XPATH, "//div[normalize-space()='Price -- Low to High']")
sort.click()

# wait for the page to load
time.sleep(10)

# locate and click the second and third products' add to cart buttons
cart = driver.find_element(By.XPATH, "//button[normalize-space()='Add to cart']")
cart.click()

buynow = driver.find_element(By.XPATH, "//button[normalize-space()='Buy Now']")
buynow.click()

# add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[normalize-space()='Add to cart']")
# add_to_cart_buttons[1].click()
# add_to_cart_buttons[2].click()

# wait for the cart page to load
time.sleep(3)
# driver.get("https://www.flipkart.com/viewcart?otracker=Cart_Icon_Click")
#
# # validate that the correct products are added with correct prices
# products = driver.find_elements(By.XPATH, "//div[@class='_2kHMtA']")
# prices = driver.find_elements(By.XPATH, "//div[@class='_30jeq3 _1_WHN1']")
# total_price = 0
# for i in range(2):
#     assert products[i].text in ['Product 2', 'Product 3']  # replace with actual product names
#     assert int(prices[i].text[1:].replace(',', '')) in [500, 600]  # replace with actual product prices
#     total_price += int(prices[i].text[1:].replace(',', ''))

# # validate the total sum
# assert int(driver.find_element(By.XPATH, "//span[text()='Total Amount']/following-sibling::span").text[1:].replace(',', '')) == total_price
#
# # close the browser
# driver.quit()
