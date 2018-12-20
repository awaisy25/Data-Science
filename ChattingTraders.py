#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 15:37:17 2018
Awais and phong created this. We used a couple of online resources to figure out how to 
do the plots.
@author: awais
"""
"""
This project analysis data for a Forex trading system and Communicatiosn trhough messages. 
It is created through pandas data frames. 
It retrives the number of users, discussion.
The different type of messages and posts. 
"""
import pandas as pd
from matplotlib import pyplot as plt
import datetime
#input phase
users = pd.read_csv("traders/users.tsv", sep='\t')
discussions = pd.read_csv("traders/discussions.tsv", sep='\t')
discussions_posts = pd.read_csv("traders/discussion_posts.tsv", sep='\t')
messages = pd.read_csv("traders/messages.tsv", sep='\t')
timeConversion = 60 * 60 * 24 * 1000
#renaming the column ids
us = users.rename(columns = {"id": "users_id"})
mess = messages.rename(columns = {"id": "messages_id"})
dp = discussions_posts.rename(columns = {"id": "dp_id"})
frames = [mess,discussions, dp,us]
DF = pd.concat(frames, axis = 1)
#Part 1 Descriptive Statistics

DatabaseTotal = DF["users_id"].count()
print("Total number of users is:", DatabaseTotal)
TimeSpan = DF["memberSince"].max() - DF["memberSince"].min()

print("Time of Database: ", TimeSpan / timeConversion)
MessageValueCnt = DF["type"].value_counts()
DiscussionsValueCnt = DF["discussionCategory"].value_counts()
plt.figure(0)
plt.title("Message of Each Type")
plt.pie(MessageValueCnt, labels = ["FRIEND_LINK_REQUEST", "DIRECT_MESSAGE"],
        autopct ='%1.1f%%')
plt.figure(1)
plt.title("Dicusissions of each type")
plt.pie(DiscussionsValueCnt, labels = ["QUESTION","POSITION","MARKET_COMMENTARY","TECHNICAL_ANALYSIS",
                                       "POLL","TECHNICAL_INDICATOR", "FEED_ITEM", "NEWSREPORT","ECONOMICEVENT"],autopct = '%1.1f%%')
DiscussionPostTotal = DF["dp_id"].count()
print("Total number of discussion posts:", DiscussionPostTotal)
#Part 2 Activity Range

plt.figure(2)
Mes = pd.merge(users,messages,left_on = "id", right_on = "sender_id")
ProperOrder = Mes.groupby(["id_x"])
ActivityRange = ProperOrder["sendDate"].max() - ProperOrder["sendDate"].min()
Converted = ActivityRange / timeConversion 
plt.title("Activity Range")
plt.hist(Converted)
plt.yscale("log")
#Part 3 Message Acitivity Delay

plt.figure(3)
Min = ProperOrder.min()
Friend = Min[Min['type'] != "DIRECT_MESSAGE"]
Direct = Min[Min['type'] != "FRIEND_LINK_REQUEST"]
FriendDelay = (Friend["sendDate"] - Friend["memberSince"]) / timeConversion
DirectDelay = (Direct["sendDate"] - Direct["memberSince"]) / timeConversion
plt.title("Message Acitivity Delay")
#The Blue is friend link request Orange is Direct message couldn't get the labels to work
plt.xlabel("Blue is Friend Link Request, Orange is Direct Message")
plt.hist(FriendDelay, label = ["FRIEND_LINK_REQUEST"])
plt.hist(DirectDelay, label = ["DIRECT_MESSAGE"])
plt.yscale("log")
#Part 4 distribution of discussion categories by the number of posts

plt.figure(4)
DisFram = pd.merge(discussions_posts, discussions, left_on="discussion_id",right_on ="id")
DiscussionCount = DisFram["discussionCategory"].value_counts()
plt.title("Discussions Posts")
DisLabels = ["QUESTION", "POST", "MARKET_COMMENTARY","TECHNICAL_ANALYSIS","POSITION","TECHNICAL_INDICATOR",
             "NEWSREPORT","FEED_ITEM","ECONOMICEVENT"]
plt.pie(DiscussionCount, labels = DisLabels, autopct ='%1.1f%%')
#Part 5 Post Acitivity Delay 

plt.figure(5)
ActivFram = pd.merge(discussions_posts,users,left_on='creator_id', right_on='id')
ActivOrder = ActivFram.groupby("creator_id")
ActMin = ActivOrder.min()
DelayTime = (ActMin["createDate"] - ActMin["memberSince"]) / timeConversion
plt.title("Post Activity Delay")
plt.hist(DelayTime)
plt.yscale("log")
#Part 6 box plot wiskers for each category 

plt.figure(6)
plt.subplot(1,4,1)
plt.title("Post Activity")
plt.boxplot(DelayTime)

plt.subplot(1,4,2)
plt.title("Activity Range")
plt.boxplot(Converted)

plt.subplot(1,4,3)
plt.title("Direct Message")
plt.boxplot(DirectDelay)

plt.subplot(1,4,4)
plt.title("Friend LRequest")
plt.boxplot(FriendDelay)
plt.tight_layout()
plt.show()
