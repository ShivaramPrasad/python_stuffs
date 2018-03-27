from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
from six.moves import urllib
import sys
from espeak import espeak
espeak.set_voice("female2")
import time

espeak.synth("HAI SHIVA.. WHATSUP")
time.sleep(2)
espeak.synth("Enter the song which you need")
data = raw_input("\nEnter the song which you need: ")
time.sleep(2)
espeak.synth("please wait..")
print("please wait..")
espeak.synth("loading %s"%data)

browser = webdriver.Firefox()

url = "https://www.youtube.com"
browser.get(url)
assert 'YouTube' in browser.title

elem = browser.find_element_by_id('masthead-search-term' or 'search')  
q = elem.send_keys(data + Keys.RETURN)

#elem1 = browser.find_element_by_uniqueselector("#item-section-174700 > li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(1)")
new_url = "https://www.youtube.com/results?search_query="
ch = data.replace(" ","+")
new = new_url + ch
req = urllib.request.urlopen(new)
soup = bs4.BeautifulSoup(req, "lxml")
search1 = soup.findAll('h3')
search1[3]
data = search1[3].a["href"]

#for openning that particular song page
browser.get(url+data)

######## Data Readings #########
req1 = urllib.request.urlopen(url+data)
soup1 = bs4.BeautifulSoup(req1, "lxml")

#for content
search = soup1.findAll('div', {"id" : "watch7-content"})
content = search[0].meta["content"]

#coloring print stmt is used below
print("\n[+]Content :"+"\033[92m {}\033[00m" .format(content))

#for title
search4 = soup1.findAll('div', {"id" : "watch-headline-title"})
title = search4[0].h1.span["title"]
print("\n[+]Title of that track :"+"\033[92m {}\033[00m" .format(title))


#for views
search3 = soup1.findAll('div', {"class" : "watch-view-count"})
view = search3[0].text
views = view.replace(u'\xa0', ' ').encode('utf-8')
str_views = views.replace(" ", ",")
print("\n[+]Views for this song :"+"\033[92m {}\033[00m" .format(str_views))

print("\n")


'''
search2 = soup.findAll('button', {"class": "videoAdUiSkipButton videoAdUiAction videoAdUiFixedPaddingSkipButton"})
elem1 = search2[0]
time.sleep(10)
#elem1 = browser.find_element_by_class_name('videoAdUiSkipContainer html5-stop-propagation')
elem1.send_keys(Keys.RETURN)
'''


