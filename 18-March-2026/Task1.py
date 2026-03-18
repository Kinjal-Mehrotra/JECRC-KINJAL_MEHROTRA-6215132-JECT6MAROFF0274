
## Task 1
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

### Link Text & Partial Link Text
# 1. Go to https://the-internet.herokuapp.com/
# 2. Find the "Checkboxes" link using LINK_TEXT
# 3. Find the "Drag and Drop" link using PARTIAL_LINK_TEXT
# 4. Find how many <li> (list item) elements are on the page using find_elements and TAG_NAME. Print the count.
# 5. Navigate to https://the-internet.herokuapp.com/tables
# 6. Write an XPath to find the "Web Site" (td) for the person with email "jdoe@hotmail.com" in table 1 (Hint: Use text() and ancestor/following sibling or preceding-sibling).
# 7. Write an XPath to find the Delete link (a) for the person with Last Name "Bach" in table 1.
# 8. Write an XPath to find the second table `(<table>)` on the page using indexing.
# 9. Write an XPath to find the cell containing "$100.00" in table 2. Find its parent <tr> element.

#getting the website
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()
sleep(2)

#finding checkboxes link
checkboxes=driver.find_element(By.LINK_TEXT,'Checkboxes')

#finding drag and drop link
drag_and_drop=driver.find_element(By.PARTIAL_LINK_TEXT,'')

#finding count of li elements
li_elements=driver.find_elements(By.TAG_NAME,'li')
print(f"Total number of list item elements are : {len(li_elements)}")
sleep(2)

#navigating to new page
driver.get('https://the-internet.herokuapp.com/tables')
print("Navigating to tables page")
sleep(2)

#finding website for person with email - jdoe@hotmail.com
website=driver.find_element(By.XPATH,'//td[text()="jdoe@hotmail.com"]/following-sibling::td[2]')
print(f"Website name for jdoe@hotmail.com: {website}")
sleep(2)

#finding delete link for person with last name bach
last_name=driver.find_element(By.XPATH,'//td[text()="Bach"]/following-sibling::td/descendant::a[text()="delete"]')
print("Found the delete link for person with last name Bach")
sleep(2)

#finding table 2
table2=driver.find_element(By.XPATH,'//table[2]')
print("Found table 2")

#finding '$100.00' in table 2
find_due=driver.find_element(By.XPATH,'//table[2]/descendant::tr[4]/td[4]')
print(f"Found $100.00 in table 2")

