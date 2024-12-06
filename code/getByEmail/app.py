import json
import boto3
from okta.client import Client as OktaClient
from okta.models import UserProfile, CreateUserRequest

okta_key_ssm = 'external/api/okta_private_key'


def lambda_handler(event, context):
    private_key = boto3.client('secretsmanager').get_secret_value(SecretId=okta_key_ssm)['SecretString']
    print(private_key)
    return 'finished'
