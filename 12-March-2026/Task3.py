#write a script using a loop to print the tile, name and current url for all the three browsers
from selenium import webdriver
from time import sleep

browsers=[webdriver.Chrome, webdriver.Edge, webdriver.Firefox]
for browser in browsers:
    driver=browser()
    driver.get('https://github.com/')
    sleep(5)
    print(f"Title for browser: {driver.title}")
    print(f"Url for browser: {driver.current_url}")
    print(f"Name for browser: {driver.name}")
    driver.quit()
