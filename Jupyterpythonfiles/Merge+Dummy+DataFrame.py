# coding: utf-8

# In[2]:

import pandas as pd

# create dummy data
df_a = pd.DataFrame({
    'subject_id': ['1', '2', '3', '4', '5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']})

df_b = pd.DataFrame({
    'subject_id': ['4', '5', '6', '7', '8'],
    'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']})

df_c = pd.DataFrame({
    'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
    'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]})

# In[3]:

pd.merge(df_a, df_c, on='subject_id')

# In[4]:

# Merge outer join
pd.merge(df_a, df_b, on='subject_id', how='outer')

# In[5]:

# merge with inner join
pd.merge(df_a, df_b, on='subject_id', how='inner')

# In[6]:

# merge with right join
pd.merge(df_a, df_b, on='subject_id', how='right')

# In[7]:

# merge with left join
pd.merge(df_a, df_b, on='subject_id', how='left')

# In[ ]:
