from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(1)
male=driver.find_element(By.XPATH,'//input[@id="male"]')
print(male.is_displayed()) #returns true if that is visible on the screen
print(male.is_enabled()) #returns true if its enabled
print(male.is_selected()) #returns true if that is selected