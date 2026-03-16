from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in/')
sleep(2)

driver.maximize_window()

search=driver.find_element(By.ID,'twotabsearchtextbox')
search.clear()
search.send_keys('Earphones')

#two ways to click a button
# 1. use .click method

search.clear()
search.send_keys('samsung s25')
search_button=driver.find_element(By.ID,'nav-search-submit-button')
search_button.click()
sleep(2)

# 2. Use keys class and use comma to give command

search1=driver.find_element(By.ID,'twotabsearchtextbox')
search1.clear()

print(search1.get_attribute('id'))

search1.send_keys('Earings in A.D')
print(search1.get_attribute('value'))
driver.find_element(By.ID,'nav-search-submit-button').click()

sleep(1)
driver.quit()