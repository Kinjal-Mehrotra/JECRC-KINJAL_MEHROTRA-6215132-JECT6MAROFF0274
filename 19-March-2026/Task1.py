#go to abc.com , print all the links for the 8 banners on home page using presence of element located explicit wait

## Task 1

### abc.com To fetch banner images

# 1. Go to abc.com
# 2. Find the banners
# 3. Print the image links


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
driver.get('https://abc.com/')
driver.maximize_window()

wait=WebDriverWait(driver,6)
images=wait.until(ec.presence_of_all_elements_located((By.XPATH,'//div[@id="hero-items"]/descendant::picture/img')))
for image in images:
    print(image.get_attribute('src'))




