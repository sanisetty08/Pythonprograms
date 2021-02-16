# coding: utf-8

# In[3]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'

# In[4]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Customers\"")
srinurow = connection.execute(MyQuery).fetchall()
# print(srinurow)


# In[8]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery2 = text("SELECT * FROM \"Address\"")
srinurow2 = connection.execute(MyQuery2).fetchall()

# In[10]:

import pandas as pd

df_a = pd.DataFrame(srinurow)
df_b = pd.DataFrame(srinurow2)

# In[16]:

df_a.columns = ['customer_id', 'store_id', 'first_name', 'last_name', 'email', 'address_id', 'active bool',
                'create_date', 'last_update', 'active']
df_a.columns
# df_a


# In[13]:

df_b.columns = ['address_id', 'address', 'address2', 'district', 'city_id', 'postal_code', 'phone', 'last_update']
# df_b.columns
df_b.columns

# In[14]:

pd.merge(df_a, df_b, on='address_id')

# In[ ]:

# Merge outer join
# pd.merge(df_a, df_b, on='address_id', how='outer')
