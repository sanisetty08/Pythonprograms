import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text

PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'
engine = create_engine(PostgresDB_URI)
connection = engine.connect()
read_connection = connection.execution_options(isolation_level="READ COMMITTED")
MyQuery = text("SELECT * FROM \"Customers\" where address_id = 5 AND customer_id = 1")
srinurow = read_connection.execute(MyQuery).fetchall()
# print(srinurow)
# print(type(srinurow))
srinu_df = pd.DataFrame(srinurow)
srinu_df.columns = ['customer_id', 'store_id', 'first_name', 'last_name',
                    'email', 'address_id', 'activebool', 'create_date', 'last_update', 'active', 'order_amount']
srinu_dict = srinu_df.to_dict('dict')  # converting to dictionary
srinu_dictkeys = srinu_dict.keys()  # accessing keys
srinu_values_temp = list(srinu_dict.values())  # accessing values and converting into list

# experimenting dict of dict

# print(type(srinu_values_temp))
# print(srinu_values_temp)

# for loop
# total 11 dictionaries and each dictionary have 1 element
srinu_list = []
for E in srinu_values_temp:
    # discarding keys and only considering values bcoz they are all 0a
    srinu_values_clean = E.values()
    srinu_list.append(srinu_values_clean)
    # print(type(srinu_values_clean))

# print(srinu_dictkeys)
# print(srinu_list)
# x = range(11)
# for n in x:
# print(srinu_dictkeys[n])

# final = {srinu_dictkeys : srinu_list}
# print(final)
# creating empty dict
# srinu_dict2 = {}


#    print(E.values())

connection.close()
