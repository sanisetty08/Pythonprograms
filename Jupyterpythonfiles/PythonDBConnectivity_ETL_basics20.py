# coding: utf-8

# In[10]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'

# In[11]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Customers\"")
srinurow = connection.execute(MyQuery).fetchall()
# print(srinurow)
# type(srinurow)


# In[15]:

import pandas as pd

df = pd.DataFrame(srinurow)
print(df.head())

# from pandas import DataFrame
# People_List = srinurow
# df = DataFrame (People_List,columns=['customer_id', 'store_id','first_Name', 'last_nmae','email', 'address_id','activebool',
# 'create_date' ,'last_update','active' ])
# print(df.head())

# a = srinurow[0]
# b = a
# c = a * b
# d = c
# e = d - a
# print(e)
connection.close()

# In[35]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres_dest'

# In[36]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="AUTOCOMMIT")

from sqlalchemy.sql import text

MyQuery = text("INSERT INTO \"load1\" VALUES(:incomingvalue)")
connection.execute(MyQuery, incomingvalue=e)
