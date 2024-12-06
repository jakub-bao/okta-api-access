import boto3
import asyncio
from okta.client import Client as OktaClient

okta_key_ssm = 'external/api/okta_private_key'

def get_okta_api_key():
    private_key = boto3.client('secretsmanager').get_secret_value(SecretId=okta_key_ssm)['SecretString']
    assert 'RSA PRIVATE KEY' in private_key
    return private_key

def get_okta_client(api_key):
    config = {
        'orgUrl': 'https://statedev.okta.com',
        'clientId': '0oate4b172simvVHJ297',
        'authorizationMode': 'PrivateKey',
        'scopes': [
            'okta.users.read',
            'okta.users.manage',
            'okta.groups.read',
            'okta.groups.manage'
        ],
        'issuer': f'https://statedev.okta.com/oauth2/default',
        'privateKey': api_key,
    }
    return OktaClient(config)

async def list_groups(okta):
    groups, resp, error = await okta.list_groups()
    print(f'Okta response error: {error}')
    return resp

def lambda_handler(event, context):
    api_key = get_okta_api_key()
    okta = get_okta_client(api_key)
    resp = asyncio.run(list_groups(okta))
    return resp.get_body()
