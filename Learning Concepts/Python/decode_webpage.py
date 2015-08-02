# Program Name: Decode a Web Page
# Task Description:  print out a list of all the article titles on the New York Times homepage
# Parameter: N/A
#Example: N/A

import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)
title = soup.find('span', 'articletitle').string

#http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html