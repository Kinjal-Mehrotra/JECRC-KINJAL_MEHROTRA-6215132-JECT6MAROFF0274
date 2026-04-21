*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/logoutpage_locators.robot
#Resource  ../../locators/loginpage_locators.robot

*** Keywords ***
Log out from Gully Labs
    [Documentation]  this logs out user from the application

    Log  Clicking on accounts button
    Sleep    5s
#    Click Element    ${account_button}
    Log    Clicking on Logout
    Click Element    ${log_out_link}
    Sleep    5s


