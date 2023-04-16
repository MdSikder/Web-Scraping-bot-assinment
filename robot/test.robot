*** Settings ***
Documentation   Validate Sort functionality for products displayed.
Library         SeleniumLibrary
#Library    WebDriverManagerLibrary
*** Variables ***
${BROWSER}      chrome
${URL}          https://www.flipkart.com/
${SEARCH_TERM}  shoes
${SORT_OPTION}  Price - Low to High
${PAGE_LIMIT}   2

${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver


*** Test Cases ***
Validate Sort Functionality for Products Displayed
    Open Browser to Flipkart
    Search for Shoes
    Sort Products by Price Low to High
    Validate Prices are in Ascending Order on Page 1
    Validate Prices are in Ascending Order on Page 2

*** Keywords ***
Open Browser to Flipkart


#    Call Method    ${options}    add_argument    --headless
#    Create Webdriver    Chrome    options=${options}
##    Go To    https://www.google.com
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    sleep    5
    Wait Until Page Contains Element    name=q

Search for Shoes
    [Arguments]    ${search_term}=${SEARCH_TERM}
    Input Text    name=q    ${search_term}
    Click Button    xpath://button[@type='submit']
    sleep    4

Sort Products by Price Low to High
#    [Arguments]    ${sort_option}=${SORT_OPTION}
#    Click Link    xpath://div[@class='_1xHtJz']/select/option[text()='${sort_option}']
    click element    //div[normalize-space()='Price -- Low to High']
    sleep    4

Validate Prices are in Ascending Order on Page 1
    [Arguments]    ${page_limit}=${PAGE_LIMIT}
    ${prices} =    Get Prices on Page    1
    Log    Prices on Page 1: ${prices}
#    ${sorted_prices} =    Sort List    ${prices}
    ${sorted_prices} =    sort products by price low to high     ${prices}
    Log    Sorted Prices on Page 1: ${sorted_prices}

    list selection should be     ${prices}    ${sorted_prices}    msg=Prices on Page 1 are not in ascending order.
#    List Should Be Equal    ${prices}    ${sorted_prices}    msg=Prices on Page 1 are not in ascending order.
    Run Keyword If    ${page_limit} > 1    Validate Prices are in Ascending Order on Page 2

Validate Prices are in Ascending Order on Page 2
    [Arguments]    ${page_limit}=${PAGE_LIMIT}
    ${prices} =    Get Prices on Page    2
    Log    Prices on Page 2: ${prices}

     ${sorted_prices} =    sort products by price low to high    ${prices}
#    ${sorted_prices} =    Sort List    ${prices}
    Log    Sorted Prices on Page 2: ${sorted_prices}
    list selection should be    ${prices}    ${sorted_prices}    msg=Prices on Page 2 are not in ascending order.
#    List Should Be Equal    ${prices}    ${sorted_prices}    msg=Prices on Page 2 are not in ascending order.

Get Prices on Page
    [Arguments]    ${page_number}
    ${prices} =    get text       xpath://div[@class='_30jeq3 _1_WHN1'][position() <= ${page_number}0]
    ${prices} =    Convert Prices to Numbers    ${prices}
    [Return]    ${prices}

Convert Prices to Numbers
    [Arguments]    ${prices}
    ${converted_prices} =    Evaluate    [float(price.replace(',', '')) for price in '${prices}']
    [Return]    ${converted_prices}
