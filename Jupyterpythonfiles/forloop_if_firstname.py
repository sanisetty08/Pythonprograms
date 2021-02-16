# coding: utf-8

# In[ ]:

# transformation6-use for loop to find if first name is Jared and change it to Mared or else leave it as old


# In[2]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'

# In[3]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Customers\" WHERE address_id=530")
srinurow = connection.execute(MyQuery).fetchone()
print(srinurow)

# In[4]:

# first_name=srinurow[2]  #behind the scenes it comes as Jared
for i in range(len(srinurow)):

    if (srinurow[i] == 'Jared'):
        print('Mared')
