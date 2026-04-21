*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/cartpage_locators.robot

*** Keywords ***
Add to Cart
    [Documentation]  this will add the product to cart
    Log  Adding product to cart
    Click Element    ${product_to_add}
    Sleep    2s

#    ${options}  Get List Items    ${size_dropdwon}
    Select From List By Value    ${size_dropdwon}  UK 4
    Sleep    1s

    Wait Until Element Is Visible    ${add_button}
    Sleep    2s
    Click Element    ${add_button}

    Page Should Contain    Cart



#    [Documentation]  this will add the product to cart
#    Log  Adding product to cart
#    Click Element    ${product_to_add}
#    Sleep    2s
#
#    Wait Until Element Is Enabled    ${size}
#    Click Element    ${size}
#    Sleep    2s
#
#    Execute Javascript  window.scrollBy(0,1000)
#    Wait Until Element Is Visible    ${increase_quantity}
#    Sleep    2s
#    Click Element    ${increase_quantity}
#
#
#    Wait Until Element Is Visible    ${add_button}
#    Sleep    2s
#    Click Element    ${add_button}
#
#
#    Page Should Contain    CART

