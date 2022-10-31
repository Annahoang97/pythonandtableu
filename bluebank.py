# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 22:33:15 2022

@author: asus
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

# with statement is the same as creating a variable: variable = statement. 
# with statement makes your code clean and readable, so it executes better when
# there are any error as well

#transform to dataframe
loandata = pd.DataFrame(data)

#finding unique values for the purpose column
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe the data for specific column
loandata['int.rate'].describe()

loandata['fico'].describe()

loandata['dti'].describe()

#using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annual.inc'] = income


# FICO scores

fico = 700

# - 300 - 400: Very Poor
# - 401 - 600: Poor
# - 601 - 660: Fair
# - 661 - 780: Good
# - 781 - 850: Excellent

if fico >= 300 and fico <= 400:
    ficocat = 'Very Poor'
elif fico >=401 and fico <= 600:
    ficocat = 'Poor'
elif fico >=601 and fico  <= 660:
    ficocat = 'Fair'
elif fico >= 661 and fico <= 780:
    ficocat = 'Good'
elif fico >= 781 and fico <= 850:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'


#apply for loops to loan data

ficocats =[]
n = len(loandata)

# for i in range(n):
#     fico = loandata['fico'][i]
#     if fico >= 300 and fico <= 400:
#         ficocat = 'Very Poor'
#     elif fico >=401 and fico <= 600:
#         ficocat = 'Poor'
#     elif fico >=601 and fico  <= 660:
#         ficocat = 'Fair'
#     elif fico >= 661 and fico <= 780:
#         ficocat = 'Good'
#     elif fico >= 781 and fico <= 850:
#         ficocat = 'Excellent'
#     else:
#         ficocat = 'Unknown'
#     ficocats.append(ficocat)

# loandata['fico.category'] = ficocats


# ficocats = pd.Series(ficocats)
# loandata['fico.category'] = ficocats


#testing error

for i in range(n):
    fico = loandata['fico'][i]
    try:
        if fico >= 300 and fico <= 400:
            ficocat = 'Very Poor'
        elif fico >=401 and fico <= 600:
            ficocat = 'Poor'
        elif fico >=601 and fico  <= 660:
            ficocat = 'Fair'
        elif fico >= 661 and fico <= 780:
            ficocat = 'Good'
        elif fico >= 781 and fico <= 850:
            ficocat = 'Excellent'
        else:
            ficocat = 'Unknown'
    except:
        ficocat = 'Unknown'
    ficocats.append(ficocat)

loandata['fico.category'] = ficocats

#df.loc as conditional statements
# df.loc[df[column_name] condition, new_column_name] = 'value if the condition is met'

# for interest rates, a new column is wanted, rate >0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loans/rows by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.4)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red', width = 0.4)
plt.show()

#scatter plots

ypoint = loandata['annual.inc']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()

#writing to csv

loandata.to_csv('loandata_cleaned.csv', index = True)











