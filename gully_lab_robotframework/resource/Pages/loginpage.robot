*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/loginpage_locators.robot

*** Keywords ***
Log in to Gully Labs
    [Documentation]  this logs in the user to the applications
    [Arguments]  ${email}  ${password}
    Log    Writing the email address
    Input Text    ${email_field}    ${email}
    Log    Writing the password
    Input Text    ${password_field}    ${password}
    Log    Now signing in
    Wait Until Element Is Enabled    ${login_button}
    Click Element    ${login_button}
    Sleep    5s

#    Page Should Contain    ACCOUNT
#    Page Should Contain Element    xpath=//a[text()='Log out']
