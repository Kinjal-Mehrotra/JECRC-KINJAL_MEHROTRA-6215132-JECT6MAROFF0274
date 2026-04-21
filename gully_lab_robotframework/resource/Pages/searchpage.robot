*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/homepage_locators.robot
Resource  ../../locators/cartpage_locators.robot
*** Keywords ***
Search a product
    [Documentation]  this searches a product in gullylabs
    [Arguments]  ${product_to_search}
    Click Element    ${search}
    Sleep    2s
    Input Text    ${search_field}    ${product_to_search}
    Press Keys    ${search_field}    ENTER
#    Click Element    ${product_to_add}
