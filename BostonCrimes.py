#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 01:21:38 2019

@author: awais
"""

import pandas as pd
import matplotlib.pyplot as plt 
#Read the crime file can update the crimes through link
#https://data.boston.gov/dataset/crime-incident-reports-august-2015-to-date-source-new-system
Data = pd.read_csv("BostonCrime.csv")
Datasubset = Data[0:1000]

#lets visually see the top crimes
#First group by the crimes and store in a value
#.reset_index() puts it back into a dataframe

TopCrimes = Data.groupby("OFFENSE_CODE_GROUP").size().reset_index()

#lets rename the numbers column to make it look better and easier to access
TopCrimes.columns = ["Crimes", "Count"]
#A lot of crimes lets just get the top 10
Top10Crimes = TopCrimes.sort_values(by=["Count"], ascending=False)[5:10]

#Time to look for outliers in the top 10 crimes
#first Convert to a list
Top10CrimesList = Top10Crimes["Crimes"].tolist()

#subset the data for only the top 10 crimes
DataTopCrimes = Data.loc[Data["OFFENSE_CODE_GROUP"].isin(Top10CrimesList)]
#boxplot to look for outliers
DataTopCrimes.boxplot(column="OFFENSE_CODE", by="OFFENSE_CODE_GROUP")


plt.savefig('test.png',dpi=200)

#plt.pie(Top10Crimes["Count"],labels=Top10Crimes["Crimes"],autopct='%.1f%%')