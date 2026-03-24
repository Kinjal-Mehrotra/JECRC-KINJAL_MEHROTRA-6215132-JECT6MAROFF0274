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
driver.get(r'D:\Selenium\23-March-2026\index1.html')
driver.maximize_window()

driver.find_element(By.ID,'password').send_keys('123456789')
wait=WebDriverWait(driver,5)
password_button=wait.until(ec.element_to_be_clickable((By.ID,'eyeBtn')))
action=ActionChains(driver)
action.click_and_hold(password_button).perform()
sleep(5)
action.release()

