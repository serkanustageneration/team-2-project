# run elt
from table_script import create_table
import extract as ex
import pandas as pd
import load_drop_dupe_db as ldd
import load_basket as ba


def run_etl_main(df):

    # create tables
    create_table()

    #transformation cust, prods, stores
    customer_df = ex.unique_customers_table(df)
    products_df = ex.create_products_df(df)
    store_df = pd.DataFrame(df['store'].unique(), columns=['store'])

    #remove dupes and load first three tables
    ldd.load_store(store_df)
    ldd.load_product(products_df)
    ldd.load_customer(customer_df)

    #transform basket
    basket_df = ba.create_basket_df(df)
    order_df = ba.create_orders_df(df)

    #Get id columns from order_df for basket_df
    customer_id = order_df['cust_id']
    store_id = order_df['branch_id']
    #Get timestamp from raw data df
    time_stamp = df['timestamp']

    #Create new columns in basket_df
    basket_df['customer_id'] = customer_id
    basket_df['store_id'] = store_id
    basket_df['time_stamp'] = time_stamp

    #load basket
    ba.execute_values(basket_df, 'basket_table')
