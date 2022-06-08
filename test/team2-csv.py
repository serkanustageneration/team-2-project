import pandas as pd
import csv
from csv import DictReader

#Extracting csv file 
def csv_file_open():
    with open("test.csv",'r') as coffee_file:
        coffee_products_reader = DictReader(coffee_file)
        coffee_products_list = list(coffee_products_reader)
        return coffee_products_list

coffee_products_list = csv_file_open()
#creating a dataframe using pandas, removing index from df and assigning timestamp as index
df_coffee_products = pd.DataFrame(coffee_products_list).set_index('timestamp')
#printing top 5 rows
print(df_coffee_products.head())

#Extracting CSV file using pandas
dfpd_coffee_products = pd.read_csv('test.csv').set_index('timestamp')
print(dfpd_coffee_products.head())

#CSV to PostgreSQL
#COPY test(timestamp,store,customer_name,basket_items,total_price,cash_or_card,card_number)
#FROM 'test.csv'
#DELIMITER ','
#CSV HEADER


#timestamp,store,customer_name,basket_items,total_price,cash_or_card,card_number