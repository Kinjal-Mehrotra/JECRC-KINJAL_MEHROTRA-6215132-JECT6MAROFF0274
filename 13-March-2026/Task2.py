# TASK-2
# 1.Go to https://the-internet.herokuapp.com/login.
# 2.Locate the username field using XPath with Tag and name attribute.
# 3.Locate the password field using XPath with Tag and id attribute.
# 4.Locate the "Login" button using XPath with Tag and type attribute.
# 5.Locate the "Elemental Selenium" link using its exact text with text().
# 5.Locate the main heading "Login Page" using contains() with text.

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#navigating to the website
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()
sleep(2)

#locating the username field using Xpath with tag and name attributes
driver.find_element(By.XPATH,'//input[@name="username"]')
print("Located the username field")

#locating the password field using XPath with Tag and id attribute.
driver.find_element(By.XPATH,'//input[@id="password"]')
print("Located the password field")

#locating the "Login" button using XPath with Tag and type attribute.
driver.find_element(By.XPATH,'//button[@type="submit"]')
print("Located the login button")

#locating the "Elemental Selenium" link using its exact text with text().
driver.find_element(By.XPATH,'//a[text()="Elemental Selenium"]')
print("Located the elemental selenium link")

#locating the main heading "Login Page" using contains() with text.
driver.find_element(By.XPATH,'//h2[contains(text(),"Login Page")]')
print("Located the main heading login page")