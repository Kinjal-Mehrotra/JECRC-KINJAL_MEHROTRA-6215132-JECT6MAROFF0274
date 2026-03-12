from selenium import webdriver
#helps selenium to control thr browser
from time import sleep #adds a pause for the python script, pauses execution for certain time

#chromeoptions - a class that has configurations you provide to chrome before the browser opens
# driver=webdriver.Chrome() #it will open chrome browser
# driver.get('https://supertails.com/')
# driver.maximize_window()
# sleep(5)
# driver.back()
# sleep(3)
# driver.forward()
# sleep(3)
# driver.refresh()
# # driver.minimize_window()
# sleep(5)

#adding chrome options
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True) #its better to use this method instead of writing sleep method again and again
driver1=webdriver.Chrome(options=opts)
driver1.get('https://github.com/')
print(f"Title of wesbite: {driver1.title}")

# driver1.back()
# driver1.sleep(3)
# driver1.forward()
driver1.maximize_window()
