# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 13:37:11 2022

@author: Vineet
"""
#!pip install regex
#!pip install collection
#!pip install wordcloud
#!pip install emoji

import regex
import pandas as pd
import numpy as np
import emoji
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import os

os.chdir('C:\\Users\\Vineet\\Downloads')

def date_time(s):
    pattern = '^([0-9]+)(\/)([0-9]+)(\/)([0-9]+), ([0-9]+):([0-9]+)[ ]?(AM|PM|am|pm)? -'
    result  = regex.match(pattern,s)
    if result:
        return True
    return False

def find_author(s):
    s = s.split(':')
    if len(s)==2:
        return True
    else:
        return False
    
def getDatapoint(line):
    splitline = line.split('-')
    dateTime = splitline[0]
    date,time = dateTime.split(',')
    message = ' '.join(splitline[1:])
    if find_author(message):
        splitmessage = message.split(":")
        author = splitmessage[0]
        message = ' '.join(splitmessage[1:])
    else:
        author = None
    return date,time,author,message

#converting data into DataFrame
data = []
conversation = 'WHATS APP CHATS.txt'
with open(conversation,encoding = 'utf-8') as fp:
    fp.readline()
    messageBuffer = []
    date,time,author =  None,None,None
    while True:
        line = fp.readline()
        if not line:
            break
        line = line.strip()
        if date_time(line):
            if len(messageBuffer) > 0:
                data.append([date,time,author,' '.join(messageBuffer)])
            messageBuffer.clear()
            date,time,authour,message = getDatapoint(line)
            messageBuffer.append(message)
        else:
            messageBuffer.append(line)

#Using of DataFrame
df = pd.DataFrame(data,columns=['Date','Time','Author','Message'])
df['Date'] = pd.to_datetime(df['Date'])
print(df.tail(20))
print(df.info())
print(df.Author.unique())

#Total number of messages
total_message = df.shape[0]
print(total_message)

#media present in the chat
media_message = df[df['Message']=='<Media omitted>'].shape[0]
print(media_message)

#Urls present in the chat
URLPATTERN = r'(http?://\S+)'
df['urlcount'] = df.Message.apply(lambda x: regex.findall(URLPATTERN,x)).str.len()
links = np.sum(df.urlcount)

print('Chats Between US')
print('Total Message',total_message)
print('Number of Media Shared',media_message)
print('Number of Links Shared',links)


