from selenium import webdriver
#helps selenium to control thr browser
from time import sleep #adds a pause for the python script, pauses execution for certain time

#firefoxoptions - a class that has configurations you provide to chrome before the browser opens

#firefoxoptions - a class that has configurations you provide to chrome before the browser opens
driver=webdriver.Firefox() #it will open chrome browser
driver.get('https://supertails.com/')
driver.maximize_window()
sleep(5)
driver.back()
sleep(3)
driver.forward()
sleep(3)
driver.refresh()
# driver.minimize_window()
sleep(5)

# #firefox options
# opts=webdriver.FirefoxOptions()
# opts.add_argument('detach')
# #opts.set_preference('detach',True)
# driver2=webdriver.Firefox(options=opts)
# driver2.get('https://supertails.com/')


