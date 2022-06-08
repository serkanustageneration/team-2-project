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

    create_customer_table = '''
                            CREATE TABLE Customer
                            (
                            Customer_id	    SERIAL NOT NULL,
                            Customer_Name	varchar	NOT NULL,
                            Store_id        interger
                            );
                            '''

    
    #if payment table =/= exist, then create a table then enter new payment detail. ELSE enter new payment detail.    
    
    cur.execute(create_customer_table)

    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is  not None:
        cur.close()
    if conn is not None:
        conn.close()


