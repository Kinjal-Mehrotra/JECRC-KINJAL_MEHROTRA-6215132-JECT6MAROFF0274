*** Settings ***
Resource  ../../resource/Pages/logoutpage.robot
Resource  ../../resource/common_resources.robot
Resource  ../../resource/Pages/loginpage.robot
Resource  ../../resource/Pages/homepage.robot
Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC002 Logout Functionality
    [Documentation]  Test case 2 logging out of the application
    [Tags]  functional
    Clicking on Accounts
    Log in to Gully Labs    ${USER_EMAIL}    ${USER_PWD}
    Sleep    2s
    Log out from Gully Labs
