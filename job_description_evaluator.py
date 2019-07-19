# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:37:22 2016

"""

from nltk.corpus import stopwords
from collections import Counter
import string
# stopwords has to be downloaded to system once
#import nltk
#nltk.download('stopwords')
#list of words to remove
words_unwanted = set(stopwords.words('english'))
punctuation = string.punctuation#['.', ',', '?', '-']
#list of knowns and initiation of used lists for search function
cad_known = ['nx', 'solidworks', 'autocad','inventor']
cad_used = []
programming_known = ['python', 'vba','javascript']
programming_used = []
software_known = ['ms office', 'microsoft office', 'matlab']
software_used = []
skills_known = ['problem solving','prototyping','3d modeling', 'solid modeling', 'fea', 'finite element analysis', 'fem', 'finite element method', 'stress analysis', 'fabrication', 'machining', 'cad', 'communication', 'organization']
skills_used = []
education_known = ['bs', 'bachelors', "bachelor's"]
education_used = []
#job posting
words = """
 
"""
#normalize text to lowercase
words = words.lower()
#remove punctuation
for x in words:
	for y in punctuation:
		if x == y:
			words = words.replace(x,'')
#search for relevant keywords
def search(known,used):
	for y in known:
		if y in words:
			used.append(y)
	return used
# find profile matches
search(cad_known,cad_used)
search(programming_known,programming_used)
search(software_known,software_used)
search(skills_known,skills_used)
search(education_known,education_used)
#creates list of words from string
wordlist = words.split()
#remove unwanted words
for x in wordlist:
	for y in words_unwanted:
		if x == y:
			wordlist.remove(x)
#determine which words are used the most
frequency = Counter(wordlist).most_common()
# print results
print(frequency[:10])
print('cad:',cad_used)
print('programming:',programming_used)
print('software:',software_used)
print('skills:',skills_used)
print('education:',education_used)
