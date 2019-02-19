#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:14:08 2018

@author: awais Created this program by myself used stack overflow to understand how to get the mean
also used stack overflow on how to change the column types. 
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize


CMPSC = pd.read_csv("cs1-scores.txt", sep=r"\s+")

#replacing the # with 0 so i could normalize it 
CMPSC["Final"] = CMPSC["Final"].replace("#","0")
normal = normalize(CMPSC,norm="max")

#Converting it to a dataframe
newCS = pd.DataFrame(normal, columns=["Final","Q1","Q2","A1","A2"])

NoFinal = newCS.drop("Final",axis=1)
newCS["Assignments"] = NoFinal.mean(axis=1)

#Creating a dataframe with only final and assignment to cluster it
NewDF = pd.concat([newCS["Final"],newCS["Assignments"]],axis=1,keys=["Final","Assignments"])

clus = KMeans(n_clusters=7).fit(NewDF)

centroids = clus.cluster_centers_

#adding the mean column asignment to the orignal dataframe
CMPSC["Assignments"] = CMPSC.mean(axis=1)
#creating a datafram with the original values 
finalDF = pd.concat([CMPSC["Final"], CMPSC["Assignments"]],axis=1,keys=["Final","Assignments"])

#converting the dataframe to float so i can divide it by 100
Df= finalDF.astype(float)
FinalDF = Df / 100


plt.xlabel("Final Exam score")
plt.ylabel("Mean assignment score")

plt.scatter(FinalDF["Final"],FinalDF["Assignments"])
plt.scatter(centroids[:, 0],centroids[:, 1], marker= "x")
plt.savefig("Cluster.png",dpi=200)

