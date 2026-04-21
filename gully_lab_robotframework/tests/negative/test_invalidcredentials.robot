*** Settings ***
Resource  ../../resource/Pages/loginpage.robot
Resource  ../../resource/common_resources.robot

Resource  ../../resource/Pages/homepage.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***

TC001 Login into the Applications
    [Documentation]  Test case 1 logging in the application
    [Tags]  negative

    Clicking on Accounts
#    Log in to Gully Labs    heyimac477@agoalz.com    heyimac
    Log in to Gully Labs    abc123@gmail.com    123
    Page Should Contain    Incorrect email or password.