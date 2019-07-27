#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.getcwd()"C:\Users\bcowl\Downloads\_MG_7831.JPG"


# In[2]:


os.chdir(r"C:\Users\bcowl\Desktop\Data")
readimage("Image1")


# In[1]:


print("Hello")


# In[3]:


os.getcwd()


# In[4]:


import pandas as pd


# In[5]:


# test

testDict = {}
testList = [1, 2, 3]

testDict['fluff'] = testList

print(testDict)


# In[1]:


# add nine of same elements to list
listRandomm = [1, 13, 41, 75, 81, 53, 69, 85, 87, 37, 3, 5, 7, 9,
               11, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 39, 43, 45,
               47, 49, 51, 55, 57, 59, 61, 63, 65, 67, 71, 73, 77, 79, 83,
               89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115]
listRandom = []

for i in listRandomm:
    for a in range(1, 9):
        listRandom.append(i)
    
    

cancerYearList = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
cancerYearList = cancerYearList * 58
print(listRandomm)


# In[7]:


countyRatesData = pd.read_csv('Rates County Edited2.csv')
countyRatesData
countyRatesList = []
total = len(countyRatesData) + 1
for i in range(0, len(countyRatesData)):
    countyRatesList.append(countyRatesData['Age-Adjusted Rate/Trend'].iloc[i])
    
print(len(countyRatesList))


# In[8]:


cancer = pd.read_csv('cancer3.0.csv')
cancer


# In[9]:


cancer2 = pd.read_csv('cancer3.02col.csv')
cancer2


# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

corr = cancer2.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(cancer2.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(cancer2.columns)
ax.set_yticklabels(cancer2.columns)
plt.show()


# In[27]:


#changes: added the elif != 0, also added if not in (that messed everything up)

# making a new dataset 
# go through every row of the data set, for each row, record county, if in database, add amounts of primary sector
#then add CO2...... to the current totals, then add to total industry
countyDict = {}
countyList = []
yearList = []
sectorList = []
CO2List = []
CH4List = []
N2OList = []
VOCList = []
NOxList = []
SOxList = []
PM10List = []
PM25List = []
CancerRateList = []
countyListComplete = []
totalIndustry = []
cogenerationList = []
otherCombustionList = []
electricityList = []
cementList = []
hydrogenList = []
refineryList = []
oilGasList = []
productionList = []



for i in listRandomm:
    year1 = 0
    tally1 = 0
    tally2 = 0
    tally3 = 0
    tally4 = 0
    tally5 = 0
    tally6 = 0
    tally7 = 0
    tally8 = 0
    industriesList = []
    industriesList2 = []
    industriesList3 = []
    industriesList4 = []
    industriesList5 = []
    industriesList6 = []
    industriesList7 = []
    industriesList8 = []
    
    for a in range(0, 3856):
        if cancer['Year'].iloc[a] == 2008:
            year1 += 1
            if cancer['County'].iloc[a] == i:
            
                if tally1 == 0:
                    
                    CO2List.append(cancer['CO2'].iloc[a])
                    CH4List.append(cancer['CH4'].iloc[a])
                    N2OList.append(cancer['N2O'].iloc[a])
                    VOCList.append(cancer['VOC'].iloc[a])
                    NOxList.append(cancer['NOx'].iloc[a])
                    SOxList.append(cancer['SOx'].iloc[a])
                    PM10List.append(cancer['PM10'].iloc[a])
                    PM25List.append(cancer['PM2.5'].iloc[a])
                    # totalIndustry.append(1)
                    tally1 = 1
                    if cancer['Primary Sector'].iloc[a] == 1:
                        if 1 not in industriesList:
                            cogenerationList.append(1)
                            industriesList.append(1)
                        else:
                            cogenerationList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[a] == 2:
                        if 2 not in industriesList:
                            otherCombustionList.append(2)
                            industriesList.append(2)
                        else:
                            otherCombustionList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[a] == 3:
                        if 3 not in industriesList:
                            electricityList.append(3)
                            industriesList.append(3)
                        else:
                            electricityList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[a] == 4:
                        if 4 not in industriesList:
                            cementList.append(4)
                            industriesList.append(4)
                        else:
                            cementList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[a] == 5:
                        if 5 not in industriesList:
                            hydrogenList.append(5)
                            industriesList.append(5)
                        else:
                            hydrogenList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[a] == 6:
                        if 6 not in industriesList:
                            refineryList.append(6)
                            industriesList.append(6)
                        else:
                            refineryList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[a] == 7:
                        if 7 not in industriesList:
                            oilGasList.append(7)
                            industriesList.append(7)
                        else:
                            oilGasList[-1:] += 1
                
                elif tally1 != 0:
                    
                    CO2List[-1:] += cancer['CO2'].iloc[a]
                    CH4List[-1:] += cancer['CH4'].iloc[a]
                    N2OList[-1:] += cancer['N2O'].iloc[a]
                    VOCList[-1:] += cancer['VOC'].iloc[a]
                    NOxList[-1:] += cancer['NOx'].iloc[a]
                    SOxList[-1:] += cancer['SOx'].iloc[a]
                    PM10List[-1:] += cancer['PM10'].iloc[a]
                    PM25List[-1:] += cancer['PM2.5'].iloc[a]
                    
                    if cancer['Primary Sector'].iloc[a] == 1:
                        if 1 not in industriesList:
                            cogenerationList.append(1)
                            industriesList.append(1)
                        else:
                            cogenerationList[-1:] += cancer['Primary Sector'].iloc[a]
                    elif cancer['Primary Sector'].iloc[a] == 2:
                        if 2 not in industriesList:
                            otherCombustionList.append(2)
                            industriesList.append(2)
                        else:
                            otherCombustionList[-1:] += cancer['Primary Sector'].iloc[a]
                    elif cancer['Primary Sector'].iloc[a] == 3:
                        if 3 not in industriesList:
                            electricityList.append(3)
                            industriesList.append(3)
                        else:
                            electricityList[-1:] += cancer['Primary Sector'].iloc[a]
                    elif cancer['Primary Sector'].iloc[a] == 4:
                        if 4 not in industriesList:
                            cementList.append(4)
                            industriesList.append(4)
                        else:
                            cementList[-1:] += cancer['Primary Sector'].iloc[a]
                    elif cancer['Primary Sector'].iloc[a] == 5:
                        if 5 not in industriesList:
                            hydrogenList.append(5)
                            industriesList.append(5)
                        else:
                            hydrogenList[-1:] += cancer['Primary Sector'].iloc[a]
                    elif cancer['Primary Sector'].iloc[a] == 6:
                        if 6 not in industriesList:
                            refineryList.append(6)
                            industriesList.append(6)
                        else:
                            refineryList[-1:] += cancer['Primary Sector'].iloc[a]
                    elif cancer['Primary Sector'].iloc[a] == 7:
                        if 7 not in industriesList:
                            oilGasList.append(7)
                            industriesList.append(7)
                        else:
                            oilGasList[-1:] += cancer['Primary Sector'].iloc[a]
        if a == 3855:
            
            if 4 not in industriesList:
                cementList.append(0)
            if 5 not in industriesList:
                hydrogenList.append(0)
            if 6 not in industriesList:
                refineryList.append(0)
            if 7 not in industriesList:
                oilGasList.append(0)
                
            if 1 not in industriesList:
                cogenerationList.append(0)
            if 2 not in industriesList:
                otherCombustionList.append(0)
            if 3 not in industriesList:
                electricityList.append(0)
                
            if tally1 == 0:
                CO2List.append(0)
                CH4List.append(0)
                N2OList.append(0)
                VOCList.append(0)
                NOxList.append(0)
                SOxList.append(0)
                PM10List.append(0)
                PM25List.append(0)
                
                    # totalIndustry[-1:] += 1
                    
                    
    for x in range(0, 3856):
        if cancer['Year'].iloc[x] == 2009:
            if cancer['County'].iloc[x] == i:
                
                if tally2 == 0:
                    CO2List.append(cancer['CO2'].iloc[x])
                    CH4List.append(cancer['CH4'].iloc[x])
                    N2OList.append(cancer['N2O'].iloc[x])
                    VOCList.append(cancer['VOC'].iloc[x])
                    NOxList.append(cancer['NOx'].iloc[x])
                    SOxList.append(cancer['SOx'].iloc[x])
                    PM10List.append(cancer['PM10'].iloc[x])
                    PM25List.append(cancer['PM2.5'].iloc[x])
                    # totalIndustry.append(1)
                    
                    if cancer['Primary Sector'].iloc[x] == 1:
                        if 1 not in industriesList2:
                            cogenerationList.append(1)
                            industriesList2.append(1)
                        else:
                            cogenerationList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[x] == 2:
                        if 2 not in industriesList2:
                            otherCombustionList.append(2)
                            industriesList2.append(2)
                        else:
                            otherCombustionList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[x] == 3:
                        if 3 not in industriesList2:
                            electricityList.append(3)
                            industriesList2.append(3)
                        else:
                            electricityList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[x] == 4:
                        if 4 not in industriesList2:
                            cementList.append(4)
                            industriesList2.append(4)
                        else:
                            cementList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[x] == 5:
                        if 5 not in industriesList2:
                            hydrogenList.append(5)
                            industriesList2.append(5)
                        else:
                            hydrogenList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[x] == 6:
                        if 6 not in industriesList2:
                            refineryList.append(6)
                            industriesList2.append(6)
                        else:
                            refineryList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[x] == 7:
                        if 7 not in industriesList2:
                            oilGasList.append(7)
                            industriesList2.append(7)
                        else:
                            oilGasList[-1:] += 1
                    
                    tally2 = 1
                
                elif tally2 != 0:
                
                    CO2List[-1:] += cancer['CO2'].iloc[x]
                    CH4List[-1:] += cancer['CH4'].iloc[x]
                    N2OList[-1:] += cancer['N2O'].iloc[x]
                    VOCList[-1:] += cancer['VOC'].iloc[x]
                    NOxList[-1:] += cancer['NOx'].iloc[x]
                    SOxList[-1:] += cancer['SOx'].iloc[x]
                    PM10List[-1:] += cancer['PM10'].iloc[x]
                    PM25List[-1:] += cancer['PM2.5'].iloc[x]
                    
                    if cancer['Primary Sector'].iloc[x] == 1:
                        if 1 not in industriesList2:
                            cogenerationList.append(1)
                            industriesList2.append(1)
                        else:
                            cogenerationList[-1:] += cancer['Primary Sector'].iloc[x]
                    elif cancer['Primary Sector'].iloc[x] == 2:
                        if 2 not in industriesList2:
                            otherCombustionList.append(2)
                            industriesList2.append(2)
                        else:
                            otherCombustionList[-1:] += cancer['Primary Sector'].iloc[x]
                    elif cancer['Primary Sector'].iloc[x] == 3:
                        if 3 not in industriesList2:
                            electricityList.append(3)
                            industriesList2.append(3)
                        else:
                            electricityList[-1:] += cancer['Primary Sector'].iloc[x]
                    elif cancer['Primary Sector'].iloc[x] == 4:
                        if 4 not in industriesList2:
                            cementList.append(4)
                            industriesList2.append(4)
                        else:
                            cementList[-1:] += cancer['Primary Sector'].iloc[x]
                    elif cancer['Primary Sector'].iloc[x] == 5:
                        if 5 not in industriesList2:
                            hydrogenList.append(5)
                            industriesList2.append(5)
                        else:
                            hydrogenList[-1:] += cancer['Primary Sector'].iloc[x]
                    elif cancer['Primary Sector'].iloc[x] == 6:
                        if 6 not in industriesList2:
                            refineryList.append(6)
                            industriesList2.append(6)
                        else:
                            refineryList[-1:] += cancer['Primary Sector'].iloc[x]
                    elif cancer['Primary Sector'].iloc[x] == 7:
                        if 7 not in industriesList2:
                            oilGasList.append(7)
                            industriesList2.append(7)
                        else:
                            oilGasList[-1:] += cancer['Primary Sector'].iloc[x]
        if x == 3855:
            if 4 not in industriesList2:
                cementList.append(0)
            if 5 not in industriesList2:
                hydrogenList.append(0)
            if 6 not in industriesList2:
                refineryList.append(0)
            if 7 not in industriesList2:
                oilGasList.append(0)
                
            if 1 not in industriesList2:
                cogenerationList.append(0)
            if 2 not in industriesList2:
                otherCombustionList.append(0)
            if 3 not in industriesList2:
                electricityList.append(0)
                
            if tally2 == 0:
                CO2List.append(0)
                CH4List.append(0)
                N2OList.append(0)
                VOCList.append(0)
                NOxList.append(0)
                SOxList.append(0)
                PM10List.append(0)
                PM25List.append(0)
                    
                    # totalIndustry[-1:] += 1
                    
                    
    for y in range(0, 3856):
        if cancer['Year'].iloc[y] == 2010:
            if cancer['County'].iloc[y] == i:
                if tally3 == 0:
                    CO2List.append(cancer['CO2'].iloc[y])
                    CH4List.append(cancer['CH4'].iloc[y])
                    N2OList.append(cancer['N2O'].iloc[y])
                    VOCList.append(cancer['VOC'].iloc[y])
                    NOxList.append(cancer['NOx'].iloc[y])
                    SOxList.append(cancer['SOx'].iloc[y])
                    PM10List.append(cancer['PM10'].iloc[y])
                    PM25List.append(cancer['PM2.5'].iloc[y])
                    # totalIndustry.append(1)
                    
                    if cancer['Primary Sector'].iloc[y] == 1:
                        if 1 not in industriesList3:
                            cogenerationList.append(1)
                            industriesList3.append(1)
                        else:
                            cogenerationList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[y] == 2:
                        if 2 not in industriesList3:
                            otherCombustionList.append(2)
                            industriesList3.append(2)
                        else:
                            otherCombustionList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[y] == 3:
                        if 3 not in industriesList3:
                            electricityList.append(3)
                            industriesList3.append(3)
                        else:
                            electricityList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[y] == 4:
                        if 4 not in industriesList3:
                            cementList.append(4)
                            industriesList3.append(4)
                        else:
                            cementList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[y] == 5:
                        if 5 not in industriesList3:
                            hydrogenList.append(5)
                            industriesList3.append(5)
                        else:
                            hydrogenList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[y] == 6:
                        if 6 not in industriesList3:
                            refineryList.append(6)
                            industriesList3.append(6)
                        else:
                            refineryList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[y] == 7:
                        if 7 not in industriesList3:
                            oilGasList.append(7)
                            industriesList3.append(7)
                        else:
                            oilGasList[-1:] += 1
                    
                    tally3 = 1
                
                elif tally3 != 0:
                    CO2List[-1:] += cancer['CO2'].iloc[y]
                    CH4List[-1:] += cancer['CH4'].iloc[y]
                    N2OList[-1:] += cancer['N2O'].iloc[y]
                    VOCList[-1:] += cancer['VOC'].iloc[y]
                    NOxList[-1:] += cancer['NOx'].iloc[y]
                    SOxList[-1:] += cancer['SOx'].iloc[y]
                    PM10List[-1:] += cancer['PM10'].iloc[y]
                    PM25List[-1:] += cancer['PM2.5'].iloc[y]
                    
                    if cancer['Primary Sector'].iloc[y] == 1:
                        if 1 not in industriesList3:
                            cogenerationList.append(1)
                            industriesList3.append(1)
                        else:
                            cogenerationList[-1:] += cancer['Primary Sector'].iloc[y]
                    elif cancer['Primary Sector'].iloc[y] == 2:
                        if 2 not in industriesList3:
                            otherCombustionList.append(2)
                            industriesList3.append(2)
                        else:
                            otherCombustionList[-1:] += cancer['Primary Sector'].iloc[y]
                    elif cancer['Primary Sector'].iloc[y] == 3:
                        if 3 not in industriesList3:
                            electricityList.append(3)
                            industriesList3.append(3)
                        else:
                            electricityList[-1:] += cancer['Primary Sector'].iloc[y]
                    elif cancer['Primary Sector'].iloc[y] == 4:
                        if 4 not in industriesList3:
                            cementList.append(4)
                            industriesList3.append(4)
                        else:
                            cementList[-1:] += cancer['Primary Sector'].iloc[y]
                    elif cancer['Primary Sector'].iloc[y] == 5:
                        if 5 not in industriesList3:
                            hydrogenList.append(5)
                            industriesList3.append(5)
                        else:
                            hydrogenList[-1:] += cancer['Primary Sector'].iloc[y]
                    elif cancer['Primary Sector'].iloc[y] == 6:
                        if 6 not in industriesList3:
                            refineryList.append(6)
                            industriesList3.append(6)
                        else:
                            refineryList[-1:] += cancer['Primary Sector'].iloc[y]
                    elif cancer['Primary Sector'].iloc[y] == 7:
                        if 7 not in industriesList3:
                            oilGasList.append(7)
                            industriesList3.append(7)
                        else:
                            oilGasList[-1:] += cancer['Primary Sector'].iloc[y]
        if y == 3855:
            if 4 not in industriesList3:
                cementList.append(0)
            if 5 not in industriesList3:
                hydrogenList.append(0)
            if 6 not in industriesList3:
                refineryList.append(0)
            if 7 not in industriesList3:
                oilGasList.append(0)
                
            if 1 not in industriesList3:
                cogenerationList.append(0)
            if 2 not in industriesList3:
                otherCombustionList.append(0)
            if 3 not in industriesList3:
                electricityList.append(0)
            
            if tally3 == 0:
                CO2List.append(0)
                CH4List.append(0)
                N2OList.append(0)
                VOCList.append(0)
                NOxList.append(0)
                SOxList.append(0)
                PM10List.append(0)
                PM25List.append(0)
                    
                    # totalIndustry[-1:] += 1
                    
                    
                    
    for p in range(0, 3856):
        if cancer['Year'].iloc[p] == 2011:
            if cancer['County'].iloc[p] == i:
                if tally4 == 0:
                    CO2List.append(cancer['CO2'].iloc[p])
                    CH4List.append(cancer['CH4'].iloc[p])
                    N2OList.append(cancer['N2O'].iloc[p])
                    VOCList.append(cancer['VOC'].iloc[p])
                    NOxList.append(cancer['NOx'].iloc[p])
                    SOxList.append(cancer['SOx'].iloc[p])
                    PM10List.append(cancer['PM10'].iloc[p])
                    PM25List.append(cancer['PM2.5'].iloc[p])
                    # totalIndustry.append(1)
                    
                    if cancer['Primary Sector'].iloc[p] == 1:
                        if 1 not in industriesList4:
                            cogenerationList.append(1)
                            industriesList4.append(1)
                        else:
                            cogenerationList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[p] == 2:
                        if 2 not in industriesList4:
                            otherCombustionList.append(2)
                            industriesList4.append(2)
                        else:
                            otherCombustionList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[p] == 3:
                        if 3 not in industriesList4:
                            electricityList.append(3)
                            industriesList4.append(3)
                        else:
                            electricityList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[p] == 4:
                        if 4 not in industriesList4:
                            cementList.append(4)
                            industriesList4.append(4)
                        else:
                            cementList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[p] == 5:
                        if 5 not in industriesList4:
                            hydrogenList.append(5)
                            industriesList4.append(5)
                        else:
                            hydrogenList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[p] == 6:
                        if 6 not in industriesList4:
                            refineryList.append(6)
                            industriesList4.append(6)
                        else:
                            refineryList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[p] == 7:
                        if 7 not in industriesList4:
                            oilGasList.append(7)
                            industriesList4.append(7)
                        else:
                            oilGasList[-1:] += 1
                    
                    tally4 = 1
                
                elif tally4 != 0:
                    CO2List[-1:] += cancer['CO2'].iloc[p]
                    CH4List[-1:] += cancer['CH4'].iloc[p]
                    N2OList[-1:] += cancer['N2O'].iloc[p]
                    VOCList[-1:] += cancer['VOC'].iloc[p]
                    NOxList[-1:] += cancer['NOx'].iloc[p]
                    SOxList[-1:] += cancer['SOx'].iloc[p]
                    PM10List[-1:] += cancer['PM10'].iloc[p]
                    PM25List[-1:] += cancer['PM2.5'].iloc[p]
                    
                    if cancer['Primary Sector'].iloc[p] == 1:
                        if 1 not in industriesList4:
                            cogenerationList.append(1)
                            industriesList4.append(1)
                        else:
                            cogenerationList[-1:] += cancer['Primary Sector'].iloc[p]
                    elif cancer['Primary Sector'].iloc[p] == 2:
                        if 2 not in industriesList4:
                            otherCombustionList.append(2)
                            industriesList4.append(2)
                        else:
                            otherCombustionList[-1:] += cancer['Primary Sector'].iloc[p]
                    elif cancer['Primary Sector'].iloc[p] == 3:
                        if 3 not in industriesList4:
                            electricityList.append(3)
                            industriesList4.append(3)
                        else:
                            electricityList[-1:] += cancer['Primary Sector'].iloc[p]
                    elif cancer['Primary Sector'].iloc[p] == 4:
                        if 4 not in industriesList4:
                            cementList.append(4)
                            industriesList4.append(4)
                        else:
                            cementList[-1:] += cancer['Primary Sector'].iloc[p]
                    elif cancer['Primary Sector'].iloc[p] == 5:
                        if 5 not in industriesList4:
                            hydrogenList.append(5)
                            industriesList4.append(5)
                        else:
                            hydrogenList[-1:] += cancer['Primary Sector'].iloc[p]
                    elif cancer['Primary Sector'].iloc[p] == 6:
                        if 6 not in industriesList4:
                            refineryList.append(6)
                            industriesList4.append(6)
                        else:
                            refineryList[-1:] += cancer['Primary Sector'].iloc[p]
                    elif cancer['Primary Sector'].iloc[p] == 7:
                        if 7 not in industriesList4:
                            oilGasList.append(7)
                            industriesList4.append(7)
                        else:
                            oilGasList[-1:] += cancer['Primary Sector'].iloc[p]
        if p == 3855:
            if 4 not in industriesList4:
                cementList.append(0)
            if 5 not in industriesList4:
                hydrogenList.append(0)
            if 6 not in industriesList4:
                refineryList.append(0)
            if 7 not in industriesList4:
                oilGasList.append(0)
            
            if 1 not in industriesList4:
                cogenerationList.append(0)
            if 2 not in industriesList4:
                otherCombustionList.append(0)
            if 3 not in industriesList4:
                electricityList.append(0)
                
            
            if tally4 == 0:
                CO2List.append(0)
                CH4List.append(0)
                N2OList.append(0)
                VOCList.append(0)
                NOxList.append(0)
                SOxList.append(0)
                PM10List.append(0)
                PM25List.append(0)
                    
                    # totalIndustry[-1:] += 1
                    
                    
     
    for t in range(0, 3856):
        if cancer['Year'].iloc[t] == 2012:
            if cancer['County'].iloc[t] == i:
                if tally5 == 0:
                    CO2List.append(cancer['CO2'].iloc[t])
                    CH4List.append(cancer['CH4'].iloc[t])
                    N2OList.append(cancer['N2O'].iloc[t])
                    VOCList.append(cancer['VOC'].iloc[t])
                    NOxList.append(cancer['NOx'].iloc[t])
                    SOxList.append(cancer['SOx'].iloc[t])
                    PM10List.append(cancer['PM10'].iloc[t])
                    PM25List.append(cancer['PM2.5'].iloc[t])
                    # totalIndustry.append(1)
                    
                    if cancer['Primary Sector'].iloc[t] == 1:
                        if 1 not in industriesList5:
                            cogenerationList.append(1)
                            industriesList5.append(1)
                        else:
                            cogenerationList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[t] == 2:
                        if 2 not in industriesList5:
                            otherCombustionList.append(2)
                            industriesList5.append(2)
                        else:
                            otherCombustionList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[t] == 3:
                        if 3 not in industriesList5:
                            electricityList.append(3)
                            industriesList5.append(3)
                        else:
                            electricityList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[t] == 4:
                        if 4 not in industriesList5:
                            cementList.append(4)
                            industriesList5.append(4)
                        else:
                            cementList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[t] == 5:
                        if 5 not in industriesList5:
                            hydrogenList.append(5)
                            industriesList5.append(5)
                        else:
                            hydrogenList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[t] == 6:
                        if 6 not in industriesList5:
                            refineryList.append(6)
                            industriesList5.append(6)
                        else:
                            refineryList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[t] == 7:
                        if 7 not in industriesList5:
                            oilGasList.append(7)
                            industriesList5.append(7)
                        else:
                            oilGasList[-1:] += 1
                    
                    tally5 = 1
                
                elif tally5 != 0:
                    CO2List[-1:] += cancer['CO2'].iloc[t]
                    CH4List[-1:] += cancer['CH4'].iloc[t]
                    N2OList[-1:] += cancer['N2O'].iloc[t]
                    VOCList[-1:] += cancer['VOC'].iloc[t]
                    NOxList[-1:] += cancer['NOx'].iloc[t]
                    SOxList[-1:] += cancer['SOx'].iloc[t]
                    PM10List[-1:] += cancer['PM10'].iloc[t]
                    PM25List[-1:] += cancer['PM2.5'].iloc[t]
                    
                    if cancer['Primary Sector'].iloc[t] == 1:
                        if 1 not in industriesList5:
                            cogenerationList.append(1)
                            industriesList5.append(1)
                        else:
                            cogenerationList[-1:] += cancer['Primary Sector'].iloc[t]
                    elif cancer['Primary Sector'].iloc[t] == 2:
                        if 2 not in industriesList5:
                            otherCombustionList.append(2)
                            industriesList5.append(2)
                        else:
                            otherCombustionList[-1:] += cancer['Primary Sector'].iloc[t]
                    elif cancer['Primary Sector'].iloc[t] == 3:
                        if 3 not in industriesList5:
                            electricityList.append(3)
                            industriesList5.append(3)
                        else:
                            electricityList[-1:] += cancer['Primary Sector'].iloc[t]
                    elif cancer['Primary Sector'].iloc[t] == 4:
                        if 4 not in industriesList5:
                            cementList.append(4)
                            industriesList5.append(4)
                        else:
                            cementList[-1:] += cancer['Primary Sector'].iloc[t]
                    elif cancer['Primary Sector'].iloc[t] == 5:
                        if 5 not in industriesList5:
                            hydrogenList.append(5)
                            industriesList5.append(5)
                        else:
                            hydrogenList[-1:] += cancer['Primary Sector'].iloc[t]
                    elif cancer['Primary Sector'].iloc[t] == 6:
                        if 6 not in industriesList5:
                            refineryList.append(6)
                            industriesList5.append(6)
                        else:
                            refineryList[-1:] += cancer['Primary Sector'].iloc[t]
                    elif cancer['Primary Sector'].iloc[t] == 7:
                        if 7 not in industriesList5:
                            oilGasList.append(7)
                            industriesList5.append(7)
                        else:
                            oilGasList[-1:] += cancer['Primary Sector'].iloc[t]
        if t == 3855:
            if 4 not in industriesList5:
                cementList.append(0)
            if 5 not in industriesList5:
                hydrogenList.append(0)
            if 6 not in industriesList5:
                refineryList.append(0)
            if 7 not in industriesList5:
                oilGasList.append(0)
                
            if 1 not in industriesList5:
                cogenerationList.append(0)
            if 2 not in industriesList5:
                otherCombustionList.append(0)
            if 3 not in industriesList5:
                electricityList.append(0)
            
            if tally5 == 0:
                CO2List.append(0)
                CH4List.append(0)
                N2OList.append(0)
                VOCList.append(0)
                NOxList.append(0)
                SOxList.append(0)
                PM10List.append(0)
                PM25List.append(0)
                    
                    # totalIndustry[-1:] += 1
                    
                    
                    
    
    for l in range(0, 3856):
        if cancer['Year'].iloc[l] == 2013:
            if cancer['County'].iloc[l] == i:
                if tally6 == 0:
                    CO2List.append(cancer['CO2'].iloc[l])
                    CH4List.append(cancer['CH4'].iloc[l])
                    N2OList.append(cancer['N2O'].iloc[l])
                    VOCList.append(cancer['VOC'].iloc[l])
                    NOxList.append(cancer['NOx'].iloc[l])
                    SOxList.append(cancer['SOx'].iloc[l])
                    PM10List.append(cancer['PM10'].iloc[l])
                    PM25List.append(cancer['PM2.5'].iloc[l])
                    # totalIndustry.append(1)
                    
                    if cancer['Primary Sector'].iloc[l] == 1:
                        if 1 not in industriesList6:
                            cogenerationList.append(1)
                            industriesList6.append(1)
                        else:
                            cogenerationList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[l] == 2:
                        if 2 not in industriesList6:
                            otherCombustionList.append(2)
                            industriesList6.append(2)
                        else:
                            otherCombustionList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[l] == 3:
                        if 3 not in industriesList6:
                            electricityList.append(3)
                            industriesList6.append(3)
                        else:
                            electricityList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[l] == 4:
                        if 4 not in industriesList6:
                            cementList.append(4)
                            industriesList6.append(4)
                        else:
                            cementList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[l] == 5:
                        if 5 not in industriesList6:
                            hydrogenList.append(5)
                            industriesList6.append(5)
                        else:
                            hydrogenList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[l] == 6:
                        if 6 not in industriesList6:
                            refineryList.append(6)
                            industriesList6.append(6)
                        else:
                            refineryList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[l] == 7:
                        if 7 not in industriesList6:
                            oilGasList.append(7)
                            industriesList6.append(7)
                        else:
                            oilGasList[-1:] += 1
                    
                    tally6 = 1
                
                elif tally6 != 0:
                    CO2List[-1:] += cancer['CO2'].iloc[l]
                    CH4List[-1:] += cancer['CH4'].iloc[l]
                    N2OList[-1:] += cancer['N2O'].iloc[l]
                    VOCList[-1:] += cancer['VOC'].iloc[l]
                    NOxList[-1:] += cancer['NOx'].iloc[l]
                    SOxList[-1:] += cancer['SOx'].iloc[l]
                    PM10List[-1:] += cancer['PM10'].iloc[l]
                    PM25List[-1:] += cancer['PM2.5'].iloc[l]
                    
                    if cancer['Primary Sector'].iloc[l] == 1:
                        if 1 not in industriesList6:
                            cogenerationList.append(1)
                            industriesList6.append(1)
                        else:
                            cogenerationList[-1:] += cancer['Primary Sector'].iloc[l]
                    elif cancer['Primary Sector'].iloc[l] == 2:
                        if 2 not in industriesList6:
                            otherCombustionList.append(2)
                            industriesList6.append(2)
                        else:
                            otherCombustionList[-1:] += cancer['Primary Sector'].iloc[l]
                    elif cancer['Primary Sector'].iloc[l] == 3:
                        if 3 not in industriesList6:
                            electricityList.append(3)
                            industriesList6.append(3)
                        else:
                            electricityList[-1:] += cancer['Primary Sector'].iloc[l]
                    elif cancer['Primary Sector'].iloc[l] == 4:
                        if 4 not in industriesList6:
                            cementList.append(4)
                            industriesList6.append(4)
                        else:
                            cementList[-1:] += cancer['Primary Sector'].iloc[l]
                    elif cancer['Primary Sector'].iloc[l] == 5:
                        if 5 not in industriesList6:
                            hydrogenList.append(5)
                            industriesList6.append(5)
                        else:
                            hydrogenList[-1:] += cancer['Primary Sector'].iloc[l]
                    elif cancer['Primary Sector'].iloc[l] == 6:
                        if 6 not in industriesList6:
                            refineryList.append(6)
                            industriesList6.append(6)
                        else:
                            refineryList[-1:] += cancer['Primary Sector'].iloc[l]
                    elif cancer['Primary Sector'].iloc[l] == 7:
                        if 7 not in industriesList6:
                            oilGasList.append(7)
                            industriesList6.append(7)
                        else:
                            oilGasList[-1:] += cancer['Primary Sector'].iloc[l]
        if l == 3855:
            if 4 not in industriesList6:
                cementList.append(0)
            if 5 not in industriesList6:
                hydrogenList.append(0)
            if 6 not in industriesList6:
                refineryList.append(0)
            if 7 not in industriesList6:
                oilGasList.append(0)
            
            if 1 not in industriesList6:
                cogenerationList.append(0)
            if 2 not in industriesList6:
                otherCombustionList.append(0)
            if 3 not in industriesList6:
                electricityList.append(0)
            
            if tally6 == 0:
                CO2List.append(0)
                CH4List.append(0)
                N2OList.append(0)
                VOCList.append(0)
                NOxList.append(0)
                SOxList.append(0)
                PM10List.append(0)
                PM25List.append(0)
                    
                    # totalIndustry[-1:] += 1
                    
    
    for n in range(0, 3856):
        if cancer['Year'].iloc[n] == 2014:
            if cancer['County'].iloc[n] == i:
                if tally7 == 0:
                    CO2List.append(cancer['CO2'].iloc[n])
                    CH4List.append(cancer['CH4'].iloc[n])
                    N2OList.append(cancer['N2O'].iloc[n])
                    VOCList.append(cancer['VOC'].iloc[n])
                    NOxList.append(cancer['NOx'].iloc[n])
                    SOxList.append(cancer['SOx'].iloc[n])
                    PM10List.append(cancer['PM10'].iloc[n])
                    PM25List.append(cancer['PM2.5'].iloc[n])
                    # totalIndustry.append(1)
                    
                    if cancer['Primary Sector'].iloc[n] == 1:
                        if 1 not in industriesList7:
                            cogenerationList.append(1)
                            industriesList7.append(1)
                        else:
                            cogenerationList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[n] == 2:
                        if 2 not in industriesList7:
                            otherCombustionList.append(2)
                            industriesList7.append(2)
                        else:
                            otherCombustionList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[n] == 3:
                        if 3 not in industriesList7:
                            electricityList.append(3)
                            industriesList7.append(3)
                        else:
                            electricityList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[n] == 4:
                        if 4 not in industriesList7:
                            cementList.append(4)
                            industriesList7.append(4)
                        else:
                            cementList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[n] == 5:
                        if 5 not in industriesList7:
                            hydrogenList.append(5)
                            industriesList7.append(5)
                        else:
                            hydrogenList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[n] == 6:
                        if 6 not in industriesList7:
                            refineryList.append(6)
                            industriesList7.append(6)
                        else:
                            refineryList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[n] == 7:
                        if 7 not in industriesList7:
                            oilGasList.append(7)
                            industriesList7.append(7)
                        else:
                            oilGasList[-1:] += 1
                    
                    tally7 = 1
                
                elif tally7 != 0:
                    CO2List[-1:] += cancer['CO2'].iloc[n]
                    CH4List[-1:] += cancer['CH4'].iloc[n]
                    N2OList[-1:] += cancer['N2O'].iloc[n]
                    VOCList[-1:] += cancer['VOC'].iloc[n]
                    NOxList[-1:] += cancer['NOx'].iloc[n]
                    SOxList[-1:] += cancer['SOx'].iloc[n]
                    PM10List[-1:] += cancer['PM10'].iloc[n]
                    PM25List[-1:] += cancer['PM2.5'].iloc[n]
                    
                    if cancer['Primary Sector'].iloc[n] == 1:
                        if 1 not in industriesList7:
                            cogenerationList.append(1)
                            industriesList7.append(1)
                        else:
                            cogenerationList[-1:] += cancer['Primary Sector'].iloc[n]
                    elif cancer['Primary Sector'].iloc[n] == 2:
                        if 2 not in industriesList7:
                            otherCombustionList.append(2)
                            industriesList7.append(2)
                        else:
                            otherCombustionList[-1:] += cancer['Primary Sector'].iloc[n]
                    elif cancer['Primary Sector'].iloc[n] == 3:
                        if 3 not in industriesList7:
                            electricityList.append(3)
                            industriesList7.append(3)
                        else:
                            electricityList[-1:] += cancer['Primary Sector'].iloc[n]
                    elif cancer['Primary Sector'].iloc[n] == 4:
                        if 4 not in industriesList7:
                            cementList.append(4)
                            industriesList7.append(4)
                        else:
                            cementList[-1:] += cancer['Primary Sector'].iloc[n]
                    elif cancer['Primary Sector'].iloc[n] == 5:
                        if 5 not in industriesList7:
                            hydrogenList.append(5)
                            industriesList7.append(5)
                        else:
                            hydrogenList[-1:] += cancer['Primary Sector'].iloc[n]
                    elif cancer['Primary Sector'].iloc[n] == 6:
                        if 6 not in industriesList7:
                            refineryList.append(6)
                            industriesList7.append(6)
                        else:
                            refineryList[-1:] += cancer['Primary Sector'].iloc[n]
                    elif cancer['Primary Sector'].iloc[n] == 7:
                        if 7 not in industriesList7:
                            oilGasList.append(7)
                            industriesList7.append(7)
                        else:
                            oilGasList[-1:] += cancer['Primary Sector'].iloc[n]
        if n == 3855:
            if 4 not in industriesList7:
                cementList.append(0)
            if 5 not in industriesList7:
                hydrogenList.append(0)
            if 6 not in industriesList7:
                refineryList.append(0)
            if 7 not in industriesList7:
                oilGasList.append(0)
                
            if 1 not in industriesList7:
                cogenerationList.append(0)
            if 2 not in industriesList7:
                otherCombustionList.append(0)
            if 3 not in industriesList7:
                electricityList.append(0)
                
            if tally7 == 0:
                CO2List.append(0)
                CH4List.append(0)
                N2OList.append(0)
                VOCList.append(0)
                NOxList.append(0)
                SOxList.append(0)
                PM10List.append(0)
                PM25List.append(0)
                    
                    # totalIndustry[-1:] += 1
                    
        
     
    for b in range(0, 3856):
        if cancer['Year'].iloc[b] == 2015:
            if cancer['County'].iloc[b] == i:
                if tally8 == 0:
                    CO2List.append(cancer['CO2'].iloc[b])
                    CH4List.append(cancer['CH4'].iloc[b])
                    N2OList.append(cancer['N2O'].iloc[b])
                    VOCList.append(cancer['VOC'].iloc[b])
                    NOxList.append(cancer['NOx'].iloc[b])
                    SOxList.append(cancer['SOx'].iloc[b])
                    PM10List.append(cancer['PM10'].iloc[b])
                    PM25List.append(cancer['PM2.5'].iloc[b])
                    # totalIndustry.append(1)
                    
                    if cancer['Primary Sector'].iloc[b] == 1:
                        if 1 not in industriesList8:
                            cogenerationList.append(1)
                            industriesList8.append(1)
                        else:
                            cogenerationList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[b] == 2:
                        if 2 not in industriesList8:
                            otherCombustionList.append(2)
                            industriesList8.append(2)
                        else:
                            otherCombustionList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[b] == 3:
                        if 3 not in industriesList8:
                            electricityList.append(3)
                            industriesList8.append(3)
                        else:
                            electricityList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[b] == 4:
                        if 4 not in industriesList8:
                            cementList.append(4)
                            industriesList8.append(4)
                        else:
                            cementList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[b] == 5:
                        if 5 not in industriesList8:
                            hydrogenList.append(5)
                            industriesList8.append(5)
                        else:
                            hydrogenList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[b] == 6:
                        if 6 not in industriesList8:
                            refineryList.append(6)
                            industriesList8.append(6)
                        else:
                            refineryList[-1:] += 1
                    elif cancer['Primary Sector'].iloc[b] == 7:
                        if 7 not in industriesList8:
                            oilGasList.append(7)
                            industriesList8.append(7)
                        else:
                            oilGasList[-1:] += 1
                    
                
                    tally8 = 1
                
                elif tally8 != 0:
                    CO2List[-1:] += cancer['CO2'].iloc[b]
                    CH4List[-1:] += cancer['CH4'].iloc[b]
                    N2OList[-1:] += cancer['N2O'].iloc[b]
                    VOCList[-1:] += cancer['VOC'].iloc[b]
                    NOxList[-1:] += cancer['NOx'].iloc[b]
                    SOxList[-1:] += cancer['SOx'].iloc[b]
                    PM10List[-1:] += cancer['PM10'].iloc[b]
                    PM25List[-1:] += cancer['PM2.5'].iloc[b]
                    
                    if cancer['Primary Sector'].iloc[b] == 1:
                        if 1 not in industriesList8:
                            cogenerationList.append(1)
                            industriesList8.append(1)
                        else:
                            cogenerationList[-1:] += cancer['Primary Sector'].iloc[b]
                    elif cancer['Primary Sector'].iloc[b] == 2:
                        if 2 not in industriesList8:
                            otherCombustionList.append(2)
                            industriesList8.append(2)
                        else:
                            otherCombustionList[-1:] += cancer['Primary Sector'].iloc[b]
                    elif cancer['Primary Sector'].iloc[b] == 3:
                        if 3 not in industriesList8:
                            electricityList.append(3)
                            industriesList8.append(3)
                        else:
                            electricityList[-1:] += cancer['Primary Sector'].iloc[b]
                    elif cancer['Primary Sector'].iloc[b] == 4:
                        if 4 not in industriesList8:
                            cementList.append(4)
                            industriesList8.append(4)
                        else:
                            cementList[-1:] += cancer['Primary Sector'].iloc[b]
                    elif cancer['Primary Sector'].iloc[b] == 5:
                        if 5 not in industriesList8:
                            hydrogenList.append(5)
                            industriesList8.append(5)
                        else:
                            hydrogenList[-1:] += cancer['Primary Sector'].iloc[b]
                    elif cancer['Primary Sector'].iloc[b] == 6:
                        if 6 not in industriesList8:
                            refineryList.append(6)
                            industriesList8.append(6)
                        else:
                            refineryList[-1:] += cancer['Primary Sector'].iloc[b]
                    elif cancer['Primary Sector'].iloc[b] == 7:
                        if 7 not in industriesList8:
                            oilGasList.append(7)
                            industriesList8.append(7)
                        else:
                            oilGasList[-1:] += cancer['Primary Sector'].iloc[b]
                            
        if b == 3855:
            if 4 not in industriesList8:
                cementList.append(0)
            if 5 not in industriesList8:
                hydrogenList.append(0)
            if 6 not in industriesList8:
                refineryList.append(0)
            if 7 not in industriesList8:
                oilGasList.append(0)
                
            if 1 not in industriesList8:
                cogenerationList.append(0)
            if 2 not in industriesList8:
                otherCombustionList.append(0)
            if 3 not in industriesList8:
                electricityList.append(0)
            
            if tally8 == 0:
                CO2List.append(0)
                CH4List.append(0)
                N2OList.append(0)
                VOCList.append(0)
                NOxList.append(0)
                SOxList.append(0)
                PM10List.append(0)
                PM25List.append(0)
                    
                    # totalIndustry[-1:] += 1
                    
                        
                
            
                
                
            
            
#         else:
#             countyList.append(cancer['County'].iloc(i))
#             yearList.append(cancer['Year'].iloc(i))
#             sectorList.append(cancer['Primary Sector'].iloc(i))
#             CO2List.append(cancer['CO2'].iloc(i))
#             CH4List.append(cancer['CH4'].iloc(i))
#             N2OList.append(cancer['N2O'].iloc(i))
#             VOCList.append(cancer['VOC'].iloc(i))
#             NOxList.append(cancer['NOx'].iloc(i))
#             SOxList.append(cancer['SOx'].iloc(i))
#             PM10List.append(cancer['PM10'].iloc(i))
#             PM25List.append(cancer['PM2.5'].iloc(i))
#             #etc do this for rest
            
        
#             elif cancer['Year'] == 2009:
        
#             elif cancer['Year'] == 2010:
        
#             elif cancer['Year'] == 2011:
    
#             elif cancer['Year'] == 2012:
        
#             elif cancer['Year'] == 2013:
        
#             elif cancer['Year'] == 2014:
        
#             elif cancer['Year'] == 2015:
print(CO2List)
print(N2OList)
print(VOCList)


# In[54]:


CO2Temp = []


for i in CO2List:
    if i != 0:
        CO2Temp.append(i)
        

avgCO2 = sum(CO2Temp)/len(CO2Temp)

CO2List2 = [avgCO2 if i == 0 else i for i in CO2List]
    


CH4Temp = []


for i in CH4List:
    if i != 0:
        CH4Temp.append(i)
        

avgCH4 = sum(CH4Temp)/len(CH4Temp)

CH4List2 = [avgCH4 if i == 0 else i for i in CH4List]
    


N2OTemp = []


for i in N2OList:
    if i != 0:
        N2OTemp.append(i)
        

avgN2O = sum(N2OTemp)/len(N2OTemp)

N2OList2 = [avgN2O if i == 0 else i for i in N2OList]
    

                
VOCTemp = []


for i in VOCList:
    if i > 0:
        
        VOCTemp.append(i)
        

avgVOC = sum(VOCTemp)/len(VOCTemp)
print(avgVOC)
VOCList2 = [avgVOC if i == 0 or i == 'nan' else i for i in VOCList]
    

                
NOxTemp = []


for i in NOxList:
    if i > 0:
        NOxTemp.append(i)
        

avgNOx = sum(NOxTemp)/len(NOxTemp)
print(avgNOx)
NOxList2 = [avgNOx if i == 0 else i for i in NOxList]
    

                
SOxTemp = []


for i in SOxList:
    if i != 0:
        SOxTemp.append(i)
        

avgSOx = sum(SOxTemp)/len(SOxTemp)

SOxList2 = [avgSOx if i == 0 else i for i in SOxList]
    

                
PM10Temp = []


for i in PM10List:
    if i != 0:
        PM10Temp.append(i)
        

avgPM10 = sum(PM10Temp)/len(PM10Temp)

PM10List2 = [avgPM10 if i == 0 else i for i in PM10List]
    

                
PM25Temp = []


for i in PM25List:
    if i != 0:
        PM25Temp.append(i)
        

avgPM25 = sum(PM25Temp)/len(PM25Temp)

PM25List2 = [avgPM25 if i == 0 else i for i in PM25List]
    
print(VOCList)


# In[65]:


cogenerationList2 = []
otherCombustionList2 = []
electricityList2 = []
cementList2 = []
hydrogenList2 = []
refineryList2 = []
oilGasList2 = []
for i in cogenerationList:
    cogenerationList2.append((i/1))
    
for i in otherCombustionList:
    otherCombustionList2.append((i/2))
    
for i in electricityList:
    electricityList2.append((i/3))
    
for i in cementList:
    cementList2.append((i/4))
    
    
for i in hydrogenList:
    hydrogenList2.append((i/5))

for i in refineryList:
    refineryList2.append((i/6))
    
for i in oilGasList:
    oilGasList2.append((i/7))
print(electricityList2)


# In[66]:


cogenerationTemp = []


for i in cogenerationList2:
    if i != 0:
        cogenerationTemp.append(i)
        

avgcogeneration = sum(cogenerationTemp)/len(cogenerationTemp)
cogenerationList2 = [avgcogeneration if i == 0 else i for i in cogenerationList2]


otherCombustionTemp = []


for i in otherCombustionList2:
    if i != 0:
        otherCombustionTemp.append(i)
        

avgotherCombustion = sum(otherCombustionTemp)/len(otherCombustionTemp)
otherCombustionList2 = [avgotherCombustion if i == 0 else i for i in otherCombustionList2]


electricityTemp = []


for i in electricityList2:
    if i != 0:
        electricityTemp.append(i)
        

avgelectricity = sum(electricityTemp)/len(electricityTemp)
electricityList2 = [avgelectricity if i == 0 else i for i in electricityList2]
print(otherCombustionList2)


# In[16]:


dataCancer = {'year': cancerYearList, 'county': listRandom, 'cancer rate': countyRatesList,
              'CO2': CO2List, 'N2O': N2OList, 'VOC': VOCList, 'CH4': CH4List, 
              'NOx': NOxList, 'SOx': SOxList, 'PM10': PM10List, 'PM2.5': PM25List, 'cogeneration': cogenerationList2,
              'other combustion': otherCombustionList2, 'electricity': electricityList2, 'cement': cementList2, 'hydrogen':
              hydrogenList2, 'refinery': refineryList2, 'oil and gas': oilGasList2}



df = pd.DataFrame(data=dataCancer)
df['VOC'].fillna(avgVOC)
df['NOx'].fillna(avgNOx)
df

df.to_csv('countyCancerFinal.csv', index=False)




# In[11]:


countyFinal = pd.read_csv('countyCancerFinal.csv')


corr = countyFinal.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(countyFinal.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(countyFinal.columns)
ax.set_yticklabels(countyFinal.columns)
plt.show()


# In[26]:


# df['column'] = df['column'].fillna(value)

null_columns=countyFinal.columns[countyFinal.isnull().any()]
countyFinal[null_columns].isnull().sum()


# In[25]:


countyFinal['VOC'] = countyFinal['VOC'].fillna(0)
countyFinal['NOx'] = countyFinal['NOx'].fillna(0)


# In[27]:


import numpy as np
cancer_label = countyFinal['PM2.5']
cancer_X = countyFinal.drop('PM2.5', axis=1)


# In[29]:


y_train


# In[28]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(cancer_X, cancer_label, test_size=0.10, random_state=42)


# In[22]:





# In[30]:


from sklearn.ensemble import RandomForestRegressor




rnd_clf = RandomForestRegressor(n_estimators=500, max_leaf_nodes=16, n_jobs=-1)
rnd_clf.fit(X_train, y_train)

y_pred_rf = rnd_clf.predict(X_test)


# In[31]:


from sklearn.ensemble import RandomForestRegressor




rnd_clf = RandomForestRegressor(n_estimators=500, max_leaf_nodes=16, n_jobs=-1)
rnd_clf.fit(X_train, y_train)

y_pred_rf = rnd_clf.predict(X_test)
print(rnd_clf.score(X_train, y_train))
print(rnd_clf.score(X_test, y_test))


# In[33]:


import pandas as pd 
feature_importances = pd.DataFrame(rnd_clf.feature_importances_, index = X_train.columns, columns=['importance']).sort_values('importance', ascending=False)
feature_importances


# In[14]:


countylist = []
for i in countyFinal2['county']:
    if i not in countylist:
        countylist.append(i)
        
print(len(countylist))


# In[12]:


import numpy as np
import matplotlib.pyplot as plt
countyFinal2 = pd.read_csv('countyCancerFinal2.csv')


corr = countyFinal2.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(countyFinal2.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(countyFinal2.columns)
ax.set_yticklabels(countyFinal2.columns)
plt.show()


# In[13]:


import numpy as np
cancer_label = countyFinal2['PM2.5']
cancer_X = countyFinal2.drop('PM2.5', axis=1)


# In[14]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(cancer_X, cancer_label, test_size=0.10, random_state=42)


# In[15]:


from sklearn.ensemble import RandomForestRegressor




rnd_clf = RandomForestRegressor(n_estimators=500, max_leaf_nodes=16, n_jobs=-1)
rnd_clf.fit(X_train, y_train)

y_pred_rf = rnd_clf.predict(X_test)
print(rnd_clf.score(X_train, y_train))
print(rnd_clf.score(X_test, y_test))


# In[16]:


import pandas as pd 
feature_importances = pd.DataFrame(rnd_clf.feature_importances_, index = X_train.columns, columns=['importance']).sort_values('importance', ascending=False)
feature_importances


# In[17]:




year = [2012, 2012, 2012]
county = [37, 105, 91]
cancer_rate = [50, 45, 50]
cogeneration = [3, 3, 3]
otherComb = [3, 5, 5]
electricity = [4, 4, 4]
cement = [3, 1, 10]
hydrogen = [6, 5, 30]
refinery = [5, 1, 1]
oilGas = [0, 1, 1]

testData = {'year': year, 'county': county, 'cancer rate': cancer_rate, 'cogeneration': cogeneration, 'other combustion': otherComb,
            'electricity': electricity, 'cement': cement, 'hydrogen': hydrogen, 'refinery': refinery, 'oil and gas': oilGas}

testDataTable = pd.DataFrame(data=testData)
testDataTable

cancerX = testDataTable


# In[18]:


pred_final = rnd_clf.predict(cancerX)
print(pred_final)


# In[19]:


countyFinal2 = countyFinal2.drop('cancer rate', axis=1)
corr_matrix = countyFinal2.corr(method='pearson', min_periods=1)
corr_matrix["PM2.5"].sort_values(ascending=False)


# In[12]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

corr = df.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(df.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.columns)
plt.show()


# In[18]:


corr_matrix = df.corr(method='pearson', min_periods=1)
print(corr_matrix)


# In[19]:


cancer.dtypes


# In[24]:


cancer['CO2'].astype(float)


# In[15]:


corr_matrix["PM2.5"].sort_values(ascending=False)


# In[ ]:




