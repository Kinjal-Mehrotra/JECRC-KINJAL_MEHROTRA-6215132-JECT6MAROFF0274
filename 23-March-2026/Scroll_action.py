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
driver.get('https://www.supertails.com/')
driver.maximize_window()
sleep(3)

cat=driver.find_element(By.XPATH,'//div[@data-ganame="Breed 5"]')
action=ActionChains(driver)
action.scroll_to_element(cat).perform()
sleep(3)

#scroll_to - scroll to the exact pixel location, if u wanna scroll up give negative values , if u wanna scroll down u give positive value
# scroll_by - scrolls to that many pixel by a particular location
#top of the page is 0,0
action.scroll_by_amount(0,-100).perform()
sleep(3)
action.scroll_by_amount(0,-300).perform()
sleep(3)
action.scroll_by_amount(100,0).perform()

#right click of mouse
action.context_click(cat).perform()

action.double_click(cat).perform()
