from selenium import webdriver
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


def call():
	users_ref = db.collection('participants')
	docs = users_ref.stream()
	for doc in docs:
		db.collection('participants').document(doc.id).delete()

	browser = webdriver.Chrome(executable_path='/Users/dewanshrawat/Desktop/selenium/chromedriver')#add your chrome path here
	hastag = 'devdays0011'
	url = 'https://twitter.com/hashtag/'
	link = url + hastag
	browser.get(link)

	tweets = browser.find_elements_by_class_name('content')
	val = []
	data = []
	for i in range(0,len(tweets)):
		c = tweets[i].text
		c = c.replace('\n', ' ')
		a = c.split(" ")
		for j in a:
			data.append(j)

	# print(data)

	li = []
	dict = {}
	for i in range(len(data)):
		c = data[i]
		if '@' in c:
			username = c
			time = data[i+1][0]
		elif 'Like' in c:
			if data[i+1].isdigit():
				likes = data[i+1]
			else:
				likes = 0
		else:
			continue
		try:
			if likes == -1:
				continue
			dict = {'username':username , 'likes':likes, 'time':time}
			likes = -1
			li.append(dict)
		except:
			continue

	# print(li)


	doc_ref = db.collection('participants')
	for i in li:
		doc_ref.add(i)

	browser.close()


while True:
	call()
	time.sleep(15)
