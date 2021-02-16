# coding: utf-8

# In[1]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'

# In[2]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Customers\"")
srinurow = connection.execute(MyQuery).fetchall()
# print(srinurow)


# In[3]:

import pandas as pd

df1 = pd.DataFrame(srinurow)
df1

# In[31]:

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Customers1\"")
srinurow1 = connection.execute(MyQuery).fetchall()
# print(srinurow1)


# In[32]:

import pandas as pd

df2 = pd.DataFrame(srinurow1)
print(df2)

# In[33]:

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Customers2\"")
srinurow2 = connection.execute(MyQuery).fetchall()

# In[34]:

import pandas as pd

df3 = pd.DataFrame(srinurow2)
print(df3)

# In[35]:

# combine DataFrames
result = pd.concat([df1, df2, df3])
result

# In[39]:

# combine DataFrames
result = pd.concat([df1, df2, df3], keys=['x', 'y', 'z'])
result

# In[40]:

# get second DataFrame
result.loc['y']

# In[52]:

# join Outer
df3 = pd.DataFrame(srinurow2)
result = pd.concat([df1, df3], axis=1)
result

# In[51]:

# join Inner
result = pd.concat([df1, df3], axis=1, join='inner')
result
