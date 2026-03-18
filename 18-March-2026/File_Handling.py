#upload a file , then download the same
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()
sleep(2)

file_upload_link=driver.find_element(By.XPATH,'//a[text()="File Upload"]')
file_upload_link.click()
sleep(2)

upload=driver.find_element(By.ID,'file-upload')
upload.send_keys(r"C:\Users\hp\OneDrive\Pictures\wallpapers\Screenshot 2024-07-21 195233.png")
submit_button=driver.find_element(By.ID,'file-submit')
submit_button.click()
sleep(1)

#now to download
driver.get('https://the-internet.herokuapp.com/')
sleep(1)
download_page=driver.find_element(By.XPATH,'//a[text()="File Download"]')
download_page.click()
sleep(2)

image_to_be_downloaded=driver.find_element(By.XPATH,'//a[text()="Screenshot 2024-07-21 195233.png"]')
image_to_be_downloaded.click()
sleep(15)
print("File successfully uploaded and downloaded")
driver.quit()

