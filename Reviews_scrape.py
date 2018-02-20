# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:40:40 2017

@author: Vibhuti
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url1="http://app.listen360.com"

#Provide the URL from the location you want to pull the data
url = input('Enter - ')  
n=0 #set the counter for the page
# Save the reviews into a text file
file = open('reviews.txt','w')  
# This code won't be able to extract the reviews to a text file if the reviews has Emojis.
# Use this link to resolve the issue:
# https://stackoverflow.com/questions/47436649/trying-to-extract-tweets-with-tweepy-but-emojis-make-it-crash  

while(n!=313):
    html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
    soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
    atags = soup('a') #Retrieve the anchor tag 
#    ptags = soup('p') 


    for atag in atags:
    #Retrieve strings from atags tag and convert it to number
       if((atag.get('rel'))==['next']):
            url2=atag.get('href',None) #get all the reviews tagged with an anchor tag
            url=url1+url2
    
    for ptag in ptags:
          file = open('reviews.txt','a')
          file.write(ptag.text)
          file.close()
    n=n+1
    print(n) #print the reviews into The console.


    
        
        