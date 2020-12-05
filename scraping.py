#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 12:12:45 2020

@author: king
"""

import pandas as pd
# Import the Article Module
from newspaper import Article 
  

#Open the file containing the URLs. 
file = open('consolidatedUrls.txt', 'r') 
count = 0

# Initialize a dataframe to which article data will be added. 
corpus = pd.DataFrame(columns = ["Article_ID","Title","Text","Summary","Keywords","Number_of_words"])


# Number of articles required.
n = int(input("Enter number of articles required: "))

# Run over all URLs in the file. 
for line in file:
    count += 1
  
    # Get next line from file 
    url = line
    
    ndtv_article = Article(url, language="en")
    try:
        ndtv_article.download()
    except:
        continue
    ndtv_article.parse()
    ndtv_article.nlp()
    
    article_id = count
    title = ndtv_article.title 
    text = ndtv_article.text
    summary = ndtv_article.summary
    keywords = ndtv_article.keywords
    number = len(text.split(" "))
    
    corpus = corpus.append({"Article_ID":article_id,"Title":title,"Text":text,"Summary":summary,"Keywords":keywords,"Number_of_words":number},ignore_index = True)
    
    if count == n:
        break
file.close() 

  
