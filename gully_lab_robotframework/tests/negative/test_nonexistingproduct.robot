*** Settings ***
Resource  ../../resource/Pages/homepage.robot
Resource  ../../resource/common_resources.robot
Resource  ../../resource/Pages/searchpage.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC003 Search Product
    [Documentation]  Test case 3 to search a product
    [Tags]  negative
    Search a product    smartphone
    Page Should Contain    No results