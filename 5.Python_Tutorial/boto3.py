import boto3

client= boto3.client('s3')
assert isinstance(client.create_bucket, object)
response = client.create_bucket