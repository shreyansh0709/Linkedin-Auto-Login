from typing import List

from selenium.webdriver.remote.webelement import WebElement
from tools.selenium_tools import send_keys

import parameters
from time import sleep
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

writer = csv.writer(open(parameters.file_name, 'w'))

writer.writerow(['Name','Job Title','Company','College', 'Location','URL'])

driver = webdriver.Chrome('C:/Users/Lenovo/Desktop/chromedriver')

driver.get('https://www.linkedin.com/login')

driver.find_element_by_xpath("//input[@id='username']").send_keys('Add your LinkedIn email adress')

sleep(2)

driver.find_element_by_xpath("//input[@id='password']").send_keys('Add your LinkedIn password')

driver.find_element_by_xpath("//button[@type='submit']").click()

sleep(5)
