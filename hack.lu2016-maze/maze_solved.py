#! /usr/bin/python

#A hacked together script for solving Maze task at Hack.lu 2016

import requests
import re
from bs4 import BeautifulSoup
import time

username = 'sup3rs3cr3tus3r'
password = 'n0b0dyc4ngu3smyp4ssw0rd' 
url = 'https://cthulhu.fluxfingers.net:1507'

already_visited = []

def checkurl(link):
    global already_visited
    if link in already_visited:
        return False
    print(link)
    html_doc = requests.get(url+link, auth=(username, password)).content
    math = re.findall('(\d+)|([+*/-]+)', str(html_doc))
    print(html_doc)
    if not math:
        return
    already_visited.append(link)
    ##print(math)
    nr1 = int(math[0][0])
    nr2 = int(math[2][0])
    #print(math[1][1])
    if str(math[1][1]) == '+':
            tot = nr1 + nr2
    elif str(math[1][1]) == '-':
            tot = nr1 - nr2
    elif str(math[1][1]) == '/':
            tot = nr1 / nr2
    elif str(math[1][1]) == '*':
            tot = nr1 * nr2
    
    html_doc3 = requests.post(url+link, auth=(username, password), data = {'result':tot}).content
    #print(html_doc3)
    urllist2 = []	

    soup2 = BeautifulSoup(str(html_doc3), "html.parser")
    for link in soup2.find_all('a'):
        urllist2.append(link.get('href'))
    #print(urllist)
    #time.sleep(2)
    for urllink2 in urllist2:
        checkurl(urllink2)



	


urllist = []

html_doc = requests.get(url, auth=(username, password)).content

soup = BeautifulSoup(str(html_doc), "html.parser")
for link in soup.find_all('a'):
    urllist.append(link.get('href'))

urllist.remove("code.php")

for urllink in urllist:
	checkurl(urllink)
	



