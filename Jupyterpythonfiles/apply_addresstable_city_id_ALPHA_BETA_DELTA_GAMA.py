# coding: utf-8

# In[2]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'

# In[3]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Address\"")
srinurow = connection.execute(MyQuery).fetchall()
# print(srinurow)


# In[4]:

import pandas as pd

data_srinurow = pd.DataFrame(srinurow)
data_srinurow.columns = ['address_id', 'address', 'address2', 'district', 'city_id', 'postal_code', 'phone',
                         'last_update']
# data_srinurow
# accessing row wise
data_srinurow.apply(lambda x: x)

# In[5]:

# access first row
data_srinurow.apply(lambda x: x[0])

# In[6]:

# access first column by index
data_srinurow.apply(lambda x: x[0], axis=1)

# In[7]:

# access by column name
data_srinurow.apply(lambda x: x["address"], axis=1)[:5]

# In[28]:

# import pandas as pd
# data_srinurow = pd.DataFrame(srinurow)
# data_srinurow.apply(lambda x: x)
# data_srinurow.columns = ['address_id', 'address', 'address2', 'district', 'city_id', 'postal_code', 'phone', 'last_update']


# In[8]:

# before clipping
data_srinurow["city_id"][:5]


# In[9]:

# clip city_id if it is greater than 0 and less than equat to 100
def clip_city_id(city_id):
    if city_id > 0 and city_id <= 100:
        city_id = "ALPHA"
        return city_id


# after clipping
data_srinurow["city_id"].apply(lambda x: clip_city_id(x))[:100]


# In[10]:

# clip city_id2
def clip_city_id(city_id):
    if city_id > 0 and city_id <= 100:
        city_id = "ALPHA"
    elif city_id > 100 and city_id <= 300:
        city_id = "BETA"
    elif city_id > 400 and city_id <= 500:
        city_id = "DELTA"
    else:
        city_id = "GAMA"
    return city_id


state_output = data_srinurow["city_id"].apply(lambda x: clip_city_id(x))[:100]
# state_output.rename(columns = {'city_id':'state'}, inplace = True)
# print(state_output)
# print(data_srinurow)
# result = pd.merge(data_srinurow,pd.DataFrame(state_output), on='city_id', how='right')
# result
# pd.merge(data_srinurow, pd.DataFrame(state_output))
# type(pd.DataFrame(state_output))
# type(data_srinurow)
result = pd.concat([data_srinurow, pd.DataFrame(state_output)], axis=1)
result.columns = ['address_id', 'address', 'address2', 'district', 'city_id', 'postal_code', 'phone', 'last_update',
                  'state']
pd.DataFrame(result)


# In[ ]:

# clip city_id2
def clip_city_id2(city_id):
    if city_id > 0 and city_id <= 100:
        city_id = "ALPHA"
    elif city_id > 100 and city_id <= 300:
        city_id = "BETA"
    elif city_id > 400 and city_id <= 500:
        city_id = "DELTA"
    else:
        city_id = "GAMA"
    return city_id


# data_srinurow["city_id"].apply(lambda x: clip_city_id2(x)) [:100]
data_srinurow
