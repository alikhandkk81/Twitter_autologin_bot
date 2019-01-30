#!/usr/bin/python3

##############################################
#              Twitter autologin bot         #
#              Coded By alikhandkk81         #       
#                01/6/019                    #
##############################################

from selenium import webdriver

username = "your username"
password = "your password"

url = "https://twitter.com/login/"

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")

driver.get(url)

driver.find_element_by_class_name('js-username-field').send_keys(username)
driver.find_element_by_class_name('js-password-field').send_keys(password)
driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium').submit()

