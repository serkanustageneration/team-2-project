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

    ceate_script = '''  CREATE TABLE orders (
                            Payment_type	    varchar	NOT NULL,	
                            Order_id	        INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                            Customer_id	        int NOT NULL ,	
                            Items_id	        int NOT NULL ,	
                            Quantity 		    int NOT NULL ,
                            Store_id	        int NOT NULL ,	
                            Card_Number	        varchar NOT NULL
                            
                            
                                
                                    
                                                                         )'''
    
    cur.execute(ceate_script)

    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is  not None:
        cur.close()
    if conn is not None:
        conn.close()


