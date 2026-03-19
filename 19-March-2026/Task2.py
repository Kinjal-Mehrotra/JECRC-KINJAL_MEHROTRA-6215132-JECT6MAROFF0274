#navigate to this website and fill this form

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://qavbox.github.io/demo/signup/')
driver.maximize_window()

wait=WebDriverWait(driver,5)

full_name=wait.until(ec.visibility_of_element_located((By.ID,'username')))
full_name.send_keys('KM')

email=wait.until(ec.visibility_of_element_located((By.ID,'email')))
email.send_keys('km@gmail.com')

number=wait.until(ec.visibility_of_element_located((By.ID,'tel')))
number.send_keys('7777777777')

upload=wait.until(ec.visibility_of_element_located((By.XPATH,'//input[@name="datafile"]')))
upload.send_keys(r'C:\Users\hp\OneDrive\Pictures\wallpapers\Screenshot 2024-07-21 195656.png')

country_dropdown=wait.until(ec.visibility_of_element_located((By.NAME,'sgender')))
dropdown=Select(country_dropdown)
dropdown.select_by_value('female')

experience=wait.until(ec.visibility_of_element_located((By.XPATH,'//input[@value="four"]')))
experience.click()

skills=wait.until(ec.visibility_of_all_elements_located((By.XPATH,'//label[@for="skills"]/following-sibling::input')))
for skill in skills:
    if skill.get_attribute('value')=="automationtesting" or  skill.get_attribute('value')=="html":
        skill.click()


tools=wait.until(ec.visibility_of_element_located((By.ID,'tools')))
auto_tools=Select(tools)
auto_tools.select_by_visible_text('Selenium')

submit=wait.until(ec.element_to_be_clickable((By.ID,'submit')))
submit.click()

