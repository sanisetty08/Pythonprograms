# coding: utf-8

# In[1]:

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'

# In[2]:

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
connection = engine.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

from sqlalchemy.sql import text

MyQuery = text("SELECT * FROM \"Customers\"")
srinurow = connection.execute(MyQuery).fetchall()
# print(srinurow)


# In[3]:

# for i in srinurow:
# print(srinurow)
for i in range(len(srinurow)):
    # print("{}. {}".format(i , a[i]))
    print("{}. {}".format(i + 1, srinurow[i]))

# In[ ]:

for i in range(len(srinurow)):
    ins = Load2table.insert().values(customer_id=srinurow[i][0], store_id=srinurow[i][1], first_name=srinurow[i][2],
                                     last_name=srinurow[i][3],
                                     email=srinurow[i][4], address_id=srinurow[i][5], activebool=srinurow[i][6],
                                     create_date=srinurow[i][7],
                                     last_update=srinurow[i][8], active=srinurow[i][9], phone_number=srinurow[i][10])
