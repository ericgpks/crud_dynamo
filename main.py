import json
import boto3

def main:
  token = 'DDDDD'
  expired = '2020/06/12'
  key = {'token': token, 'expired': expired}
  #print(dynamodb.get(key))
  #movie_table = create_movie_table()
  item = {'token': 'CCCCCC1', 'expired': '2020/06/11'}
  update_expression="set #st =:r"
  expression_attribute_names={'#st' : 'comment'}
  expression_attribute_values={':r': '123456789aaa'}
  #print(dynamodb.insert(item))
  #print(dynamodb.update(key, update_expression, expression_attribute_names, expression_attribute_values))
  print(dynamodb.delete(key))