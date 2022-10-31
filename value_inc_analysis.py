# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 23:12:19 2022

@author: asus
"""

import pandas as pd
# file_name = pd.read_csv('file.csv') <--- format of read_csv
data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

# Sumary of the data
data.info()

# Playing around with variables

# Working with calculations

# Defining variables

CostPerItem = 11.73

# Variable = dataFrame['column_name']

# Cost Per Transaction
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

# Sales Per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit Per Transaction
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup = (Sales - Cost)/Cost
data['Markup'] = data['ProfitPerTransaction']/data['CostPerTransaction']

# Rounding Markup
roundMarkup = round(data['Markup'], 2)
data['Markup'] = round(data['Markup'], 2)

# Combining data fields
data['Date'] = str(data['Year']) +'-'+ data['Month'] +'-'+ str(data['Day'])


# Checking columns data type
print(data['Day'].dtype)

# Change columns type
day = data['Day'].astype(str)
print(day.dtype)
year = data['Year'].astype(str)

my_date = day +'-'+data['Month']+'-'+year
#my_date = my_date.strftime('%Y%m%d') # <--- error: 'Series' object has no attribute 'strftime'
data['Date'] = my_date

# Using iloc to view specific columns/rows
data.iloc[0] # View the row with index = 0
data.iloc[0:3] #first three rows
data.iloc[-5:] #last five rows

data.head(5) #see first five rows
data.tail(5) #view last five rows

data.iloc[:,2] #view all rows in the column with index = 2

data.iloc[4,2] #brings in data in the 4th row, 2nd column

# Using split to split the client keywords field
# new_var = column.str.split('sep', expand=True)
split_col = data['ClientKeywords'].str.split(',', expand=True)

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContact'] = split_col[2]

# Using the replace function
data['ClientAge'] = data['ClientAge'].str.replace("[","")
data['LengthofContact'] = data['LengthofContact'].str.replace(']','')

# Using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

# How to merge file
# bring in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep = ';')

# merging files: merge_df = pd.merge(df_old, df_new, on='key')
data = pd.merge(data, seasons, on='Month')

# Dropping columns
# df = df.drop('column_name', axis=1)

data = data.drop('ClientKeywords', axis = 1)

data = data.drop(['Day','Year','Month'], axis = 1) #drop multiple columns

# Export into a CSV
data.to_csv('ValueInc_Cleaned.csv', index = False)

#data.to_excel('ValueInc_Cleaned.xlsx')












