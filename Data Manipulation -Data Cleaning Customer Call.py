#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd


# In[64]:


df= pd.read_excel('Customer Call List.xlsx')
df


# In[65]:


#drop duplicates
df.drop_duplicates()


# In[111]:


#removed unwanted columns 
df.drop(columns = 'Not_Useful_Column')
df


# In[75]:


#removing symbols from names


#df['Last_Name'] = df['Last_Name'].str.lstrip('.../_')  #from left side

#df['Last_Name'] = df['Last_Name'].str.rstrip('.../_')   #from right side

df['Last_Name'] = df['Last_Name'].str.strip('123./_')
df['Last_Name']
df


# In[ ]:


#how to clean phone numbers


# In[ ]:


#


# In[116]:


#how to work on address (cleaning)

#df['Address'].str.split(',', n = 1 expand = True)   #1 reps how many values from left to right it should look for

#df[['Address1'] = 
df[['Stress_Address', 'State', 'Zip_Code']] = df['Address'].str.split(',', n=2, expand=True)

df[['Stress_Address', 'State', 'Zip_Code']]
df


# In[ ]:


#In python difference between #() and []

# how to clean phone number


# In[120]:


#replacing values 
#replace Yes = Y 
#replace No = N

df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y')

df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N')

df


# In[131]:


#replacing some values
#df = df.replace('N/a', '')
df.fillna('')


# In[ ]:


#In python difference between #() and []

# how to clean phone number
#How to remove NaN#lamda function


# In[ ]:





# In[ ]:




