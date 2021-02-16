# coding: utf-8

# In[ ]:

# transformation3-use dictionary to add middle name with value sontenam


# In[1]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'

# In[3]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Customers\" where address_id = 5 AND customer_id = 1")
srinurow = connection.execute(MyQuery).fetchone()
print(srinurow)

# In[17]:

my_dictionary = {'middle_name': 'Sontenam'}
print(my_dictionary['middle_name'])
