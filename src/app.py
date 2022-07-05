from table_script import *
from load_basket import *
from load_drop_dupe_db import *

def run_etl():
    create_table()
    load_store()
    load_customer()
    load_product()
    load_basket()
    
run_etl()

