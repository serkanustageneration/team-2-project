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

    create_script = ''' CREATE TABLE store_table (
                            Store_ID        SERIAL NOT NULL PRIMARY KEY,
                            Store_name        	VARCHAR	NOT NULL)'''
                            	
    cur.execute(create_script)
   
    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is  not None:
        cur.close()
    if conn is not None:
        conn.close()


