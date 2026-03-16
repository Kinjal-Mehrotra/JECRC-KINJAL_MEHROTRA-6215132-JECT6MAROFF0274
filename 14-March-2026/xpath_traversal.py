from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
opts.add_argument('--headless')
driver=webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in/')
sleep(5)

#using ancestor
all_text=driver.find_element(By.XPATH,'//span[text()="All"]/ancestor::div[@id="nav-main"]')
print("all text successfully found")

customer_service_text=driver.find_element(By.XPATH,'//a[text()="Customer Service"]/ancestor::div[@class="nav-div"]')
print("customer service text successfully found")

#using descendent 
fresh_text=driver.find_element(By.XPATH,'//div[@class="nav-div"]/descendant::a[text()="Fresh"]')
print("Found fresh text")

#finding siblings (preceding / following)
driver.find_element(By.XPATH,'//a[text()="Fresh"]/ancestor::li/following-sibling::li[1]')
print("Found element using siblings")

driver.get('https://testautomationpractice.blogspot.com/')

#using java to find price

driver.find_element(By.XPATH,'//td[text()="Learn Java"]/following-sibling::td[3]')
print("Found price using learn java")

#using amod to find selenium in first row 
list_of_subjects=driver.find_elements(By.XPATH,'//td[text()="300"]/preceding-sibling::td[3]')
print(f"subjects with price 300: {list_of_subjects}")
print(f"Total subjects with cost 300: {len(list_of_subjects)}")

#using table to find the subject names 
list_of_subjects=driver.find_elements(By.XPATH,'//table[@id="taskTable"]/descendant::tbody/descendant::tr/td[1]')
print(f"browser names: {list_of_subjects}")
print(f"Total browser names: {len(list_of_subjects)}")