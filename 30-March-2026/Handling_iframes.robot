#Navigate to website
#scroll to popup windw
#click on it
#switch to the window and return title
#switch back to parent window and assert heading of the page

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling iframes
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Select Frame    id=singleframe

    Input Text    xpath=//input[@type="text"]    KM
    Sleep  3s
    Unselect Frame

    Close Browser
