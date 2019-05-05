
# coding: utf-8

# Mood_Check

# In[3]:


#project.py
#!/usr/bin/env python

import requests
import bs4

content = requests.get('http://ptrckprry.com/course/ssd/data/positive-words.txt').content.decode('utf-8')
resp = requests.get('http://ptrckprry.com/course/ssd/data/positive-words.txt')
soup = bs4.BeautifulSoup(resp.content, 'html.parser')


# In[4]:


pos_lib=list(soup.get_text().split('\n'))[35:-1]


# In[5]:


content2 = requests.get('http://ptrckprry.com/course/ssd/data/negative-words.txt').content.decode('ISO-8859-1')
resp2 = requests.get('http://ptrckprry.com/course/ssd/data/negative-words.txt')
soup2 = bs4.BeautifulSoup(resp2.content, 'html.parser')


# In[6]:


neg_lib=list(soup2.get_text().split('\n'))[35:-1]


# In[141]:


import os
import re
from bs4 import BeautifulSoup


def mood_test(i):
    pos_count = 0
    neg_count = 0
    if i.endswith(".txt"):
        with open(Path + i, 'r', encoding='utf8') as txt_file:
            content = txt_file.read()
            words = re.findall(r'\w+', content)
            for word in words:
                if word in pos_lib:
                    pos_count += 1
                elif word in neg_lib:
                    neg_count += 1
                else:
                    pos_count = 0
                    neg_count = 0
            pos_percent = pos_count/len(words)
            neg_percent = neg_count/len(words)
            if pos_percent >= neg_percent:
                mood = 0.5+30*pos_percent
            else:
                mood = 0.5-30*neg_percent
            if mood < 0:
                mood = 0.5
            if mood > 1:
                mood = 1
    return mood
    


# Kid_Safe

# In[8]:


content3 = requests.get('http://www.cs.cmu.edu/~biglou/resources/bad-words.txt').content.decode('utf-8')
resp3 = requests.get('http://www.cs.cmu.edu/~biglou/resources/bad-words.txt')
soup3 = bs4.BeautifulSoup(resp3.content, 'html.parser')


# In[9]:


profanity_lib=list(soup.get_text().split('\n'))[35:-1]


# In[25]:


def kid_safe(i):
    profanity_count = 0
    if i.endswith(".txt"):
        with open(Path + i, 'r',encoding='utf8') as txt_file:
            content = txt_file.read()
            words=re.findall(r'\w+', content)
            for word in words:
                if word in profanity_lib:
                    profanity_count += 1
            profanity_percent= profanity_count/len(words)
            kid_safe_score = 1-20*profanity_percent
            if (kid_safe_score < 0):
                kid_safe_score = 0
    return kid_safe_score
kid_safe_scores=[kid_safe(i) for i in filelist]


# Length

# In[26]:


total_length=[]
for i in filelist:
    if i.endswith(".txt"):
        with open(Path + i, 'r',encoding='utf8') as txt_file:
            content = txt_file.read()
            words=re.findall(r'\w+', content)
            length=len(words)
            total=total_length.append(length)
avg_length=sum(total_length)/len(total_length)

def length_test(i):
    if i.endswith(".txt"):
        with open(Path + i, 'r',encoding='utf8') as txt_file:
            content = txt_file.read()
            words=re.findall(r'\w+', content)
            length=len(words)
            if length==avg_length:
                length_score=0.5
            elif length>avg_length:
                length_score=0.5+(length-avg_length)/avg_length*0.25
            else:
                length_score=0.5-(avg_length-length)/avg_length*0.25
            if length_score>1:
                length_score=1
            if length_score<0:
                length_score=0    
    return length_score

length_scores=[length_test(i) for i in filelist]


# Complexity

# In[31]:


from collections import Counter
def complexity(i):  
    if i.endswith(".txt"):
        with open(Path + i, 'r',encoding='utf8') as txt_file:
            content = txt_file.read()
            words=re.findall(r'\w+', content)
            counts = Counter(words)
            unique_word=len(counts.keys())
            times=sorted(counts.values())[-1]
            complex_score=1-times/unique_word
            if complex_score<0:
                complex_score=0
    return complex_score

complexity_scores=[complexity(i) for i in filelist]


# LOVE

# In[32]:


Path = "/Users/iamsu/Desktop/project/"
with open(Path + 'Romantic.txt', 'r',encoding='utf8') as fp:
    content = fp.readlines()
    content = [x.strip() for x in content] 
    love_lib = set(content)


# In[33]:


def love_test(i):
    love_count = 0
    if i.endswith(".txt"):
        with open(Path + i, 'r',encoding='utf8') as txt_file:
            content = txt_file.read()
            words=re.findall(r'\w+', content)
            for word in words:
                if word in love_lib:
                    love_count += 1
            love_percent= love_count/len(words)
            love_song_score = 10*love_percent
            if love_song_score>1:
                love_song_score =1
    return love_song_score

love_scores=[love_test(i) for i in filelist]


# Return a dictionary

# In[ ]:


import re
def value(i):
    content = i.replace('.txt', '').split('~')
    id_info = content[0]
    artist_info = content[1]
    title_info = content[2]
    value = {'ID': id_info ,
             'artist': artist_info, 
             'title': title_info,
             'kid_safe': kid_safe(i), 
             'love': love_test(i), 
             'mood': mood_test(i), 
             'length': length_test(i), 
             'complexity': complexity(i)}
    return value

Path = "/Users/iamsu/Desktop/project/Lyrics.unzipped/"
filelist = os.listdir(Path)
all_value = [value(i) for i in filelist]  
output={'characterizations':all_value}


# Unit-testing
# 

# In[91]:


import unittest
class TestRange(unittest.TestCase):
    def test_mood(self): 
        for i in filelist:
            if i.endswith(".txt"):
                self.assertTrue(mood_test(i) <=1 and mood_test(i)>=0)
    def test_kid(self):
        for i in filelist:
            if i.endswith(".txt"):
                self.assertTrue(kid_safe(i) <=1 and kid_safe(i)>=0)
    def test_length(self):
        for i in filelist:
            if i.endswith(".txt"):
                self.assertTrue(length_test(i) <=1 and length_test(i)>=0)
    def test_complexity(self):
        for i in filelist:
            if i.endswith(".txt"):
                self.assertTrue(complexity(i) <=1 and complexity(i)>=0)
    def test_love(self):
        for i in filelist:
            if i.endswith(".txt"):
                self.assertTrue(love_test(i) <=1 and love_test(i)>=0)               

suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestRange)
# Run each test in suite
unittest.TextTestRunner().run(suite)

