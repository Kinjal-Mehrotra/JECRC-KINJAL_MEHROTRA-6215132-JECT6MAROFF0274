*** Settings ***
Resource  ../../resource/Pages/loginpage.robot
Resource  ../../resource/common_resources.robot
Resource  ../../resource/Pages/homepage.robot
Resource    ../../resource/Pages/searchpage.robot
Resource    ../../resource/Pages/cartpage.robot
Resource  ../../locators/cartpage_locators.robot
Resource  ../../resource/Pages/closecartpage.robot
Resource  ../../resource/Pages/logoutpage.robot
Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC006 Complete user journey (Login to Logout)
    [Documentation]  performing end to end testing
    [Tags]  e2e
    Sleep    5s
    Clicking on Accounts
    Sleep    5s
    Log in to Gully Labs    ${USER_EMAIL}    ${USER_PWD}
    Sleep    5s
    Search a product
    Sleep    2s
    Add to Cart
    Sleep    2s
    Close Cart Page
    Sleep    2s
#    Navigate to homepage
#    Sleep    5s
    Clicking on Accounts
    Sleep    5s
    Log out from Gully Labs
    Sleep    2s


