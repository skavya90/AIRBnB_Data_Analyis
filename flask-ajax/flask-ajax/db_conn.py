import pandas as pd
from sqlalchemy import create_engine
from config import password

finalairbnba_df = pd.read_csv("../../cleaned_listings.csv")

rds_connection_string = f'root:{password}@localhost:3306'
engine = create_engine(f'mysql+pymysql://{rds_connection_string}')

engine.execute("CREATE DATABASE airbnbaustin_db") #create db
engine.execute("USE airbnbaustin_db")

finalairbnba_df.to_sql(name='finalairbnba_data', con=engine, if_exists='append', index=False)