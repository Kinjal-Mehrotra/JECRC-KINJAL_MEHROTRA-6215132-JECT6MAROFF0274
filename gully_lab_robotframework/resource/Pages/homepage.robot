*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/homepage_locators.robot

*** Keywords ***
Clicking on Accounts
    [Documentation]  this opens the accounts
    Click Element    ${accounts}

Clicking on Search
    [Documentation]  this searches a product
    Click Element    ${search}

Navigate to homepage
    [Documentation]  this will take you to home page
    Click Element    ${gullylabs_logo}