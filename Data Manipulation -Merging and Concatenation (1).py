#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


df1 = pd.read_csv('LOTR.csv')
df1


# In[7]:


df2 = pd.read_csv('LOTR 2.csv')
df2


# In[15]:


#merge; used in merging two or more data frames together.
#the merge does an inner join
#it merges data that are marge each other

df1.merge(df2, how = 'inner', on = ['FellowshipID', 'FirstName'] )


# In[22]:


#outer join, it gives out all the values


df1.merge(df2, how = 'outer')


# In[23]:


#left join, returns everything in the left join and only data in the right joins that marches the left join.

df1.merge(df2, how = 'left')


# In[25]:


#right join, is the excat opposite of the left join.

df1.merge(df2, how = 'right')


# In[28]:


#cross join, it takes each value in left data frame and compare with each value in the right data frame.


df1.merge(df2, how = 'cross')


# In[ ]:





# #### Concanate

# In[30]:


#Concanate puts dataframe on top of each other not like the merge and join that puts dataframe side by side to each other.

pd.concat([df1, df2])


# In[37]:


#putting the join function to the concatenate



pd.concat([df1, df2], join = 'outer', axis = 1)


# In[32]:


pd.concat([df1, df2], join = 'inner')


# In[ ]:





# In[ ]:





# In[ ]:




