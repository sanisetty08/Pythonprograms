import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# extablishing connection to postgres
PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/postgres'
engine = create_engine(PostgresDB_URI)
connection = engine.connect()
read_connection = connection.execution_options(isolation_level="READ COMMITTED")

# extracting data from postgres
MyQuery = text("SELECT * FROM \"Employee_table\"")
srinurow = read_connection.execute(MyQuery).fetchall()
# print(srinurow)

# converting to dataframs from list
srinu_df = pd.DataFrame(srinurow)
srinu_df.columns = ['Emp_id', 'first_name', 'last_name', 'dept', 'salary', 'status', 'location', 'country',
                    'load_timestamp', ]

# transformation
try:
    srinu_df['last_name'] = srinu_df['last_name'].str.upper()
except NameError:
    with open('D:\Pysql\Pythonprograms\python_errors/uppercase_1.txt', 'w') as f:
        f.write('last name not found!')
    print('Name not found')
except SyntaxError:
    print('check the syntax')
except Exception as e:
    print(e)
else:
    print('successful')
finally:
    print("The End")
# print(srinu_df)

# mapping to destination fields
python_Emp_id = srinu_df['Emp_id']
python_first_name = srinu_df['first_name']
python_last_name = srinu_df['last_name']
python_dept = srinu_df['dept']
python_salary = srinu_df['salary']
python_status = srinu_df['status']
python_location = srinu_df['location']
python_country = srinu_df['country']
python_load_timestamp = srinu_df['load_timestamp']
# print(python_first_name)

# loading to postgres
PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/Load_database'

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
write_connection = engine.connect()
load_connection = write_connection.execution_options(isolation_level="AUTOCOMMIT")

srinu_df.to_sql('staging_table', engine, if_exists='replace')

connection.close()

# from sqlalchemy import Boolean
# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
# metadata = MetaData()
# Load2table = Table('staging_table', metadata,
#         Column('Emp_id', Integer),
#         Column('first_name', String),
#         Column('last_name', String),
#         Column('dept', String),
#         Column('salary', Integer),
#         Column('status', String),
#         Column('location', String),
#         Column('country',String),
#         Column('load_timestamp',Integer)
#         )
#
# ins = Load2table.insert().values(Emp_id=srinu_df['Emp_id'], first_name=srinu_df['first_name'], last_name=srinu_df['last_name'],
#                                  dept=srinu_df['dept'], salary=srinu_df['salary'], status=srinu_df['status'],location=srinu_df['location'],
#                                 country=srinu_df['country'], load_timestamp=srinu_df['load_timestamp'])
#
# load_connection.close()
# read_connection.close()
