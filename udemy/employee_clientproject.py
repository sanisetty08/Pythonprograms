import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# establishing connection to postgres
PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/Miracle'
engine = create_engine(PostgresDB_URI)
connection = engine.connect()
read_connection = connection.execution_options(isolation_level="READ COMMITTED")

# extracting data from postgres
MyProject = text("SELECT * FROM \"Development\".\"Project\"")
projectrow = read_connection.execute(MyProject).fetchall()
# print(projectrow)

MyResource = text("SELECT * FROM \"Development\".\"Resource\"")
resourcerow = read_connection.execute(MyResource).fetchall()
# print(resourcerow)

MyClient = text("SELECT * FROM \"Sales\".\"Client\"")
clientrow = read_connection.execute(MyClient).fetchall()
# print(clientrow)

# transfromation
pd.set_option('display.max_columns', None)

project_df = pd.DataFrame(projectrow)
project_df.columns = ['project_id', 'project_name', 'client_id', 'project_details', 'load_timestamp']
# print(project_df)

resource_df = pd.DataFrame(resourcerow)
resource_df.columns = ['resource_id', 'first_name', 'last_name', 'phone_number', 'project_id', 'salary',
                       'load_timestamp']

client_df = pd.DataFrame(clientrow)
client_df.columns = ['client_id', 'client_name', 'client_contact', 'industry', 'project_name', 'client_location',
                     'client_phonenumber', 'load_timestamp']

pro_res_df = pd.merge(project_df, resource_df, on=['project_id'], how='inner')
# print(tabulate(df1, headers='keys', tablefmt='psql'))

pro_res_cli_df = pd.merge(client_df, pro_res_df, on=['client_id'], how='inner')
# print(tabulate(df2, headers='keys', tablefmt='psql'))

myresult = pro_res_cli_df[['first_name', 'last_name', 'client_name', 'project_name_x']]
myresult.rename(index=str, columns={"project_name_x": "project_name"}, inplace=True)
# print(tabulate(myresult, headers='keys', tablefmt='psql'))

# loading to postgres
PostgresDB_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/Reporting_database'

from sqlalchemy import create_engine

engine = create_engine(PostgresDB_URI)
write_connection = engine.connect()
load_connection = write_connection.execution_options(isolation_level="AUTOCOMMIT")

myresult.to_sql('pro_res_cli', engine, if_exists='replace')

connection.close()
