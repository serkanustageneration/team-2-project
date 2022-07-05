## imports ##
#from this import s
import pandas as pd
import hashlib
import psycopg2


def df_connect():
    hostname = 'localhost'
    database = 'team-2_group-project'
    username = 'root'
    pwd = 'pass'

    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd
        )
        return conn
    except Exception as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
        # if conn is not None:
        #     conn.close()


conn = df_connect()
cur = conn.cursor()

#reading csv
FIELDNAMES = ['timestamp', 'store', 'customer_name',
              'basket_items', 'total_price', 'cash_or_card', 'card_number']

# Need to connect this to s3 bucket somehow.
FILENAME = r'csv\chesterfield_11-06-2022_09-00-00.csv'

data = pd.read_csv(FILENAME, names=FIELDNAMES)


## hashing values function
def hash_value(x):
    """
    - Hashes x with hashlib.sha256
    """
    if x != 'nan':
        return hashlib.sha256(x.encode()).hexdigest()
    else:
        return None

# creating Clean customers_table **hashed**
def unique_customers_table():
    unhashed_cus_df = data[["customer_name", "card_number"]].drop_duplicates()
    hashed_cus_df = unhashed_cus_df.applymap(lambda x: hash_value(str(x)))
    return hashed_cus_df


### Transform basket  ###
def fetch_products():
    """
    - Returns a df with all products and details in the raw data
    - Must be transformed
    """
    #Split the basket_items col so that each row is a list
    items_series = data['basket_items'].apply(lambda x: x.split(", "))
    
    #Load this pd.Series object into a pd.DataFrame. Unwanted column - dropped after transformation
    products_df = pd.DataFrame(items_series, columns=['basket_items'])

    #Explode contents of each order so that every item in an order is a separate row in the df
    products_df = products_df.explode('basket_items')

    return products_df


## creating products function


def create_products_df():
    """
    - Returns a df which transforms the unique products and details
    """
    products_df = fetch_products()

    #Get unique products
    products_df = products_df.drop_duplicates(ignore_index=True)

    product_names, product_flavours, product_prices = [], [], []

    for product in products_df['basket_items']:
        details = product.split(' - ')
        #Append name and price (always first and last elements of details)
        product_name = f'{details[0]}'
        product_names.append(product_name)

        product_price = f'{details[-1]}'
        product_prices.append(product_price)

        #Handle flavours
        if 'Flavoured' in product:
            #Append flavour
            product_flavour = f'{details[1]}'
            product_flavours.append(product_flavour)
        else:
            #Append 'Original'
            product_no_flavour = f'Original'
            product_flavours.append(product_no_flavour)

    #Populate products_df with new columns
    products_df['product_name'] = product_names
    products_df['product_flavour'] = product_flavours
    products_df['product_price'] = product_prices

    #Drop unwanted column
    products_df = products_df.drop('basket_items', axis=1)
    return products_df


#Fetch conn and cursor objects
conn = df_connect()
cur = conn.cursor()
### dataFrame ###
customer_df = unique_customers_table()
products_df = create_products_df()
store_df = pd.DataFrame(data['store'].unique(), columns=['store'])
