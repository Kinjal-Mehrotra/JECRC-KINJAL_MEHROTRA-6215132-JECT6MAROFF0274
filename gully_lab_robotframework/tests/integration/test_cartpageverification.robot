*** Settings ***
Resource  ../../resource/Pages/loginpage.robot
Resource  ../../resource/common_resources.robot
Resource  ../../resource/Pages/homepage.robot
Resource    ../../resource/Pages/searchpage.robot
Resource    ../../resource/Pages/cartpage.robot
Resource  ../../locators/cartpage_locators.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC005 Verifying product added reflects in cart
    [Documentation]  Test Case 5 adding a product to cart
    [Tags]  integration
    Sleep    5s
    Clicking on Accounts
    Sleep    5s
    Log in to Gully Labs    ${USER_EMAIL}    ${USER_PWD}
    Sleep    5s
    Search a product
    Sleep    5s

    Add to Cart

    ${product_name}=  Get Text    ${product_name_locator}
    ${actual_quantity}=  Get Element Attribute    ${actual_quantity_locator}    value
    ${size_value}=  Get Text    ${size}

#    Page Should Contain    CART

    Wait Until Element Is Visible    ${cart_product_name_locator}  timeout=10s
    ${cart_product_name}=  Get Text    ${cart_product_name_locator}
    Should Not Be Empty    ${cart_product_name}

    Log To Console    ${cart_product_name}
    ${cart_quantity}=  Get Element Attribute    ${cart_product_quantity_locator}    value


    Should Contain    ${cart_product_name}    ${product_name}
    Should Be Equal    ${cart_quantity}    ${actual_quantity}
    Should Contain    ${cart_product_name}    ${size_value}