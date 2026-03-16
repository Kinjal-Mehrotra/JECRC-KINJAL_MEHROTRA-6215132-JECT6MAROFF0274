# ## Task 2
#
# ### Radio Buttons
#
# Automate interaction with radio buttons `https://demoqa.com/radio-button`
#
# 1. Open the radio button page.
# 2. Print the **title** of the page.
# 3. Locate the **"Yes" radio button**.
# 4. Click the radio button using `click()`.
# 5. Capture and print the **result message** using `.text`.
# 6. Use `get_attribute()` to fetch attributes like:
#    - `class`
#    - `id`
# 7. Print the **current URL**.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/radio-button')
driver.maximize_window()
sleep(2)
#printing title of the page
print(f"The title of the page is: {driver.title}")
sleep(1)

#locating the yes radio button
yes_button=driver.find_element(By.ID,'yesRadio')
yes_button.click()
sleep(1)

#getting the message
statement=driver.find_element(By.XPATH,'//p[@class="mt-3"]')
print(f"Printing the result message: {statement.text}")

#using use_attribute()
print(f"--Printing attributes of yes button--")
print(f"ID of yes_button: {yes_button.get_attribute('ID')}")
print(f"Type of yes_button: {yes_button.get_attribute('type')}")
print(f"Class of yes_button: {yes_button.get_attribute('class')}")

print("--Printing attributes of statement--")
print(f"Class of statement: {statement.get_attribute('class')}")

#printing current_url
print(f"Current URL: {driver.current_url}")

sleep(10)
driver.quit()
