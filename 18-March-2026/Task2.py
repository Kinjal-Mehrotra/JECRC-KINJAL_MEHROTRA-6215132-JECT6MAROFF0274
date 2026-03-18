### Registration Form
# 1. Go to: https://demoqa.com/automation-practice-form
# 2. Handle every element in that form except the calendar
# `Note: Give fake names and emails`
# 3. Click on submit button

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()
sleep(2)

#sending first name
first_name=driver.find_element(By.ID,'firstName')
first_name.send_keys('K')

#sending last name
last_name=driver.find_element(By.ID,'lastName')
last_name.send_keys('M')

#sending email
email=driver.find_element(By.ID,'userEmail')
email.send_keys('km@gmail.com')

#gender button
driver.find_element(By.XPATH,'//input[@value="Female"]').click()

#sending mobile number
mobile=driver.find_element(By.ID,'userNumber')
mobile.send_keys('9999999999')

#sending subject
# subject_field=driver.find_element(By.ID,'subjectsInput')
# subject_field.send_keys('Physics')

#clicking hobbies checkbox
# checkboxes=driver.find_elements(By.XPATH,'//input[@type="checkbox"]')

checkboxes=driver.find_elements(By.XPATH,'//div[@id="hobbiesWrapper"]/descendant::input')
for hobby in checkboxes:
    if hobby.get_attribute('value')=="1":
        continue
    hobby.click()

#uploading picture
upload_picture=driver.find_element(By.ID,'uploadPicture')
upload_picture.send_keys(r"C:\Users\hp\OneDrive\Pictures\wallpapers\Screenshot 2024-07-21 195656.png")

#sending current address
current_address=driver.find_element(By.ID,'currentAddress')
current_address.send_keys('ABC street 1, city 1, State, pincode')

#state and city dropdowns
state=driver.find_element(By.ID,'react-select-3-input')
state.send_keys('Uttar Pradesh',Keys.ENTER)

city=driver.find_element(By.ID,'react-select-4-input')
city.send_keys('Lucknow',Keys.ENTER)

#clicking submit button
sleep(1)
submit_button=driver.find_element(By.ID,'submit')
submit_button.click()

print("Form successfully submitted")
