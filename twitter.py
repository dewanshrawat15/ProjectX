from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.ChromeOptions()
options.add_argument("--headless")


browser = webdriver.Chrome(options=options,executable_path='/Users/dewanshrawat/Desktop/selenium/chromedriver')#add your chrome path here
hastag = 'devdays191117'
url = 'https://twitter.com/hashtag/'
link = url + hastag
browser.get(link)

tweets = browser.find_elements_by_class_name('content')
for i in range(0,len(tweets)):
	print(tweets[i].text)
