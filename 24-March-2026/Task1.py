# ## Task 1
# ### https://codepen.io/gdw96/pen/jOypoYL
# 1. navigate to the above url
# 2. enter username and password
# 3. click on hold on the eye to view password
# 4. click on register
# 5. Use sleep for 5sec then refresh the page
# 6. Validate the word `Registration` using assert

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

driver.get('https://codepen.io/gdw96/pen/jOypoYL')

# wait=WebDriverWait(driver,5)
# iframe1=wait.until(ec.presence_of_element_located((By.ID,'result')))
iframe1=driver.find_element(By.ID,'result')
driver.switch_to.frame(iframe1)

username=driver.find_element(By.ID,'username')
driver.execute_script("arguments[0].value='ABC';",username)

email=driver.find_element(By.ID,'email')
driver.execute_script("arguments[0].value='abc@gmail.com';",email)

password=driver.find_element(By.ID,'password')
driver.execute_script("arguments[0].value='12345679';",password)

action=ActionChains(driver)
show_password=driver.find_element(By.ID,'showPsswd')
action.click_and_hold(show_password).perform()
sleep(3)

register_button=driver.find_element(By.XPATH,'//input[@value="Register"]')
register_button.click()

sleep(5)

#driver.refresh()
driver.back()

iframe1=driver.find_element(By.ID,'result')
driver.switch_to.frame(iframe1)
# iframe1=wait.until(ec.presence_of_element_located((By.ID,'result')))
# driver.switch_to.frame(iframe1)
element=driver.find_element(By.TAG_NAME,"h1")
assert 'Registration' in element.text, "Couldn't find registration page"
print("Registration successful")