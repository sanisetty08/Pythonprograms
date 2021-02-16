# coding: utf-8

# In[6]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'

# In[7]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Coronavirus\"")
srinurow = connection.execute(MyQuery).fetchall()

# In[8]:

import pandas as pd

# read the data set
data_df = pd.DataFrame(srinurow)
data_df.columns = ['Country', 'TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered',
                   'ActiveCases', 'SeriousCases', 'TotalCasesPM', 'DeathsPM', 'TotalTests', 'TestsPM', 'Population']
data_df

# In[15]:

data_df = pd.DataFrame(['SeriousCases', 'NewCases'])['Population'].sum().reset_index()
data_df
