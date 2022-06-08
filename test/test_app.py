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

    create_items_table = '''  CREATE TABLE items_table (
                            item_id	        SERIAL NOT NULL PRIMARY KEY,	
                            item_name	    varchar	NOT NULL,
                            item_size	    varchar	NOT NULL,	
                            item_flavor     varchar NULL,	
                            item_price		numeric NOT NULL)'''
                            
    create_payment_table = '''
                            CREATE TABLE Payment
                            (
                            Order_id	    integer,
                            Total_Price	    numeric	NOT NULL,
                            Date        	date	NOT NULL,	
                            Time        	time	NOT NULL,	
                            Day_of_the_Week	numeric NOT NULL,
                            Cash_or_Card	varchar	NOT NULL,	
                            Card_Number	    varchar
                            );
                            '''
                            
    cur.execute(create_payment_table)
    
    create_customer_table = '''
                            CREATE TABLE Customer
                            (
                            Customer_id	    SERIAL NOT NULL,
                            Customer_Name	varchar	NOT NULL,
                            Store_id        interger
                            );
                            '''
                            
    create_orders_tabe = '''  CREATE TABLE orders (
                            Payment_type	    varchar	NOT NULL,	
                            Order_id	        INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                            Customer_id	        int NOT NULL ,	
                            Items_id	        int NOT NULL ,	
                            Quantity 		    int NOT NULL ,
                            Store_id	        int NOT NULL ,	
                            Card_Number	        varchar NOT NULL
                            
                            
                                
                                    
                                                                         )'''
    

    cur.execute(create_items_table, create_payment_table, create_customer_table,create_orders_tabe)

    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
