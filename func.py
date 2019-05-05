
# coding: utf-8

# In[ ]:


import os
mypath = input()
filelist=os.listdir(mypath)


# Mood_Check

# In[2]:


#project.py
#!/usr/bin/env python
import requests
import bs4
from bs4 import BeautifulSoup

content = requests.get('http://ptrckprry.com/course/ssd/data/positive-words.txt').content.decode('utf-8')
resp = requests.get('http://ptrckprry.com/course/ssd/data/positive-words.txt')
soup = bs4.BeautifulSoup(resp.content, 'html.parser')
pos_lib=list(soup.get_text().split('\n'))[35:-1]


# In[157]:


content2 = requests.get('http://ptrckprry.com/course/ssd/data/negative-words.txt').content.decode('ISO-8859-1')
resp2 = requests.get('http://ptrckprry.com/course/ssd/data/negative-words.txt')
soup2 = bs4.BeautifulSoup(resp2.content, 'html.parser')
neg_lib=list(soup2.get_text().split('\n'))[35:-1]


# In[158]:


import re
def mood_test(path):
    pos_count = 0
    neg_count = 0
    with open(path, 'r', encoding='utf8') as txt_file:
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


# In[150]:


def kid_safe(path):
    profanity_count = 0
    with open(path, 'r',encoding='utf8') as txt_file:
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


# Length

# In[144]:



total_length=[]
for i in filelist:
    with open(mypath+'/'+i, 'r',encoding='utf8') as txt_file:
        content = txt_file.read()
        words=re.findall(r'\w+', content)
        length=len(words)
        total_length.append(length)
avglength=sum(total_length)/len(total_length)

def length_test(path):
    with open(path, 'r',encoding='utf8') as txt_file:
        content = txt_file.read()
        words=re.findall(r'\w+', content)
        length=len(words)
        if length==avglength:
            length_score=0.5
        elif length>avglength:
            length_score=0.5+(length-avglength)/avglength*0.25
        else:
            length_score=0.5-(avglength-length)/avglength*0.25
        if length_score>1:
            length_score=1
        if length_score<0:
            length_score=0    
    return length_score


# Complexity

# In[145]:


from collections import Counter
def complexity(path):  
    with open(path, 'r',encoding='utf8') as txt_file:
        content = txt_file.read()
        words=re.findall(r'\w+', content)
        counts = Counter(words)
        unique_word=len(counts.keys())
        times=sorted(counts.values())[-1]
        complex_score=1-times/unique_word
        if complex_score<0:
            complex_score=0
    return complex_score


# LOVE

# In[3]:


content3 = requests.get('https://github.com/silanx/tools-project/blob/master/Romantic.txt').content.decode('ISO-8859-1')
resp3 = requests.get('https://github.com/silanx/tools-project/blob/master/Romantic.txt')
soup3 = bs4.BeautifulSoup(resp3.content, 'html.parser')
love_lib=list(soup3.get_text().split('\n'))


# In[147]:


def love_test(path):
    love_count = 0
    with open(path, 'r',encoding='utf8') as txt_file:
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

