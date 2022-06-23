import psycopg2
import numpy as np
import psycopg2.extras as extras

from extract import *

basket_df = create_basket_df()
order_df = create_orders_df()
customer_id = order_df['cust_id']
store_id = order_df['branch_id']
time_stamp = data['timestamp']

basket_df['customer_id'] = customer_id
basket_df['store_id'] = store_id
basket_df['time_stamp'] = time_stamp  
  
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

execute_values(conn, basket_df, 'basket_df')

