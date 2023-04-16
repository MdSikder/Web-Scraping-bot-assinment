*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
Example Test Case
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --headless
    Create Webdriver    Chrome    options=${options}
    Go To    https://www.google.com
