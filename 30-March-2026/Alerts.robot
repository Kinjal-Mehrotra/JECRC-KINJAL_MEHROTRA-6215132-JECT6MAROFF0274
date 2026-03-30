#Navigate to website
#scroll to popup windw
#click on it
#switch to the window and return title
#switch back to parent window and assert heading of the page

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Simple alert
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//button[text()="Click for JS Alert"]
    Handle Alert
    #will by default it will wait for alert to pop up and accept it 
    
    Sleep    5s
    Close Browser

Confirmation alert
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//button[text()="Click for JS Confirm"]

    Sleep  2s

    #to dismiss
    Handle Alert  action=DISMISS
    Sleep    2s

    #to accept
    Click Element    xpath=//button[text()="Click for JS Confirm"]
    Handle Alert

    Sleep  2s

    Close Browser

Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//button[text()="Click for JS Prompt"]
    Sleep  2s

    #giving prompt and accepting
    Input Text Into Alert    Hello World
    Sleep  2s

    #dismissing
    Click Element    xpath=//button[text()="Click for JS Prompt"]
    Input Text Into Alert  Hello  action=DISMISS
    Sleep    2s

    Close Browser
