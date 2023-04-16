// Here is a sample test class in Java using TestNG framework to validate the sort functionality for products displayed on flipkart.com:

java
Copy code
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.*;

import java.util.List;

public class FlipkartSortTest {

    private WebDriver driver;
    private WebDriverWait wait;
    private String baseUrl = "https://www.flipkart.com/";

    @BeforeClass
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver.exe");
        driver = new ChromeDriver();
        wait = new WebDriverWait(driver, 10);
    }

    @Test(dataProvider = "searchData")
    public void testSortFunctionality(String searchQuery, String sortOption, int pageLimit) {
        driver.get(baseUrl);
        WebElement searchBox = driver.findElement(By.xpath("//input[@title='Search for products, brands and more']"));
        searchBox.sendKeys(searchQuery);
        searchBox.submit();

        WebElement sortDropdown = driver.findElement(By.xpath("//div[@class='_2yC6Ul']/div/select"));
        sortDropdown.sendKeys(sortOption);

        wait.until(ExpectedConditions.textToBe(By.xpath("//div[@class='_2yC6Ul']/span"), "Price -- Low to High"));

        validateSortOrder(pageLimit);
    }

    private void validateSortOrder(int pageLimit) {
        boolean isSorted = true;
        int currentPage = 1;
        while (currentPage <= pageLimit) {
            List<WebElement> prices = driver.findElements(By.xpath("//div[@class='_30jeq3 _1_WHN1']"));
            for (int i = 1; i < prices.size(); i++) {
                int price1 = Integer.parseInt(prices.get(i - 1).getText().replace(",", ""));
                int price2 = Integer.parseInt(prices.get(i).getText().replace(",", ""));
                if (price1 > price2) {
                    isSorted = false;
                    break;
                }
            }
            if (!isSorted) {
                break;
            }
            if (currentPage < pageLimit) {
                WebElement nextPageButton = driver.findElement(By.xpath("//a[@class='_1LKTO3'][text()='Next']"));
                nextPageButton.click();
                currentPage++;
            }
        }
        Assert.assertTrue(isSorted, "Prices are not sorted in ascending order");
    }

    @DataProvider(name = "searchData")
    public Object[][] getSearchData() {
        return new Object[][]{
                {"shoes", "Price -- Low to High", 2},
                {"sneakers", "Price -- High to Low", 1},
                {"boots", "Newest First", 3}
        };
    }

    @AfterClass
    public void tearDown() {
        driver.quit();
    }
}