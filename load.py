from sqlalchemy import create_engine

host = 'localhost'
port = 5432
user = 'postgres'
password = 'walastik'
db_name = 'fakes_store_db'

def load_to_postgres(df, table_name):
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

    df.to_sql(table_name, engine, if_exists = 'replace',index=False)

    print('Data Loaded to postgres successfully')