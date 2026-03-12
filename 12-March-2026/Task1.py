#Write a script to perform all the functions for chrome
from selenium import webdriver
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_expeimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://github.com/')
driver.maximize_window()
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(1)
driver.minimize_window()
driver.quit()