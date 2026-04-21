*** Variables ***



${product_to_add}  xpath=(//div[@id='ProductGridContainer']/descendant::div[@class='product-card__media relative h-auto']/descendant::a)[5]

${size_dropdwon}  xpath=(//select[@class='select'])[2]
${add_button}  xpath=//button[@name='add']

${close_cart_page_button}  xpath=//button[@data-entity-id="Close"]

#${product_name_locator}  xpath=//section[@class='title']/h1
#${cart_button}  xpath=//li[@class='cartCounter']/button
#${cart_product_name_locator}  xpath=//span[@class='title']


#${product_to_add}  xpath=//div[@class="card-image"]/descendant::a
##(//section[@class="results product"]/descendant::a[@tabindex=-1])[2]
#
##${gender}  xpath=//a[text()="WOMEN"]
#
#${size}  xpath=//label[contains(text(),"UK 5")]
#${increase_quantity}  xpath=//button[@name='plus']
#${add_button}  id=ProductSubmitButton-template--25420726436124__main
#
#${product_name_locator}  xpath=//section[@class='title']/h1
#${cart_button}  xpath=//li[@class='cartCounter']/button
#${cart_product_name_locator}  xpath=//span[@class='title']
#
#${actual_quantity_locator}  xpath=//input[@class='quantity__input']
#${cart_product_quantity_locator}  xpath=(//input[@type='number'])[1]