import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
dataset = pd.read_csv('countries of the world.csv')
select_data = dataset.loc[:,['Country','GDP ($ per capita)']]
sorted_data = select_data.sort_values(by='GDP ($ per capita)',ascending=False)
top_ten = sorted_data.iloc[:10]
plt.pie(top_ten['GDP ($ per capita)'], labels=top_ten['Country'])
plt.show()

# the above code plots the GDP shares of top 10 countries 
'''

'''
dataset = pd.read_csv('countries of the world.csv')
select_data = dataset.loc[:,['Country','Area (sq. mi.)','Pop. Density (per sq. mi.)']]

x = np.array(select_data['Pop. Density (per sq. mi.)'])
y = np.array(select_data['Area (sq. mi.)'])
plt.figure(figsize=(50,50))
plt.scatter(x,y)
plt.xlim(0,20)
plt.show()  

#the above code plots the relation between area and population density of the different countries
'''

'''
dataset = pd.read_csv('countries of the world.csv')
select_data = dataset.loc[:,['Country','Area (sq. mi.)']]
    for i in select_data.itertuples():
        if i[2]>3000000:
            print(i[1])
         
#the above code prints out the countries larger in size of 3000000 sq. mi. or more
'''

#print(dataset.describe()) #provides mathematical analysis over the possible sets for easy understanding

#print(dataset.tail(5)) #prints first 5 rows from bottom

#print(dataset.head(5)) #prints first 5 rows from top

#print(dataset.dtypes) #prints all the columns and their datatypes

#print(dataset.shape) #gives # of rows and columns of the dataset

#print(dataset) #prints the dataset in console output


