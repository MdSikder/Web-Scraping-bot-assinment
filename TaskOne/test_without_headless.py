import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestSortFunctionality(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 10)

    def test_sort_products_by_price(self):
        # retrieve test data
        search_term = "shoes"
        sort_parameter = "Price – Low to High"
        page_limit = 2

        # navigate to flipkart.com
        self.driver.get("https://www.flipkart.com/")
        time.sleep(5)

        cross = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/button')
        cross.click()
        time.sleep(2)

        # find search textbox and search button
        search_box = self.driver.find_element(By.NAME, "q")
        time.sleep(1)
        search_button = self.driver.find_element(By.CLASS_NAME, "L0Z3Pu")
        time.sleep(1)

        # enter search term and click search button
        search_box.send_keys(search_term)
        search_button.click()
        time.sleep(4)

        # wait for search results to load
        search_results_xpath = "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[2]"
        self.wait.until(EC.presence_of_element_located((By.XPATH, search_results_xpath)))
        time.sleep(2)

        sort = self.driver.find_element(By.XPATH, "//div[normalize-space()='Price -- Low to High']")
        sort.click()
        time.sleep(10)

        # validate prices for all products displayed till page limit are in ascending order
        prices = []
        for page in range(1, page_limit + 1):

            price_elements = self.driver.find_elements(By.XPATH,
                                                       "//div[@class='_30jeq3']")  # Replace with the appropriate xpath for the price elements
            prices = [float(price_element.text.replace('₹', '').replace(',', '')) for price_element in price_elements]
            print(page, "st page products prices", prices)
            # Check if prices are in ascending order
            is_ascending = prices == sorted(prices)
            if is_ascending:
                print("Page", page, "product prices are in ascending order.")
            else:
                print("Page", page, "product prices are not in ascending order.")

            # Check if prices are in descending order
            is_descending = prices == sorted(prices, reverse=True)
            if is_descending:
                print("Page", page, "product prices are in descending order.")
            else:
                print("Page", page, "product prices are not in descending order.")

            self.driver.execute_script("window.scrollBy(0,1000)", "")
            time.sleep(1)
            # navigate to next page
            if page < page_limit:
                next_button = self.driver.find_element(By.XPATH, "//span[normalize-space()='Next']")
                next_button.click()
                time.sleep(10)
                # self.wait.until(EC.staleness_of(self.driver.find_element(By.XPATH, "//div[@class='_30jeq3']")))
                print("----------------------------------------------------------------")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
