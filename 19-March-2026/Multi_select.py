from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

multi_drop=driver.find_element(By.ID,'colors')
select=Select(multi_drop)

if select.is_multiple:
    select.select_by_value('blue')
    select.select_by_index(5)
    select.select_by_visible_text('Yellow')

list_of_colors=[i.text for i in select.all_selected_options]
print(list_of_colors)
select.deselect_by_value('blue')
list_of_colors_2=[i.text for i in select.all_selected_options]
print(list_of_colors_2)