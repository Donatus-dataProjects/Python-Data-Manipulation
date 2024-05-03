#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Handling null values we can use the following ways
#1. fill the null values with some values
#2. Drop such rows
#3. Either replace them


# In[ ]:


#methods of replacing them


# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('Bengaluru_House_Data.csv')
df


# In[3]:


#checking the first 5 rows
df.head(5)


# In[4]:


#analysing the dataset using the .shape 
df.shape


# In[5]:


#to check if it has a null values
df.isnull()
#all values showine True means the value in the cell is null value and False is a value


# In[6]:


#to know the total value of each column
df.isnull().sum()


# In[7]:


#sum of the whole column
df.isnull().sum().sum()


# ## Filling null values

# In[8]:


#using the function fillna() to replace a missing value
#you canreplace a missing value with any value
# e.g replacing it with 5
df2 = df.fillna(value = 5)
df2


# In[9]:


#checking if df2 still has a null value
df2.isnull().sum().sum()


# In[10]:


#replacing the missing value with 9
df3 = df.fillna(value = 9)
df3


# ### Filling Null values with a previous value 

# In[11]:


# using the pad method
df4 = df.fillna(method = 'pad')
df4


# In[12]:


#checking for null values in df4
df4.isnull().sum()

#no Null values becaue it was replaced using the method 'pad' which replaces Null values with previous values


# In[13]:


df


# ### Filling the Null values with the next value

# In[14]:


#this method uses the next value after the null value to replace the null value 'backward fill' in short form 'bfill'
df5 = df.fillna(method = 'bfill')
df5

#When using this method if the last row in the dataset has a Null value it will remain Null 
#because this method uses the value after the Null value to replace the Null+


# ### Filling missing values with the previous values column wise

# In[15]:


# what this method means is filling Null values with the previous values in the previous or next rows.
#using the previous row to fill the Null values
df6 = df.fillna(method = 'pad', axis = 1)
df6


# In[16]:


#using the 'backwardfill' 'bfill' row to fill it
df6 = df.fillna(method = 'bfill', axis = 1)
df6


# In[17]:


df


# ### Filling Null values of each column with a  different value

# In[18]:


#so each column that has a Null value will be replace with a different value.

df7 = df.fillna({'society': 'Victor', 'balcony': 'number'})
df7


# ### Filling Null value with the mean, max or min of the column

# In[19]:


#the mean of the specified column will be used to replace the Null value.

df8 = df.fillna(value = df['balcony'].mean())
df8


# In[20]:


#using the maximum function to fill the Null value.

df9 = df.fillna(value = df['balcony'].max())
df9


# In[21]:


#using the mean function
df10 = df.fillna(value = df['balcony'].min())
df10


# ## Droping columns in a dataset 

# In[23]:


df


# In[25]:


##droping rows with null value

df12 =df.dropna()
df12


# In[26]:


#using the 'how'
#any - it means parameter if any cell in the row is enull that row will be drop.
#all -  parameter if all the values in the row is null then that row will be deleted.

#using any it will drop all the records that have null values
df13 = df.dropna(how = 'any')
df13



# In[28]:


#using the all parameter.
#it won't work on this dataset because we don't have the entire row to be null
df14 = df.dropna(how = 'all')
df14


# ### Using the replace function

# In[29]:


#using the replace to replace null values
#N/B numpy contains an object for Null values
import numpy as np


# In[30]:


df15 = df.replace(to_replace = np.nan, value = 'missing-value')
df15


# In[31]:


#you can also replace a value using the 'replace' function

df16 = df.replace(to_replace = 'Soiewre', value = 'India')
df16


# ## Interpolate()

# In[36]:


#it interpolates value an automatically fill the NaN value. e.g below
#it will interpolate the values and replace the 'nan' with 5

1
2
3
4
nan
6
7


# ## methods in interpolation
# 

# In[35]:


#linear method
#it will fill the null value with the mean of the two numbers

5
#nan    #The mean is 5.5
6




# In[37]:


#using the linear method
df['balcony'] = df['balcony'].interpolate(method = 'linear')
df

#the null value in row 13316 has been replaced with  0.5


# In[39]:


df['balcony'] = df['balcony'].interpolate(method = 'linear', limit_direction = 'forward')
df


# In[ ]:





# In[ ]:




