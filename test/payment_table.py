import psycopg2

hostname = 'localhost'
database = 'team2'
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
                            # ALTER TABLE Payment
                            #     ADD CONSTRAINT fk_order_id
                            #     FOREIGN KEY (Order_id)
                            #     REFERENCES Order (Order_id);
                                
                                    
    
    
    #if payment table =/= exist, then create a table then enter new payment detail. ELSE enter new payment detail.    
    
    cur.execute(create_payment_table)

    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is  not None:
        cur.close()
    if conn is not None:
        conn.close()


