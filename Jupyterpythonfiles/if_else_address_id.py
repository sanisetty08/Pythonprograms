# coding: utf-8

# In[ ]:

# transformation5-use if else statement to verify address id = 530 then change to 5300 or else leave it as old


# In[1]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'

# In[5]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Customers\" WHERE address_id=530")
srinurow = connection.execute(MyQuery).fetchone()
print(srinurow)

# In[12]:

address_id = '500'
if (address_id == 530):
    print(address_id)
else:
    print(530)
