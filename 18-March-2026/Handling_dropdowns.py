from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
#
driver=webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window() #so that elements dont overlap

#select class is used to handle dropdowns
country_dropdown=driver.find_element(By.ID,'country')
#3 ways to select these options
# 1. By visible text
# 2. By index
# 3. By value

dropdown=Select(country_dropdown)
dropdown.select_by_value('australia')
sleep(5)
print("Selecting by value successful")

dropdown.select_by_index(4) #indexing here starts from 0
print("Selecting by index successful")
sleep(5)

dropdown.select_by_visible_text('India')
print("Selecting by visible text successful")
sleep(5)


