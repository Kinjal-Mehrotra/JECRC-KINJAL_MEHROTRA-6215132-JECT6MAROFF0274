import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
sleep(2)

#simple alert
alert_button=driver.find_element(By.XPATH,'(//button)[1]')
alert_button.click()
sleep(2)
alert=driver.switch_to.alert
alert.accept()
sleep(2)

#confirm alert - accepting
confirm_alert_button=driver.find_element(By.XPATH,'(//button)[2]')
confirm_alert_button.click()
alert=driver.switch_to.alert
sleep(2)
alert.accept()


#confirm alert - dismissing
confirm_alert_button=driver.find_element(By.XPATH,'(//button)[2]')
confirm_alert_button.click()
alert=driver.switch_to.alert
sleep(2)
alert.dismiss()

#prompt alert - sending values
prompt_alert_button=driver.find_element(By.XPATH,'(//button)[3]')
prompt_alert_button.click()
alert=driver.switch_to.alert
alert.send_keys('asdfghjkl')
sleep(2)
alert.accept()

#switching to the element using waits
wait=WebDriverWait(driver,5)
driver.find_element(By.XPATH,'(//button)[1]').click()
alert=wait.until(ec.alert_is_present())
sleep(2)
alert.accept()

sleep(5)
driver.quit()