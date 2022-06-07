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

    ceate_script = '''  CREATE TABLE test1 (
                            Time_Stamp	    timestamp NOT NULL,	
                            Store_Name	    varchar	NOT NULL,
                            Customer_Name	varchar	NOT NULL,	
                            Basket_Items	varchar	NOT NULL,	
                            Total_Price		numeric NOT NULL,
                            Cash_or_Card	varchar	NOT NULL,	
                            Card_Number	    varchar)'''
    
    cur.execute(ceate_script)

    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is  not None:
        cur.close()
    if conn is not None:
        conn.close()


