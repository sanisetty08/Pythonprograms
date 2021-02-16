# coding: utf-8

# In[43]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'

# In[44]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Customers\"")
srinurow = connection.execute(MyQuery).fetchall()

MyQuery2 = text("SELECT * FROM \"Address\"")
srinurow2 = connection.execute(MyQuery2).fetchall()

# In[45]:

import pandas as pd

data_df = pd.DataFrame(srinurow)
data_df2 = pd.DataFrame(srinurow2)

data_df.columns = ['customer_id', 'store_id', 'first_name', 'last_name',
                   'email', 'address_id', 'activebool', 'create_date', 'last_update', 'active', 'order_amount']
data_df2.columns = ['address_id', 'address', 'address2', 'district', 'city_id', 'postal_code', 'phone', 'last_update']
# print(data_df)
# print(data_df.type)
# drop the null values
# data_df = data_df.dropna(how='any')
# reset index after dropping
# data_df = data_df.reset_index(drop= True)
# view the top results
# data_df


# In[50]:

df1 = data_df[['customer_id', 'first_name', 'last_name', 'email', 'address_id', 'order_amount']]
# data_df.columns = ['customer_id','first_name', 'last_name', 'mail', 'address_id','order_amount']
top10customerDF = df1.head(10)

# In[48]:

data_df2

# In[69]:

top10customersAddressDF = pd.merge(top10customerDF, data_df2, on='address_id', how='inner')

# selecting rows based on condition 
top10customersAddressDFfilter = top10customersAddressDF[(top10customersAddressDF['first_name'] == 'Carlos')]

# to identify duplicates - method1
# len(pd.unique(top10customersAddressDF['first_name']))
# to identify duplicates - method2
# top10custgroupedDF = top10customersAddressDFfilter.groupby('first_name').first()
# top10custgroupedDF.loc[:,'order_amount'].sum()
resultDF = top10customersAddressDF.groupby(['first_name', 'last_name', 'district', 'address', 'phone'])[
    'order_amount'].sum().reset_index()
# testing
# resultDF['first_name'][0]
# len(resultDF)


# In[76]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres_dest'

# In[82]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="AUTOCOMMIT")

# simplified insertion code

resultDF.to_sql('CustomerReport', engine, if_exists='replace')

# from sqlalchemy import Boolean
# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
# metadata = MetaData()
# CustomerReport = Table('CustomerReport', metadata,
# Column('first_name', String),
# Column('last_name', String),
# Column('district', String),
# Column('address', String),
# Column('phone', Boolean),
# Column('order_amount',String)
#    )

# for i in range(len(resultDF)):
# ins = CustomerReport.insert().values(first_name=resultDF['first_name'][i],last_name=resultDF['last_name'][i],
# district=resultDF['district'][i],address=resultDF['address'][i],
# phone=resultDF['phone'][i],order_amount=resultDF['order_amount'][i])

# connection.execute(ins)


connection.close()
