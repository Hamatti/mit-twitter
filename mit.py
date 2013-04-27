# -*- coding: utf-8 -*- 
import time
import tweepy, re
from datetime import date
import sqlite3 as sql
import os, signal, sys, base64
import urllib, urllib2
import mimetypes, types
from bs4 import BeautifulSoup

conn = sql.connect('mit.db')
c = conn.cursor()

# Twitter API authentication info
username = ""
password = ""

auth = tweepy.auth.BasicAuthHandler(username, base64.b64decode(password))
api = tweepy.API(auth)

search_query = "#mitshooting"
toolbar_width = 15

while True:
    results = api.search(search_query, include_entities=True)

    for result in results:
        user = result.from_user
        tweet = result.text
        print "%s: %s" % (user, tweet)
        try:
            insertables = (user.encode('utf-8'), tweet.encode('utf-8'))
            c.execute("INSERT INTO tweets VALUES (?, ?)", insertables)
            conn.commit()
        except:
            pass

    time.sleep(15)

c.close()
