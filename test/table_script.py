import psycopg2

hostname = 'localhost'
database = 'test'
username = 'root'
pwd = 'pass' 

conn = None
cur = None
try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd
    )

    cur = conn.cursor()

    #Create an order tables, main table, every other Foreign Key is connected here.
    create_orders_table = '''  CREATE TABLE orders (
                            order_id	        INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                            payment_type	    varchar	NOT NULL,	
                            customer_id	        int NOT NULL ,	
                            items_id	        int NOT NULL ,	
                            quantity 		    int NOT NULL ,
                            store_id	        int NOT NULL ,	
                            card_number	        varchar NOT NULL
                            )'''

    #Item table, stores all the item information. 
    #item_id need to be FK into order table
    create_items_table = '''  CREATE TABLE items_table (
                            item_id	        SERIAL NOT NULL PRIMARY KEY,
                            item_name	    varchar	NOT NULL,
                            item_size	    varchar	NOT NULL,	
                            item_flavor     varchar NULL,	
                            item_price		numeric NOT NULL)'''
               
    #Table of all cash payment, for future reference if needed for data visualisation.
    #need to pull the order_id from Order table.             
    create_cash_payment_table = '''CREATE TABLE cash_payment (
                            order_id	    integer,
                            total_price	    numeric	NOT NULL,
                            date        	date	NOT NULL,	
                            time        	time	NOT NULL,	
                            day_of_the_week	numeric NOT NULL,
                            cash           	boolean
                            );'''
                 
    #Table of all card payment, for data visualisation.
    #card_number need to be encrypted.
    #need to pull the order_id from Order table.
    create_card_payment_table = '''CREATE TABLE card_payment  (
                            order_id	    integer,
                            total_price	    numeric	NOT NULL,
                            date        	date	NOT NULL,	
                            time        	time	NOT NULL,	
                            day_of_the_week	numeric NOT NULL,	
                            card_number	    varchar
                            );'''
                            
    #Table of all customer details, current just name, and need to be encrypted.
    #need to pull store id from Store Table, so we know which customer likes to vist which store*(data visualisation stuff)
    #need to pull the order_id from Order table.
    #customer_id need to be link as a FK to Order table.
    create_customer_table = '''CREATE TABLE customer
                            (
                            customer_id	    SERIAL NOT NULL,
                            customer_name	varchar	NOT NULL,
                            store_id        interger
                            );'''
    
    #Table of all store details, current just location of store.
    #store_id need to be link as a FK to Order table.
    create_store_table = '''CREATE TABLE store
                            (
                            store_id	    SERIAL NOT NULL,
                            store_name  	varchar	NOT NULL
                            );'''
    
                            
    cur.execute(create_orders_table, create_items_table, create_cash_payment_table,
                create_card_payment_table, create_customer_table, create_store_table)

    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
