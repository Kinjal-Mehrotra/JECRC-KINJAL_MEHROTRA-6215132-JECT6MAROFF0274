#its powerful as you can traverse in any direction
#u can find elements using inner text
#two types of xpath - relative(//html) and absolute(/html)

#slower as compared to other locators as it traverses back and forth
#difficult to read

# absolute xpath : /html/body/div/input[@attribute_name="value"]
# better to use relative xpath
# relative xpath: directly go to any place using the //tag_name[@attribute="value"]

from selenium import webdriver
from selenium.webdriver.common.by import By
#imported by class
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
# opts.add_argument('--headless')
driver=webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(1)

element1=driver.find_element(By.XPATH,'//input[@maxlength="15"]')
element2=driver.find_element(By.XPATH,'//label[@for="gender"]')
element3=driver.find_element(By.XPATH,'//button[@type="submit"]')
element4=driver.find_element(By.XPATH,'//input[@placeholder="End Date"]')
element5=driver.find_element(By.XPATH,'//style[@type="text/css"]')
print(element1,element2,element3,element4,element5)
print("Script successfully terminated")

#using inner text in xpath
element6=driver.find_element(By.XPATH,'//a[text()="Home"]')
element7=driver.find_element(By.XPATH,'(//a[text()="Home"])[1]')
element8=driver.find_element(By.XPATH,'//a[text()="GUI Elements"]')
element9=driver.find_element(By.XPATH,'//label[text()="Email:"]')

#using contains keyword to handle extra spaces in the text
element10=driver.find_element(By.XPATH,'//label[contains(text(),"Male")]')
element11=driver.find_element(By.XPATH,'//option[contains(text(),"Blue")]')