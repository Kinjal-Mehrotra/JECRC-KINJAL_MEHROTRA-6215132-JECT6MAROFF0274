#we can use screenshots whenever there is an error
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#get current working directory and join screenshots folder to it
folder=os.path.join(os.getcwd(),'screenshots')
os.makedirs(folder,exist_ok=True)

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://in.pinterest.com/')
driver.maximize_window()

sleep(2)

driver.save_screenshot(f'{folder}/full_page_ss.png')

picture=driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"]/descendant::img)[3]')
action=ActionChains(driver)
action.scroll_to_element(picture).perform()
picture.screenshot(f'{folder}/picture1.png')
sleep(2)
picture2=driver.find_element(By.XPATH,"//img[contains(@alt,'bold lip')]")
action.scroll_to_element(picture2).perform()
sleep(2)
picture2.screenshot(f'{folder}/picture2.png')
sleep(5)
driver.quit()