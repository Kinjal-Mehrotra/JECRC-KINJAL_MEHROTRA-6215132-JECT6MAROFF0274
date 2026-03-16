from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
# opts.add_argument('--headless')
driver=webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
sleep(5)

driver.find_element(By.PARTIAL_LINK_TEXT,'Udemy')
#we can pass a substring in partial link text unlike link text

print("Found the element using partial link text")
