### OrangeHRM Login

# Automate the login flow in OrangeHRM and verify that the user successfully reaches the dashboard:

# 1. Open the OrangeHRM demo website. `https://opensource-demo.orangehrmlive.com/`
# 2. Get and print the title of the page.
# 3. Locate the username input field and use clear() if needed.
# 4. Enter the username using send_keys().
# 5. Locate the password input field and enter the password using send_keys().
# 6. Submit the login form using either: click() on the Login button, or Keys.ENTER
# 7. After login, print the current URL.
# 8. Check if dashboard is present in that url using `in`
# 9. Print 'successful login'

# Test Data:

# Username: `Admin`
# Password: `admin123`

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://opensource-demo.orangehrmlive.com/')
sleep(2)
driver.maximize_window()
print(f"Printing the title of page: {driver.title}")

sleep(2)
#locating the username field and use clear() if needed
user_name=driver.find_element(By.NAME,'username')
user_name.clear()

#sending value
user_name.send_keys('Admin')

#locating password
password=driver.find_element(By.NAME,'password')
password.send_keys('admin123')

#clicking the login button
driver.find_element(By.XPATH,'//button[@type="submit"]').click()

#printing current url
curr_url=driver.current_url
print(f"Current url of the page: {curr_url}")

#checking if dashboard is present in url
if 'dashboard' in curr_url:
    print("Yes, 'dashboard' is present in current url")


print("Login successful")
sleep(10)
driver.quit()
