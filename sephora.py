#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:03:22 2018

@author: awais
I received advice from Mike Fusiek and Eli Mani in completeting this assignment 
"""
import pandas as pd
import matplotlib.pyplot as plt

productsFile = pd.read_csv("products.csv")

#Sort the files by the boolean values
dis = sorted(productsFile.groupby("discontinued"))

#A dataframe that only has False values
SortedBools = productsFile[productsFile["discontinued"] == False]

#Indexing inside the list of data Frames and sorting it by price 
FalseVals = dis[0][1]
prices = FalseVals.sort_values("price")
Price = pd.qcut(prices["price"],10)
Mean = SortedBools.groupby(Price)["reviews"].mean()

xVals = [1,2,3,4,5,6,7,8,9,10]

#Plotting phase
plt.scatter(xVals,Mean)
plt.title("Sephora Products")
plt.xlabel("Price")
plt.ylabel("Reviews")
plt.grid()
plt.savefig("Sephora Reviews", dpi=150)
plt.show()

