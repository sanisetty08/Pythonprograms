# coding: utf-8

# # Extract

# In[7]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'

# In[8]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Customers\" where address_id = 5 AND customer_id = 1")
srinurow = connection.execute(MyQuery).fetchone()
print(srinurow)

# In[13]:

# type(srinurow)


# # Transformation

# In[10]:

# taking control of individual fields within a row
# print(srinurow[0],srinurow[1],srinurow[2],srinurow[3],srinurow[4],srinurow[5],srinurow[6],srinurow[7],srinurow[8],srinurow[9])
# print(srinurow[0:9])

# assigning variables
python_customer_id = srinurow[0]
store_id = srinurow[1]
first_name = srinurow[2]
last_name = srinurow[3]
email = srinurow[4]
address_id = srinurow[5]
activebool = srinurow[6]
create_date = srinurow[7]
last_update = srinurow[8]
active = srinurow[9]
# print(customer_id, store_id, first_name, last_name,email, address_id, activebool, create_date, last_update, active)
# what if I have 1000 columns - for loop
# print(first_name)
# changing first_name from Mary to Lori

# transformation1-changing name from Mary to Lory
first_name = 'Lory'

connection.close()
print(first_name)
# print(customer_id, store_id, first_name, last_name,email, address_id, activebool, create_date, last_update, active)


# # Load

# In[46]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres_dest'

# In[34]:

# Old Fashioned code
# from sqlalchemy import create_engine
# engine = create_engine(PostgresDB_URI)
# connection = engine.connect()
# connection = connection.execution_options(isolation_level="AUTOCOMMIT")

# from sqlalchemy.sql import text
# MyQuery = text("INSERT INTO \"load2\" VALUES(:incomingvalue0,:incomingvalue1,:incomingvalue2,:incomingvalue3,:incomingvalue4,:incomingvalue5,:incomingvalue6,:incomingvalue7,:incomingvalue8,:incomingvalue9)")
# connection.execute(MyQuery,incomingvalue0=customer_id,incomingvalue1=store_id,incomingvalue2=first_name,incomingvalue3=last_name,incomingvalue4=email,incomingvalue5=address_id,incomingvalue6=activebool,incomingvalue7=create_date,incomingvalue8=last_update,incomingvalue9=active)
# connection.close()


# In[47]:

# New Fashioned Code
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

ins = Load2table.insert().values(customer_id=python_customer_id, store_id=store_id, first_name=first_name,
                                 last_name=last_name,
                                 email=email, address_id=address_id, activebool=activebool, create_date=create_date,
                                 last_update=last_update, active=active)

connection.execute(ins)
connection.close()

# In[ ]:
