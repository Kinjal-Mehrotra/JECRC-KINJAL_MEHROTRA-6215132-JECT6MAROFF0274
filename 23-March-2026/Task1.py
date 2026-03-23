#Open your favorite ipl team website, go to favourite picture , scroll up five times

from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from selenium.webdriver.common.keys import Keys


opts=ChromiumOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.royalchallengers.com/')
driver.maximize_window()
sleep(2)

wait=WebDriverWait(driver,5)
image=wait.until(ec.presence_of_element_located((By.XPATH,'(//div[@class="prod-inr"]/descendant::img)[6]')))
action=ActionChains(driver)

action.scroll_to_element(image).perform()
sleep(2)

for i in range(5):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(2)

sleep(10)
driver.quit()