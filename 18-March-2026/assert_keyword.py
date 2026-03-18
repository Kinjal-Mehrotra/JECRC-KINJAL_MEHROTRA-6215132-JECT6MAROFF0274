from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(5)

eye=driver.find_element(By.ID,'lrd1')
# print(eye.text)
#assert is a keyword in python , it checks if a statement is true or false, if its true it will continue otherwise it gives assertion error
assert'EYEGLASSES' in eye.text,  "Didn't find" #this is true

# assert'GLASSES'== eye.text,  "Didn't find" #this is true
#if condition is false , driver doesn't quit
#assert is used for validation instead of if statement
# driver.quit()

#
# driver.get('https://www.lenskart.com/lenskart-air-la-e17269-c1-eyeglasses.html')
# sleep(3)
# # pincode=driver.find_element(By.XPATH,'//p[@title="Enter pincode"]')
# pincode=driver.find_element(By.XPATH,'//div[@class="sc-a3b31f26-12 hyBEjt"]/p')
#
# pincode.click()
#
# sleep(2)
# check_button_2=driver.find_element(By.XPATH,"//div[@class='sc-a3b31f26-14 fDEfLM']")
# print(check_button_2.is_enabled())
#
