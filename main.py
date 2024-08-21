from fastapi import FastAPI, HTTPException
import pandas as pd
import sqlalchemy as db
from sqlalchemy import text
from sqlalchemy import *


app = FastAPI()

# Create an engine and connect to the database
engine = create_engine('mysql+mysqlconnector://root:MysqlRoot%40133@localhost/transaction_data', pool_size = -1, max_overflow = -1)
conn = engine.connect()
metadata = MetaData()

# table_dict = {
#        "Country" : 'country_table',
#        "Customer" : 'customer_table'
#         }

@app.post("/insights")
async def main(Country_or_Customer: str, column_name:str, ide:str):
        if(Country_or_Customer == "Country"):
                # table = Table('country_table', metadata, autoload_with=engine)
                # query = select([table.c[column_name]]).where(table.c["Country"] == ide) # type: ignore
                # query = text(f"SELECT text{Revenue_max_Sep} FROM text{Country} WHERE text{Country}== text{Australia}")
                query = text(""" SELECT {column_name} 
                        FROM country_table 
                        WHERE  country_table.Country = "{ide}" """)
                
        else:
                # table = Table('customer_table', metadata, autoload_with=engine)
                # # Define the query
                query = text(""" SELECT {column_name} 
                        FROM customer_table 
                        WHERE  customer_table.UserId = "{ide}" """)

        
        output  = conn.execute(query)
        results =output.scalars().all()[0]
        print(results)
        return results
        # results = output.fetchall()
        # print(results)
        # return results
       
        # # Check if a result was found
        # if results:
        #         print(results[0])  
        # else:
        #         print("No record found.")


       
        # print(type(results))
        # return {i:x for i,x in enumerate(results) }

    