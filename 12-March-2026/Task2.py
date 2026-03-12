#write a for loop to open/ close a url using all the browsers
from selenium import webdriver
from time import sleep
browsers=[webdriver.Chrome, webdriver.Edge, webdriver.Firefox]
for browser in browsers:
    driver=browser()
    driver.get('https://github.com/')
    sleep(5)
    driver.quit()
