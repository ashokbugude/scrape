# Python3 code to print top 5 most occuring words of a web page

import requests 
from bs4 import BeautifulSoup 
import operator 
from collections import Counter 

# take url as parameter to crawl
def start(url): 

	# list to store the content fetched
	wordlist = [] 
	source_code = requests.get(url).text 

	# ping url for data 
	soup = BeautifulSoup(source_code, 'html.parser') 

	# loop all div tags for content
	for each_text in soup.findAll('div', {'class':'nav-sidebar'}): 
		content = each_text.text


		# split senctence to words and convert to lower case
		words = content.lower().split() 
		
		for each_word in words: 
			wordlist.append(each_word) 
		clean_wordlist(wordlist) 

# remove any unwanted symbols in words
def clean_wordlist(wordlist): 

	clean_list =[] 
	for word in wordlist: 
		symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
		
		for i in range (0, len(symbols)): 
			word = word.replace(symbols[i], '') 
			
		if len(word) > 0: 
			clean_list.append(word) 
	create_dictionary(clean_list) 

# Creates a dictionary conatining each word's 
# count and top_20 ocuuring words 
def create_dictionary(clean_list): 
	word_count = {} 
	
	for word in clean_list: 
		if word in word_count: 
			word_count[word] += 1
		else: 
			word_count[word] = 1

	c = Counter(word_count) 
	
	# returns the most occuring elements 
	top = c.most_common(5)

	print("Word\t\tCount")
	for i in range(len(top)):
		 print(str(top[i][0])+'\t\t'+str(top[i][1]))
	#print(top) 

# Start executing code
if __name__ == '__main__': 
        start("https://hiverhq.com")

