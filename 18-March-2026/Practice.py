#Open lenskart website, search for a product, put a filter and print the text of the first image that comes

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(1)

search_box=driver.find_element(By.XPATH,'//input[@placeholder="What are you looking for?"]')
search_box.send_keys('Round glasses for women',Keys.ENTER)
sleep(2)
dropdown=driver.find_element(By.ID,'sortByDropdown')
filter_dropdown=Select(dropdown)
filter_dropdown.select_by_value('low_price')

first_image=driver.find_element(By.XPATH,"//div[@class='sc-bf32d8a7-0 gOVKHN']/descendant::div/p")
print(first_image.text)

driver.quit()

