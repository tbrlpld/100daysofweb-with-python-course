import random
import string

import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError


dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-west2",
    endpoint_url="http://localhost:8000",
)

KEY_SCHEMA = [
    {
        "AttributeName": "short",
        "KeyType": "HASH",
    },
    {
        "AttributeName": "long",
        "KeyType": "RANGE",
    },
]

ATTRIBUTES_DEFINITIONS = [
    {
        "AttributeName": "short",
        "AttributeType": "S",
    },
    {
        "AttributeName": "long",
        "AttributeType": "S",
    },
]

PROVISIONED_TRHOUGHPUT = {
    "ReadCapacityUnits": 10,
    "WriteCapacityUnits": 10,
}


# Get or create table
def get_table(name="urls"):
    table = dynamodb.Table(name)
    try:
        status = table.table_status
    except ClientError:
        table = create_table(name)
    else:
        if status != "ACTIVE":
            raise RuntimeError
    return table


def create_table(name="urls"):
    table = dynamodb.create_table(
        TableName=name,
        KeySchema=KEY_SCHEMA,
        AttributeDefinitions=ATTRIBUTES_DEFINITIONS,
        ProvisionedThroughput=PROVISIONED_TRHOUGHPUT,
    )
    if table.table_status == "ACTIVE":
        return table
    else:
        raise RuntimeError


def save_long_url(table, long_url):
    item = {
        "short": random_string(),
        "long": long_url,
    }
    response = table.put_item(Item=item)

    if response["ResponseMetadata"]["HTTPStatusCode"] != 200:
        raise RuntimeError
    return item


def get_long_from_short(table, short):
    response = table.query(KeyConditionExpression=Key("short").eq(short))
    if response["Count"] == 0:
        return None
    item = response["Items"][0]
    return item.get("long")


def random_string(length=4):
    return "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=length,
        ),
    )
