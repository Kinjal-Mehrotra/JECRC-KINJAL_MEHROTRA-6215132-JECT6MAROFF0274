*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/jaipur

*** Test Cases ***
Screenshots
    Set Screenshot Directory    ${CURDIR}/Screenshots

    #from subfolder , u go to the main folder
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Capture Page Screenshot  fullpage.png

#    Sleep  1s
    Scroll Element Into View    xpath=//img[@alt="Adventure of Iceberg 7D - Combo"]
    Capture Element Screenshot    xpath=//img[@alt="Adventure of Iceberg 7D - Combo"]  element1.png


*** Keywords ***