from selenium import webdriver
#helps selenium to control thr browser
from time import sleep #adds a pause for the python script, pauses execution for certain time

#edgeoptions - a class that has configurations you provide to chrome before the browser opens

# #edge options
# opts=webdriver.EdgeOptions()
# opts.add_experimental_option('detach',True) #its better to use this method instead of writing sleep method again and again
# driver1=webdriver.Edge(options=opts)
# driver1.get('https://supertails.com/')
# driver1.maximize_window()



driver=webdriver.Edge
driver.get('https://in.pinterest.com/')
driver.maximize_window()
sleep(5)
driver.back()
sleep(3)
driver.forward()
sleep(3)
driver.refresh()
sleep(5)

