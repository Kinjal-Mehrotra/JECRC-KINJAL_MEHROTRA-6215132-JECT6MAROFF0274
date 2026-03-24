#Open myntra, hover over men/women, choose any category, then click on it , scroll to 4th or 5th row product , use proper waits

from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.myntra.com/')
driver.maximize_window()
sleep(2)

wait=WebDriverWait(driver,5)
action=ActionChains(driver)
women_section=wait.until(ec.visibility_of_element_located((By.XPATH,'(//div[@class="desktop-navLink"])[2]/a')))
action.move_to_element(women_section).perform()

category=wait.until(ec.visibility_of_element_located((By.XPATH,'//li[@data-reactid="218"]')))
category.click()

fourth_row=wait.until(ec.presence_of_element_located((By.XPATH,'(//ul[@class="results-base"]/li)[16]')))
action.scroll_to_element(fourth_row).perform()

sleep(10)
driver.quit()