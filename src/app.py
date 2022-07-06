def transform_data():
    from table_script import create_table
    from load_drop_dupe_db import load_data
    create_table()
    load_data()
    from load_basket import load_basket
    load_basket()

