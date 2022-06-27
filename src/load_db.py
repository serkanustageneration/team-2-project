import psycopg2
import numpy as np
import psycopg2.extras as extras

from extract import *
  
  
def execute_values(conn, df, table):
  
    tuples = [tuple(x) for x in df.to_numpy()]
  
    cols = ','.join(list(df.columns))
    # SQL query to execute
    
    
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
  
conn = psycopg2.connect(
    database="team-2_group-project", user='root', password='pass', host='127.0.0.1', port='5432'
)

def run_insert_db():
    execute_values(conn, customer_df, 'customer_df')
    execute_values(conn, products_df, 'products_df')
    execute_values(conn, store_df, 'store_df')


