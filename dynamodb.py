import json
import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger()

dynamoDB = boto3.resource('dynamodb')
table_name = 'api_token_dev'
table = dynamoDB.Table(table_name)

# get one record   
def get(key):
  try:
    response = table.get_item(Key=key)
  except ClientError as e:
    logger.error(e.response['Error']['Message'])
  else:
    return response["Item"]

# insert
def insert(item):
  try:
    response = table.put_item(Item=item)
  except ClientError as e:
    logger.error(e.response['Error']['Message'])
  else:
    return response

# update
def update(key, update_expression, expression_attribute_names, expression_attribute_values):
  try:
    response = table.update_item(
      Key=key,
      UpdateExpression=update_expression, 
      ExpressionAttributeNames= expression_attribute_names,
      ExpressionAttributeValues=expression_attribute_values
    )
  except ClientError as e:
    logger.error(e.response['Error']['Message'])
  else:
    return response

#delete
def delete(key):
  try:
    response = table.delete_item(Key=key)
  except ClientError as e:
    logger.error(e.response['Error']['Message'])
  else:
    return response