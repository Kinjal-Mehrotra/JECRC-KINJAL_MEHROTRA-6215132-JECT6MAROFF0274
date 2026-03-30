*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
Implicit waits in robot framework
    Open Browser  ${url}  chrome
    ${before}  Get Selenium Implicit Wait
    Log To Console    ${before}

    Set Selenium Implicit Wait    5s

    ${after}  Get Selenium Implicit Wait
    Log To Console    ${after}

    ${later}  Get Selenium Implicit Wait
    Log To Console    ${later}

    Close Browser
    
Implicit wait 2
    Open Browser  ${url}  chrome
    ${implicit_wait_2}  Get Selenium Implicit Wait
    Log To Console    ${implicit_wait_2}

