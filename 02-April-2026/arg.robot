*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://sauce-demo.myshopify.com/account/login

*** Test Cases ***
Login Positional Arguments
    Open Browser  ${url}  chrome
    Sleep    2s
    Login Success    cheeseburger@gmail.com    12345

Login Default arguments
    Open Browser  ${url}  chrome
    Sleep    2s
    Login Success    cheeseburger@gmail.com


Login Keyword arguments
    Open Browser  ${url}  chrome
    Sleep    2s
    Login Success    email=cheeseburger@gmail.com  password=12345

*** Keywords ***
Login Success
    [Arguments]  ${email}  ${password}=12345
    Input Text    id=customer_email    ${email}
    Input Text    id=customer_password    ${password}