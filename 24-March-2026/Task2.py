## Task 2
### Alerts
# 1. navigate to the url: `https://demoqa.com/alerts`
# 2. work on all the 4 alerts one after the other
# 3. validate the result appearing, eg: for `ok` you should assert with it the result shown

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/alerts')

#alert button
driver.find_element(By.ID,'alertButton').click()
sleep(2)
alert=driver.switch_to.alert
alert.accept()

#timer alert
wait=WebDriverWait(driver,5)
driver.find_element(By.ID,'timerAlertButton').click()
sleep(2)
alert=wait.until(ec.alert_is_present())
alert.accept()

#accepting confirm alert
driver.find_element(By.ID,'confirmButton').click()
sleep(2)
alert=driver.switch_to.alert
alert.accept()

msg1=driver.find_element(By.XPATH,'(//div[@class="col-md-6"])[3]/span[2]')
assert 'Ok' in msg1.text, 'Error'

#dismissing confirm alert
driver.find_element(By.ID,'confirmButton').click()
sleep(2)
alert=driver.switch_to.alert
alert.dismiss()

msg2=driver.find_element(By.XPATH,'(//div[@class="col-md-6"])[3]/span[2]')
assert 'Cancel' in msg1.text, 'Error'

#prompt alert
driver.find_element(By.ID,'promtButton').click()
alert=driver.switch_to.alert
sleep(2)
alert.send_keys('Hello')
alert.accept()

#validating message

msg3=driver.find_element(By.ID,'promptResult')
assert 'Hello' in msg3.text,'Error'

#dismissing prompt
driver.find_element(By.ID,'promtButton').click()
sleep(2)
alert=driver.switch_to.alert
alert.dismiss()
