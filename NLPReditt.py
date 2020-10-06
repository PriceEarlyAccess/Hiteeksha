#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:54:04 2020

@author: hiteekshamathur
"""

import praw
from praw.models import MoreComments

import pandas as pd 
from datetime import datetime

import os
os.chdir(r"/Users/hiteekshamathur/Desktop/MFE/UCLA/RA/ThomasRA")
#%%
reddit = praw.Reddit(client_id='i50mJ36xx4Y-Dw', client_secret='8b3CD0iN1D7UEGH5bFr7rOPBBBQ', user_agent='hprofessional')
#%% GAMES

game='combinedarms'

#game='KineticVoid'
#game='thelongdark'
#reddit.redditor(game).id
#%% POSTS

# get 10 hot posts from the  subreddit
hot_posts = reddit.subreddit(game).hot()
#hot_posts = reddit.subreddit(game).hot(limit=10)
for post in hot_posts:
    print(post.title)
    
# get hottest posts from all subreddits
#hot_posts = reddit.subreddit('all').hot(limit=10)
hot_posts = reddit.subreddit('all').hot()
for post in hot_posts:
    print(post.title)

posts = []
game_subreditt = reddit.subreddit(game)


#for post in game_subreditt.hot(limit=50):
for post in game_subreditt.hot():
    #print()
    #score= upvotes
    post.time=datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')
    post.created=(datetime.fromtimestamp(post.created).strftime('%Y-%m-%d %H:%M:%S'))    
    posts.append([post.title, post.score, post.author,post.id, post.subreddit, post.url, post.num_comments, post.selftext,post.time])
posts = pd.DataFrame(posts,columns=['title', 'upvotes', 'author','id', 'subreddit', 'url', 'num_comments', 'text', 'creation_date_time'])
#print(posts)
posts.to_csv('Posts.csv')
# get  subreddit data
game_subreditt = reddit.subreddit(game)

#print(game_subreditt.description)

#%% COMMENTS

comments_array=[]
for i in range(len(posts)):
#Get comments from a specific post
    title=posts.loc[i,'title']
#    submission = reddit.submission(url=posts.loc[i,'url'])
    submission = reddit.submission(id=posts.loc[i,'id'])
    
#    print(i)
    #submission = reddit.submission(url="https://www.reddit.com/r/MapPorn/comments/a3p0uq/an_image_of_gps_tracking_of_multiple_wolves_in/")
    # or 
    #submission = reddit.submission(id="a3p0uq")
    
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
#        print(top_level_comment.body)
        
    submission.comments.replace_more()
    for comment in submission.comments.list():
#        print(comment.body)
        comments_array.append([title,comment.body])
#        print(comments_array)
    comments_df=pd.DataFrame(comments_array,columns=['Post Title','Comments'])
comments_df.to_csv('Comments.csv')

#%% DEVELOPERS/ MODERATORS

mods=[]
for moderator in reddit.subreddit(game).moderator():
    mods.append(moderator.name)

moderators=[]
for i,j in enumerate(mods):
    moderators.append([reddit.redditor(j).name,reddit.redditor(j).id,reddit.redditor(j).comment_karma,\
          reddit.redditor(j).comments,reddit.redditor(j).created_utc,\
          reddit.redditor(j).has_verified_email,reddit.redditor(j).is_mod])
moderators = pd.DataFrame(moderators,columns=['Name','ID','comment_karma','comments','Acc creation',\
                                              'has_verified_email','mods_any_subreddits'])

moderators.to_csv('Moderators.csv')

#%% ROUGH WORK

#import requests
#import spacy 
#from bs4 import BeautifulSoup
#
#
#nlp = spacy.load("en") 
#url = 'https://www.reddit.com/r/thelongdark/?f=flair_name%3A%22Glitch%2FIssue%22'
#r = requests.get(url)
#html = r.text
#soup = BeautifulSoup(html, "html5lib")
#text = soup.get_text()
#gutten_nlp = nlp(text)
##gutten_nlp = nlp(text[:99999])
#
#rep = []
#
#for token in gutten_nlp:
#    rep.append((token))
#    rep.append((token.orth_))
#    rep.append((token.orth))
#
#print(rep)
#
#for token in gutten_nlp:
#    if not token.is_punct | token.is_space:
#        print(token.orth_)
#
#""" Lemmitization """ 
#
#for token in gutten_nlp:
#    lemma = (token.lemma_)
#    print(lemma)
#    
#
#""" Part of Speech """ 
#for token in gutten_nlp:
#    tag_token = (token, token.tag_)
#    print(tag_token)
#
#""" Entity Recognition """
#for token in gutten_nlp.ents:
#    print(token, token.label_, token.label)
#     
#""" Sentence Recognition """
#for token in gutten_nlp.sents:
#    print(token)
#
#
#
#""" Nouns """
#nouns = []
#for token in gutten_nlp:
#    if not token.is_stop | token.is_punct and token.pos_ == "NOUN":
#        nouns.append(token.text)
#
#        
#"""" VERBS """
#verbs = []
#for token in gutten_nlp:
#    if not token.is_stop | token.is_punct and token.pos_ == "VERB":
#        verbs.append(token.text)
#
#from collections import Counter
#
#""" Entity Recognition """
#kind = []
#kind_words=[]
#for entity in gutten_nlp.ents:
#    print(entity)
#    print(entity)
#    kind.append(entity.label_)
#    kind.append(entity)
#kind_count = Counter(kind)
#top_kind = kind_count.most_common(5)
#
#""" Sentence Count """
#sentences = []
#for token in gutten_nlp.sents:
#    sentences.append(token)
#print(len(sentences))    
#
#from spacy import displacy
#fifty = sentences[50]
#displacy.render(fifty, style="dep")
#
#
#
#
#
#
#
#
