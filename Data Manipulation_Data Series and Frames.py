#!/usr/bin/env python
# coding: utf-8

# # Pandas DataFrames

# In[ ]:


#DataFrame is a 2 dimensional structure.


# In[ ]:


#pandas series is a one dimentional array


# In[6]:


import pandas as pd
import numpy as np


# In[2]:


#how to form pandas data series.
#this can be done through the 
#1. series or  2. dictionary by having keys and values


# In[3]:


#how to create pandas series which is one dimensional data object in pandas used to build up to 2 dimensional


# In[7]:


my_series = pd.Series(data  = [2, 3, 4, 5, 6],
                     index = ['a', 'b', 'c', 'd', 'e'])

my_series


# In[31]:


#slicing your series
my_series [1:4]


# In[19]:


#creating a series using a dictionary
#It is one dimensionna
dict = {'x': 2, 'a': 5, 'b': 4, 'c': 8}
result = pd.Series(dict)
result


# In[22]:


colorz = {'red': 2, 'blue': 4, 'red': 5, 'purple': 3, 'yellow': 6, 'pink': 9}
colorz = pd.Series(colorz)
colorz


# # Data Frame starts here

# In[ ]:


#data frame is a 2 dimentional table with labeled columns that can each hold differet data types.
#N/B you can create a dataframe using a dictionary.
#Datas must be the same rows or it will fill the rows with same data


# In[14]:


my_dict = {'data': [2, 3, 4, 5, 6],
          'index': ['a', 'b', 'c', 'd', 'e']}
my_dict = pd.DataFrame(my_dict)
my_dict


# In[16]:


#creating series using a dictionary
names = {'name': ['Cosmos', 'Wills', 'Don', 'Victor'],
        'course': ['Postgres', 'CSS', 'Python', 'Excel']}
names = pd.DataFrame(names)
names


# In[39]:


names.course


# In[13]:


#how to form pandas data series.
#this can be done through the series or dictionary by having keys and values

my_series = pd.Series(data = ['excel', 'power bi', 'sql', 'python', 'java'],
                    index = [1, 2, 3, 4, 5])

my_series


# In[16]:


cources =  ['excel', 'power bi', 'sql', 'python', 'java'] 
grade = [80, 87, 97, 85, 90]


# In[19]:


resultsheet = {'cources': ['excel', 'power bi', 'sql', 'python', 'java'],
               'grade': [80, 87, 97, 85, 90]}

resultsheet


# In[20]:


resultsheet=pd.DataFrame(resultsheet)
resultsheet


# In[53]:


#creating a dictionary with some different data types

new_dict = { 'name': ['Joe', 'Bob', 'Francis'],
           'age': np.array ([10, 15, 20]),
           'weight': (75, 123, 239),
           'height': pd.Series ([4.5, 5, 6.1],
                                index = ['Joe', 'Bob', 'Francis']),
           'siblings': 1,
            'gender': 'M'}

df = pd.DataFrame(new_dict)
df

#note that the index column was specified because one of the data columns was in series.
#thats the reason thams was used as index.


# In[ ]:


#the example below does not have a pandas series 


# In[58]:


dict2 = { 'name': ['Joe', 'Bob', 'Francis'],
           'age': np.array ([10, 15, 20]),
           'weight': (75, 123, 239),
           'height': [4.5, 5, 6.1],
           'siblings': (1, 5, 3),
            'gender': 'M'}

df = pd.DataFrame(dict2)
df

#in the result below the data frame automatically used the numbers as the index 


# In[59]:


#to delete a column

del df['gender']


# In[60]:


df


# In[62]:


#to add new column

df['sex'] = ['M', 'F', 'M']
df


# In[66]:


#adding new column with same word throughout the column
df['status'] = 'married'
df


# In[70]:


df.loc


# In[73]:


#to access rows and clumns by index values
df.iloc[0]


# In[74]:


df.iloc[1]


# In[75]:


df.iloc[2]


# In[81]:


#using the boolean index to know which row is true
#N/B you must specify the entire length of the row

boolean_index = [False, True, True]
df[boolean_index]


# In[ ]:





# In[ ]:


#N/B to know the size of your data 
dataname.shape


# In[ ]:


#to see the head
dataname.head()

#for tail

dataname.tail()


# In[ ]:


#to create index for your data if there was no index
dataname.index = dataname['age']      #'age' is one of the column in your data set
del dataname.['age']                  #the column you are using as an index should be deleted from the columns
print (dataname.index[0:10])        #where [0:10] are the first 10 rows


# In[ ]:


dataname.describe summarize the numeric columns for you such as mean, std, max etc


# In[ ]:


#it gives you the data type and memory

dataname.info 


# In[ ]:





# In[ ]:





# In[ ]:




