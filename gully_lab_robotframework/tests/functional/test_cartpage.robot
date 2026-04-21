*** Settings ***
Resource  ../../resource/Pages/loginpage.robot
Resource  ../../resource/common_resources.robot
Resource  ../../resource/Pages/homepage.robot
Resource    ../../resource/Pages/searchpage.robot
Resource    ../../resource/Pages/cartpage.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC004 Add a product to cart
    [Documentation]  Test Case 4 adding a product to cart
    [Tags]  functional
    Sleep    5s
    Clicking on Accounts
    Sleep    5s
    Log in to Gully Labs    ${USER_EMAIL}    ${USER_PWD}
    Sleep    5s
    Search a product
    Sleep    5s
    Add to Cart



