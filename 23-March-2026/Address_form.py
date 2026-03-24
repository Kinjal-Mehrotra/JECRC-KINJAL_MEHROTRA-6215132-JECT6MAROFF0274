

from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get(r'D:\Selenium\23-March-2026\address_page.html')
driver.maximize_window()
sleep(3)

present_address=driver.find_element(By.ID,'presentAddress')
permanent_address=driver.find_element(By.ID,'permanentAddress')

present_address.send_keys('JECRC, JAIPUR, RJ')
sleep(2)
present_address.click()
action=ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
sleep(2)

action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
permanent_address.click()

sleep(2)
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
sleep(2)

