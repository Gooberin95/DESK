import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Create connection string

engine = create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server")

try:
    with engine.connect() as conn:
        print("We have connected successfully")
except Exception as e:
    print(f"An error has occured...{e}")


def select_all():
    try:
        query = "SELECT * FROM Homes"
        df = pd.read_sql(query, engine)
        print(df)
    except Exception as e:
        print(f"An error has occurred {e}")

select_all()


def insert_into_excel():
    try: 
        query = "SELECT * FROM Homes"
        df = pd.read_sql(query, engine)
        df.to_excel("Testing.xlsx", index=False)
        print("The table data has been saved into an Excel file")
    except Exception as e:
        print(f"An error has occurred... {e}")


insert_into_excel()


def replace_table_data():

    csv_file_path = r"C:\\Users\\Sober\\Downloads\\tesla_stock_data_2000_2025.csv"

    df = pd.read_csv(csv_file_path)
    try:
        df.to_sql("Homes", con=engine, if_exists="replace", index=False )
        print("Tabel data has been replaced")
    except Exception as e:
        print(f"An error as occured...{e}")
    

