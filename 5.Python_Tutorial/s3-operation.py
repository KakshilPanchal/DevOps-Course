import boto3 as boto3

client = boto3.client('s3')
response = client.create_bucket(
 bucket='my-tpl')