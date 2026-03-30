*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://inc.in/

*** Test Cases ***
handling js
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s

    Execute Javascript  window.scrollTo(0,document.body.scrollHeight)
    Sleep  2s

    Execute Javascript  window.scrollTo(0,0)
    Sleep  2s

    Execute Javascript  window.scrollBy(0,600)
    Sleep  2s

    Execute Javascript  window.scrollBy(0,-200)
    Sleep  2s

    Close Browser


*** Keywords ***