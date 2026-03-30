#Navigate to website
#scroll to popup windw
#click on it
#switch to the window and return title
#switch back to parent window and assert heading of the page

*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${check_path}  C:\\Users\\hp\\Downloads\\sample.txt

*** Test Cases ***
File upload
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//a[@href="/upload"]
    Sleep    2s

    ${path}  Normalize Path    ${CURDIR}/sample.txt
    Choose File    id=file-upload    ${path}
    Sleep    2s

    Click Element    id=file-submit
    Close Browser

File Download
    Open Browser  ${url}  chrome
    Click Element    xpath=//a[@href="/download"]
    Sleep    1s

    Click Element    //a[text()="sample.txt"]

    Wait Until Created    ${check_path}  timeout=10s

    File Should Exist    ${check_path}

    Close Browser
