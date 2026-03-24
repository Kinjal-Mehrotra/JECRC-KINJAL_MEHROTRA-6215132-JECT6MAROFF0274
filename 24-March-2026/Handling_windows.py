from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
sleep(3)

parent_window=driver.current_window_handle
driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
sleep(2)
all_windows=driver.window_handles #gives list of all the windows open
print(len(all_windows))

driver.switch_to.window(all_windows[-1])

assert 'New' in driver.find_element(By.CLASS_NAME,'example').text
print('Done')

driver.switch_to.window(parent_window)
driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()

driver.switch_to.new_window('window')
sleep(3)
driver.get('https://in.pinterest.com/')

driver.switch_to.new_window('tab')
sleep(3)

driver.get('https://abc.com')
sleep(3)

driver.quit()