*** Variables ***
${accounts}  xpath=(//shopify-account)[2]
${search}  xpath=(//a[@href='/search'])[2]
${search_field}  xpath=//input[@class='input search__input']
#${accounts}  xpath=//a[@href="/account/login"]
#${search}  xpath=//a[@href="/search"]
#${search_field}  id=Search-In-Template
${gullylabs_logo}  xpath=//a[@href='/']