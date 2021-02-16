# coding: utf-8

# In[31]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'

# In[32]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Customers\"")
srinurow = connection.execute(MyQuery).fetchall()

# In[36]:

import pandas as pd

# converting normal table data into data frame
# data_df = pd.DataFrame(srinurow)
# below line is a data from csv
# read the dataset
data_df = pd.read_csv('D:\Pysql\Pythonprograms\Data\customers.csv')
# drop the null values
data_df = data_df.dropna(how='any')
# view the top results
data_df.head(5)

# In[37]:

# sort by address id
sorted_data = data_df.sort_values(by='address_id')
# print sorted data
sorted_data[:5]

# In[38]:

# sort in place and descending order
data_df.sort_values(by='address_id', ascending=False, inplace=True)
data_df[:5]

# In[41]:

# read the data set
data_df = pd.DataFrame(srinurow)
# drop the null values
data_df = data_df.dropna(how='any')

# sort by multiple coloumns
data_df.sort_values(by=[5, 1], ascending=False)
data_df[:5]

# In[42]:

# change the order of Cloumns
data_df.sort_values(by=[5, 1], ascending=False, inplace=True)
data_df[:5]

# In[43]:

data_df.sort_index(inplace=True)
data_df[:5]
