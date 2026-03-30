*** Settings ***
Library  SeleniumLibrary
Documentation  Handle dropdowns

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
handle dropdown
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    
    Click Element    xpath=//a[text()="Dropdown"]

    Page Should Contain List   id=dropdown
    #assert to check if page contains the dropdown or not
    
    ${options}  Get List Items    id=dropdown
    Log To Console    ${options}
    
    Select From List By Value    id=dropdown  2

    ${select_option}=  Get Selected List Label    id=dropdown
    Log To Console    ${select_option}

    List Selection Should Be    id=dropdown  2
    Sleep  3s

    Close Browser



*** Keywords ***

