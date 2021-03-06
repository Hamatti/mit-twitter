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
	# Database was created with user and tweet columns as opposites, therefore we get user column instead of tweet
	query_results = cursor.execute('SELECT user FROM tweets WHERE user NOT LIKE "%free%" AND user NOT LIKE "%pengikut%"').fetchall()
	for res in query_results:
		if 'chair' in res[0]:
			continue
		tweets.append(clean_words(res[0]))
	return tweets

def clean_words(words):
	return words.replace('\n', '').replace('.', '').replace(':', '').replace(',', '').replace('"', '').replace('?','').replace('!', '').replace('(', '').replace(')', '').replace("'", "").strip()

def get_tweets_by_intervals(tweets, interval):
	tweets_by_interval = dict()
	start_point = 0
	for iteration in range(1,11):
		tweets_by_interval[iteration] = set(all_tweets[start_point:interval*iteration])
		start_point += interval
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

def get_interval_frequency_table(raw_tweets):
	freqs = dict()
	for interval, tweets in raw_tweets.iteritems():
		if interval not in freqs.keys():
			freqs[interval] = defaultdict(int)
		for tweet in tweets:
			for word in tweet:
				freqs[interval][word] += 1

	return freqs



def write_all_words_to_file(fname):
	textfile = open(fname, 'w+')
	for interval, tweet in cleaned_tweets.iteritems():
		for ls in tweet:
			for word in ls:
				textfile.write("%s " % word)
	textfile.close()

def write_freq_to_csv(sorted_freq, fname):
	output_file = open(fname, 'w+')
	for word,freq in sorted_freq:
		output_file.write('%s,%s\n' % (word, freq))
	output_file.close()

def write_hourly_freq_to_csv(frequencies,fname):
	i = 1
	for interval in frequencies.keys():
		output_file = open('%s%s.txt' % (fname, i), 'w+')
		current_dict = frequencies[interval]
		for word, freq in current_dict.iteritems():
			output_file.write("%s,%s\n" % (word, freq))
		i += 1
		output_file.close()

DATABASE = 'mit.db'
STOPWORDS = get_stopwords()
connection = sql.connect(DATABASE)
cursor = connection.cursor()

all_tweets = get_tweets(cursor)
tweets_by_interval = get_tweets_by_intervals(all_tweets, 3600)
cleaned_tweets = clean_tweets(tweets_by_interval)
frequencies = get_frequency_table(cleaned_tweets)
sorted_freq = sorted(frequencies.iteritems(), key=operator.itemgetter(1))

interval_freq = get_interval_frequency_table(cleaned_tweets)

write_hourly_freq_to_csv(interval_freq, 'hourly_frequencies')
#write_freq_to_csv(sorted_freq, 'frequencies.txt')
