*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/cartpage_locators.robot

*** Keywords ***
Close Cart Page
    [Documentation]  this will close cart page
    Wait Until Element Is Visible    ${close_cart_page_button}  timeout=20s
    Click Element    ${close_cart_page_button}
    Sleep    2s