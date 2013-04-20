# -*- coding: utf-8 -*- 

import sqlite3 as sql
from collections import defaultdict
import operator

def get_stopwords():
	words = []
	for line in open('stopwords.txt'):
		words.append(line.strip().lower())
	return words

def get_tweets(cursor):
	tweets = []
	query_results = cursor.execute('SELECT user FROM tweets WHERE user NOT LIKE "%free%"').fetchall()
	for res in query_results:
		if 'chair' in res[0]:
			continue
		tweets.append(res[0].replace('\n', '').replace('.', '').replace(':', '').replace(',', '').replace('"', '').replace('?','').replace('!', '').replace('(', '').replace(')', '').replace("'", "").strip())
	return tweets

def get_tweets_by_intervals(tweets):
	tweets_by_interval = dict()

	start_point = 0
	for iteration in range(1,11):
		tweets_by_interval[iteration] = set(all_tweets[start_point:INTERVAL*iteration])
		start_point += INTERVAL
	return tweets_by_interval

def clean_a_tweet(tweet):
	words = tweet.split(' ')
	cleaned = []
	for word in words:
		word = word.lower()
		if word in STOPWORDS or word.startswith('#') or word.startswith('@') or word == '' or word.startswith('http') or word in '123456789.?!,/+|' or word.startswith('"') or word.startswith('&'):
			continue
		else:
			cleaned.append(word.lower())
	return cleaned 

def clean_tweets(raw_tweets):
	cleaned = dict()
	for interval, tweets in raw_tweets.iteritems():
		cleaned[interval] = []
		for tweet in tweets:
			cleaned[interval].append(clean_a_tweet(tweet))
	return cleaned

def get_frequency_table(raw_tweets):
	freqs = defaultdict(int)
	for interval, tweets in raw_tweets.iteritems():
		for tweet in tweets:
			for word in tweet:
				freqs[word] += 1
	return freqs

DATABASE = 'mit.db'
INTERVAL = 3600
STOPWORDS = get_stopwords()
connection = sql.connect(DATABASE)
cursor = connection.cursor()

all_tweets = get_tweets(cursor)
tweets_by_interval = get_tweets_by_intervals(all_tweets)
cleaned_tweets = clean_tweets(tweets_by_interval)
frequencies = get_frequency_table(cleaned_tweets)

sorted_freq = sorted(frequencies.iteritems(), key=operator.itemgetter(1))
output_file = open('frequencies.txt', 'w+')
for word,freq in sorted_freq:
	output_file.write('%s,%s\n' % (word, freq))

