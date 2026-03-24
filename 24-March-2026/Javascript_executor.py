#we can use screenshots whenever there is an error
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://in.pinterest.com/')
driver.maximize_window()
sleep(2)

driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(3)

driver.execute_script('window.scrollTo(0,0);')
sleep(2)

driver.execute_script('window.scrollBy(0,500);')
sleep(2)
driver.execute_script('window.scrollBy(0,-200);')
sleep(2)

element=driver.find_element(By.XPATH,'//div[contains(text(),"Join Pinterest")]')
driver.execute_script('arguments[0].scrollIntoView();',element)
sleep(2)

driver.execute_script('arguments[0].click();',element)
sleep(2)

driver.quit()