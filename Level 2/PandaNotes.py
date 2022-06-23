#from pickle import FALSE
from pickle import FALSE
import numpy as np
import pandas as pd

#If excel file then read_xlsx
#If tab separated file (ex. .txt) --> , read_csv(, delimiter='/t')

df = pd.read_csv('/Users/viviandang/Desktop/Nuage Training/pokemon_data.csv')

(df.head(3))

#See headers
(df.columns)

#Read each column that is specified (all data)
(df['Name'])
(df[['Name', 'Type 1', 'HP']])

#iloc integer location? 
(df.iloc[1:4]) #prints from index 1-4
(df.iloc[2,1]) #prints from index 2, 1 row

df.loc[df['Type 1']=='Grass']   # prints all columns and rows where type 1 = grass
new_df = (df.loc[(df['Type 1'] == 'Grass') | (df['Type 1'] == 'Poison')])

df.describe #shows standard deviation and stuff
(df.sort_values(['Type 1', 'HP']))  #sorts by type and hp, can also do ascending/descending

#____________________________________________________
#creating new column (doesn't actually modify your data)
df['Total'] = df['HP'] + df['Attack']   #+...
df.head(5)
#can also be rewritten as:
df['Total'] = df.iloc[:, 4:10].sum(axis=1)  #using columns 4 to 10 to sum
df.head(5)


#reset df by redefining 'df...' to 'df = df...'
df = df.drop(columns = ['Total'])

#Updating csv
#df.to_csv('modified.csv', index=FALSE);
#df.to_csv('modified.txt', index=FALSE, sep='\t');  tab delimiter

#new_df.to_csv('filtered_pokemon.csv')
#can reset index too (saves old index numbers)
#new_df.reset_index()
#new_df.reset_index(drop=True, inplace=True)

#filter by string, can also use regex 
#df.loc[df['Name'].str.contains('Mega')] #find string "Mega" in name column
#df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)] #name begins with pi

#Ignore capitalization with flags
#df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]

#Conditional Changes
#Change fire type to flamer
#df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
#Change all fire type to legendary
#df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True