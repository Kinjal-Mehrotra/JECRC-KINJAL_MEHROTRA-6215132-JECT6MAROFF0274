from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)

driver.get(r'D:\Selenium\20-March-2026\playlist.html')
driver.maximize_window()

songs=driver.find_element(By.ID,'songs')
select=Select(songs)

list_of_fav=driver.find_elements(By.XPATH,'//optgroup[@label="Ed Sheeran"]/option')

if select.is_multiple:
    for song in list_of_fav:
        select.select_by_visible_text(song.text)
        print(song.text)

driver.find_element(By.TAG_NAME,'button').click()

