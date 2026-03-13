#TASK-3
# 1. Navigate to https://www.amazon.in/
# 2. Locate the main search bar using its ID with a CSS Selector.
# 3. Locate the Amazon logo (usually an <a> tag with an ID like nav-logo sprites) using a CSS Selector.
# 4. Locate the "Cart" link/icon (often has an ID like nav-cart) using a CSS Selector.
# 5. Locate the "Sign in" link in the navigation bar (It might be inside a div with an ID like nav-tools. Use descendant way (space)).
# 6. Locate all the main category links in the navigation bar under "All"(e.g."Best Sellers", "Mobiles", "Today's Deals").
# Inspect their common parent and use descendant way and to find all the <a> tags within it.Use find_elements and print the count.

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#navigating to the website
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)

#locating main search bar
search_bar=driver.find_element(By.CSS_SELECTOR,'#twotabsearchtextbox')
print("Successfully found search bar ")

#locating the amazon logo
driver.find_element(By.CSS_SELECTOR,'a[id="nav-logo-sprites"]')
print("Sucessfully found the amazon logo")

#locating the cart link
driver.find_element(By.CSS_SELECTOR,"#nav-cart")
print("Sucessfully found the cart link")

#locating the sign in link
driver.find_element(By.CSS_SELECTOR,'div[id="nav-tools"] a[href*="signin"]')
print("Sucessfully found the sign-in link")

#locating all category links
#categories=driver.find_elements(By.CSS_SELECTOR,'div[id="nav-xshop"] li[class="nav-li"] div[class="nav-div"] a')
categories=driver.find_elements(By.CSS_SELECTOR,'div[id="nav-xshop"] a')
print(f"Count of all the main category links in the navigation bar: {len(categories)}")