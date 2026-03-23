from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

opts=ChromiumOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.supertails.com/')
driver.maximize_window()
sleep(3)
action=ActionChains(driver)
action.send_keys(Keys.PAGE_DOWN).perform()
sleep(2)
action.send_keys(Keys.PAGE_UP).perform()
sleep(2)

action.key_down(Keys.CONTROL).send_keys('a').perform()
sleep(2)
action.key_up(Keys.CONTROL).perform()
sleep(2)


