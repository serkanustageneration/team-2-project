from src.extract import *
from src.load_drop_dupe_db import load_data
from src.table_script import create_table
import boto3
s3 = boto3.client('s3')


def transform_data():
    create_table()
    load_data()
    from src.load_basket import load_basket
    load_basket()


def lambda_handler(event, contex=None):
    # bucket = event['Records'][0]['s3']['bucket']['name']
    # key = event['Records'][0]['s3']['object']['key']
    # try:
    #     response = s3.get_object(Bucket=bucket, Key=key)
    #     fieldnames = ['timestamp', 'store', 'customer_name',
    #                   'basket_items', 'total_price', 'cash_or_card', 'card_number']
    #     df = pd.read_csv(response["Body"], names=fieldnames)
    # except Exception as e:
    #     print(e)
    #     print(
    #         f"Error getting object {key} from bucket {bucket}. Make sure they exist and your bucket is in the same region as this function.")
    #     raise e
    # print(key)
    transform_data()
