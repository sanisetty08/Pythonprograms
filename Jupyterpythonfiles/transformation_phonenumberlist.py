# coding: utf-8

# In[ ]:

# transformation2-use list to add phone number with value 9000903798


# In[9]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'

# In[10]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Customers\" where address_id = 5 AND customer_id = 1")
srinurow = connection.execute(MyQuery).fetchone()
# print(srinurow)
# type(srinurow)
# for i in srinurow:
# print(i)
# for i in range(len(srinurow)):
# print(i)


# In[11]:

# purpose1: copy database rowproxy(srinurow) to srinulist because we cannot modify rowproxy values

# step1:initialization of new list
srinulist = []
# step2: copy from srinurow to srinulist(here on awards we dont need srinurow any more)
for i in range(len(srinurow)):
    srinulist.append(srinurow[i])
# step3:here we are appending the phone number to the list
myphone_number = '9000903798'
srinulist.append(myphone_number)
print(srinulist)

connection.close()

# In[12]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres_dest'

# In[15]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="AUTOCOMMIT")

from sqlalchemy import Boolean
from sqlalchemy import Table, Column, Integer, BigInteger, String, MetaData

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
                   Column('active', Integer),
                   Column('myphone_number', BigInteger)
                   )

ins = Load2table.insert().values(customer_id=srinulist[0], store_id=srinulist[1], first_name=srinulist[2],
                                 last_name=srinulist[3],
                                 email=srinulist[4], address_id=srinulist[5], activebool=srinulist[6],
                                 create_date=srinulist[7],
                                 last_update=srinulist[8], active=srinulist[9], myphone_number=srinulist[10])

connection.execute(ins)
connection.close()

# In[ ]:
