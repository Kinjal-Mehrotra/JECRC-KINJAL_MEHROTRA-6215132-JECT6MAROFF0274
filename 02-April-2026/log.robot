*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://www.cricbuzz.com/

*** Test Cases ***
Handling log levels
    Open Browser  ${url}  headlesschrome

    Log  Navigated to cricbuzz  INFO
    Log  Navigated to cricbuzz  DEBUG
    Log  Navigated to cricbuzz  WARN
    Log  Navigated to cricbuzz  ERROR

# robot -d reports --timestamp log.robot
#robot -d "reports/$(Get-Date -Format 'yyyy-MM-dd_HH-mm-ss')" log.robot