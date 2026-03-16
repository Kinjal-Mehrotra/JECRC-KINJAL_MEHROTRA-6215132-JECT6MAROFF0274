from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

name=driver.find_element(By.ID,'name')
name.clear()
#send value which u give to the field
name.send_keys('Kinjal')
sleep(1)

print(name.get_attribute('placeholder'))
print(name.get_attribute('value'))
email=driver.find_element(By.XPATH,'//input[@placeholder="Enter EMail"]')
email.send_keys('kinjalmehrotra123@gmail.com')

# driver.find_element(By.XPATH,'//label[text()="Monday"]/preceding-sibling::input').click()

#how to get text from a tag
monday_checkbox=driver.find_element(By.XPATH,'//input[@id="monday"]/following-sibling::label')
print(monday_checkbox.text)
sleep(1)
#toggle male and female radio button
genders=driver.find_elements(By.XPATH,'//input[@name="gender"]')
for gender in genders:
    gender.click()
    sleep(2)

checkboxes=driver.find_elements(By.XPATH,'//div[@class="form-group"]/descendant::input[@type="checkbox"]')
days = driver.find_elements(By.XPATH,'//label[@class="form-check-label"]')
i=2
for checkbox in checkboxes:
    checkbox.click()
    print(days[i].text)
    i+=1
    sleep(1)

checkboxes=checkboxes[::-1]
for checkbox in checkboxes:
    checkbox.click()
    sleep(1)

sleep(10)

driver.quit()

