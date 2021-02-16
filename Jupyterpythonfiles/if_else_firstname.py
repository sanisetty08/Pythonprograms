# coding: utf-8

# In[ ]:

# transformation4-use if else statement to verify name = Jared(first name) then change the name to ganesh else leave it as old


# In[37]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'

# In[38]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Customers\" WHERE first_name = 'Jared'")
srinurow = connection.execute(MyQuery).fetchone()
# print(srinurow)


# In[39]:

first_name = 'Sanjay'
if (first_name == 'Jared'):
    print('Ganesh')
else:
    print('Jared')

# In[40]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres_dest'

# In[42]:

mytransformation = first_name
from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="AUTOCOMMIT")

from sqlalchemy import Boolean
from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()
Load2table = Table('load2', metadata,
                   Column('customer_id', Integer),
                   Column('store_id', Integer),
                   Column('first_name', String),
                   Column('last_name', String),
                   Column('email', String),
                   Column('address_id', String),
                   Column('activebool', Boolean),
                   Column('create_date', String),
                   Column('last_update', String),
                   Column('active', Integer)
                   )

ins = Load2table.insert().values(customer_id=python_customer_id, store_id=store_id, first_name=mytransformation,
                                 last_name=last_name,
                                 email=email, address_id=address_id, activebool=activebool, create_date=create_date,
                                 last_update=last_update, active=active)

connection.execute(ins)
connection.close()
