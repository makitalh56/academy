import json
import os
import sys
import uuid
import datetime

import azure.cosmos.exceptions as AzureError
from azure.cosmos import CosmosClient, PartitionKey


ENDPOINT = os.environ['COSMOS_ENDPOINT']
KEY = os.environ['COSMOS_KEY']
client = CosmosClient(ENDPOINT, credential=KEY)


#CONN_STR = os.environ["COSMOS_CONNECTION_STRING"]
#client = CosmosClient.from_connection_string(conn_str=CONN_STR)

DATABASE_NAME = "hannaf"
CONTAINER_NAME = "ordercontainer"

def run_sample():
    
    #Create database
    try:
        database = client.create_database(DATABASE_NAME)
    except AzureError.CosmosResourceExistsError:
        database = client.get_database_client(DATABASE_NAME)

    #Create container
    try:
        container = database.create_container(id=CONTAINER_NAME, partition_key=PartitionKey(path="/id"))
    except AzureError.CosmosResourceExistsError:
        container = database.get_container_client(CONTAINER_NAME)

    for i in range(1, 3):
        container.upsert_item({
                'id': 'Asiakas{0}'.format(i),
                'productName': 'Omena',
                'productPrice': '0.5'
            }
        )

if __name__ == '__main__':
    run_sample()


