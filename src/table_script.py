import psycopg2

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

    cur = conn.cursor()
    
    ## create customer table ## as ** customer_table
    create_customer_table = '''CREATE TABLE IF NOT EXISTS customer_table(
                            customer_id     INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                            customer_name	TEXT,
                            card_number	    text                          
                            );'''
    
    ## create store table ## as ** store_table
    create_store_table = '''CREATE TABLE IF NOT EXISTS  store_table(

                            store_id     INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                            store     	 TEXT
                            );'''
    
    ## create basket table ## as ** basket_table
    create_basket_table = '''CREATE TABLE IF NOT EXISTS  basket_table(
                            order_id         integer,
                            product_id     	 integer,
                            customer_id      integer,
                            store_id         integer,
                            time_stamp       text,
                            constraint fk_product
                                foreign key (product_id) 
                                REFERENCES product_table (product_id),
                            constraint fk_customer
                                foreign key (customer_id) 
                                REFERENCES customer_table (customer_id),
                            constraint fk_store
                                foreign key (store_id) 
                                REFERENCES store_table (store_id)
                            );'''
    
    ## create product table ## as ** product_table                    
    create_product_table = '''CREATE TABLE IF NOT EXISTS product_table(
                            product_id      INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                            product_name	TEXT,
                            product_flavour    TEXT,  	
                            product_price	 TEXT
                            );'''
    
    # executing tables 
    cur.execute(f' {create_customer_table}{create_store_table}{create_product_table}{create_basket_table}')
    print('tables have been created!!')
    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


