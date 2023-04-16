*** Settings ***
Library       SeleniumLibrary

*** Variables ***
${BROWSER}    Chrome
${URL}        https://www.flipkart.com
${SEARCH_TEXT}    shoes
${SORT_OPTION}    Price - Low to High

*** Test Cases ***
Validate Add to Cart Functionality
    [Setup]    Open Browser    ${URL}    ${BROWSER}
    sleep    3

    click element    xpath=/html/body/div[2]/div/div/button
    sleep    2
    Input Text    css=input[name='q']    ${SEARCH_TEXT}
    Click Button    css=button[type='submit']
    Click Element    css=div[style*='display: block'] div:nth-child(2) a
    Click Element    css=div[style*='display: block'] div:nth-child(3) a
    Click Button    css=button._2AkmmA._2Npkh4._2MWPVK
    Click Element    css=div[style*='display: block'] div:nth-child(2) a
    Click Element    css=div[style*='display: block'] div:nth-child(3) a
    Click Button    css=button._2AkmmA._2Npkh4._2MWPVK
    Click Button    css=span.nav-cart-icon.nav-sprite
    Wait Until Element Is Visible    css=div[data-id^='CartItem']    timeout=10s
    ${product1_name}    Get Text    css=div[data-id^='CartItem']:nth-child(1) a
    ${product1_price}    Get Text    css=div[data-id^='CartItem']:nth-child(1) div._30jeq3._1_WHN1
    ${product2_name}    Get Text    css=div[data-id^='CartItem']:nth-child(2) a
    ${product2_price}    Get Text    css=div[data-id^='CartItem']:nth-child(2) div._30jeq3._1_WHN1
    Should Be Equal As Strings    ${product1_name}    Expected Product 1 Name
    Should Be Equal As Strings    ${product1_price}    Expected Product 1 Price
    Should Be Equal As Strings    ${product2_name}    Expected Product 2 Name
    Should Be Equal As Strings    ${product2_price}    Expected Product 2 Price
    ${total_sum}    Evaluate    int(${product1_price}.replace(',', '')) + int(${product2_price}.replace(',', ''))
    ${cart_total}    Get Text    css=span._2Ru97g
    Should Be Equal As Strings    ${cart_total}    Rs. ${total_sum}

*** Keywords ***
Expected Product 1 Name
    [Return]    Product 1 Name

Expected Product 1 Price
    [Return]    Product 1 Price

Expected Product 2 Name
    [Return]    Product 2 Name

Expected Product 2 Price
    [Return]    Product 2 Price
