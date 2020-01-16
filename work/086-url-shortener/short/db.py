# -*- coding: utf-8 -*-

"""Module to abstract away the database setup and access code."""

import random
import string
from typing import Dict, Optional

import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError


class DynamoTable(object):
    """
    Class to simplify interaction with the configured DynamoDB.

    It abstracts away the necessary schema definition for a table that
    can hold a long url which is stored under a short key.

    """

    def __init__(self, table_name: str = "urls", local: bool = False):
        """
        Initialize a connected DynamoDB table.

        Arguments:
            table_name (str): (Optional) Name of the table on the Dynamo
                Database to connect to. If no name is provided `urls` is used
                by default.
            local (bool): Whether to use a local instance of DynamoDB. If True,
                the DynamoDB should be reachable at "http://localhost:8000".
                Default is False.

        """
        self.table_name = table_name
        self.table = None

        endpoint_url = None
        if local:
            endpoint_url = "http://localhost:8000"

        self.dynamodb = boto3.resource(
            "dynamodb",
            region_name="us-west-1",
            endpoint_url=endpoint_url,
        )

        self.KEY_SCHEMA = [
            {
                "AttributeName": "short",
                "KeyType": "HASH",
            },
            {
                "AttributeName": "long_url",
                "KeyType": "RANGE",
            },
        ]

        self.ATTRIBUTES_DEFINITIONS = [
            {
                "AttributeName": "short",
                "AttributeType": "S",
            },
            {
                "AttributeName": "long_url",
                "AttributeType": "S",
            },
        ]

        self.PROVISIONED_TRHOUGHPUT = {
            "ReadCapacityUnits": 10,
            "WriteCapacityUnits": 10,
        }

        if not self.table:
            self.conntect_table()

    def conntect_table(self):
        """
        Connect to an existing table or create a new table by the name.

        Sets the classes `table` attribute to an active table with the given
        name. If no such table exists to connect to, a table is created.

        Raises:
            RuntimeError: Raised if existing of created table responds to a
                status check, but with a status different than "ACTIVE".

        """
        table = self.dynamodb.Table(self.table_name)
        try:
            status = table.table_status
        except ClientError:
            table = self.create_table()
            status = table.table_status
        else:
            if status != "ACTIVE":
                raise RuntimeError
        self.table = table

    def create_table(self):
        """
        Create table with the given name and the schema defined in the class.

        Returns:
            boto3.resource.Table: The created table object and does not set any
                attributes of the class.

        """
        return self.dynamodb.create_table(
            TableName=self.table_name,
            KeySchema=self.KEY_SCHEMA,
            AttributeDefinitions=self.ATTRIBUTES_DEFINITIONS,
            ProvisionedThroughput=self.PROVISIONED_TRHOUGHPUT,
        )

    def save_long_url(self, long_url: str) -> Dict[str, str]:
        """
        Save a given long URL under a randomly generated key in the DB.

        Arguments:
            long_url (str): URL which to save.

        Returns:
            dict: Contains the `short` key and `long` URL.

        Raises:
            RuntimeError: Raised if the DynamoDB table responds with a
                different HTTP status than 200.

        """
        item = {
            "long_url": long_url.strip(),
        }
        item["short"] = self.get_short_of_long(long_url)

        if item["short"] is None:
            item["short"] = random_string()
            response = self.table.put_item(Item=item)
            if response["ResponseMetadata"]["HTTPStatusCode"] != 200:
                raise RuntimeError
        return item

    def get_short_of_long(self, long_url: str) -> Optional[str]:
        """
        Get short key for given long URL.

        Arguments:
            long_url (str): Long URL to lookup in the database and for which
                to return the short key.

        Returns:
            str: Short key for the given long URL.
            None: If no short key was found, `None` is returned

        """
        response = self.table.scan(
            FilterExpression=Attr("long_url").eq(long_url),
        )
        if response["Count"] == 0:
            return None
        return response["Items"][0].get("short")

    def get_long_from_short(self, short: str) -> Optional[str]:
        """
        Get long URL saved under a given `short` key.

        Arguments:
            short (str): Short key under which the long URL is saved.

        Returns:
            str: Long URL saved under the given short key.
            None: If no entry for the given short key can be found.

        """
        response = self.table.query(
            KeyConditionExpression=Key("short").eq(short),
        )
        if response["Count"] == 0:
            return None
        item = response["Items"][0]
        return item.get("long_url")


def random_string(length: int = 4) -> str:
    """
    Return a random string of given length.

    Arguments:
        length (int): (Optional) Length of the returned string. Default: 4.

    Returns:
        str: Random string of a given length. The string is composed of upper
            and lower case letters as well as digits 0-9.

    """
    return "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=length,
        ),
    )
