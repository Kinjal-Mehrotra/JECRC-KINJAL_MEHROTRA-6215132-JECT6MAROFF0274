from selenium import webdriver
from selenium.webdriver.common.by import By
#imported by class
from time import sleep

#headless mode
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
# opts.add_argument('--headless')
driver=webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(1)

#finding using ID
name=driver.find_element(By.ID,'name')
#finds the first occurring element, if there is no such element , gives NO SUCH ELEMENT FOUND EXCEPTION
print(name)
print('name textfield found')

phone_number=driver.find_element(By.ID,'phone')
print('phone number textfield found')


navbar=driver.find_element(By.NAME,'Navbar')
print('Navigation bar was found')

radio_button=driver.find_element(By.CLASS_NAME,'form-check-input')
print('radio button found')

radio_buttons=driver.find_elements(By.CLASS_NAME,'form-check-input')
print(radio_buttons)
print(len(radio_buttons))
print('radio buttons found')

inp_elements=driver.find_elements(By.TAG_NAME,'input')
print(inp_elements)
print(len(inp_elements))

