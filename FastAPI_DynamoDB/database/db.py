from boto3 import resource
from os import getenv

dynamodb = resource("dynamodb",
        aws_access_key_id=getenv("AWS_ACCES_KEY_ID"),
        aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=getenv("REGION_NAME"))


tables = [
    {
        "TableName": "Song",
        
        "AttributeDefinitions": [
            {
                'AttributeName': 'LoaderId',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'SongId',
                'AttributeType': 'S'
            }
        ],

        "KeySchema": [
            {
                'AttributeName': 'LoaderId',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'SongId',
                'KeyType': 'RANGE'
            },

        ],
    },
]


def create_tables():

    try:
        for table in tables:
            dynamodb.create_table(
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                BillingMode="PAY_PER_REQUEST"
            )
    except Exception as e:

        print(e)
