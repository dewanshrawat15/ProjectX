from selenium import webdriver
import csv
import time
import os
from os import system, name

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

clear()

browser = webdriver.Chrome(executable_path='/Users/dewanshrawat/Desktop/selenium/chromedriver')
hastag = 'devdays191117'
url = 'https://twitter.com/hashtag/'
link = url + hastag
browser.get(link)
time.sleep(6)
content = browser.find_elements_by_tag_name('article')
l = []
for i in content:
	l.append(i.get_attribute('class'))
print(l)
browser.close()
