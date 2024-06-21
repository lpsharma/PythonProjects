import requests
import json
import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
username = os.getenv('SF_USERNAME')
password = os.getenv('SF_PASSWORD')
security_token = os.getenv('SF_SECURITY_TOKEN')

# Salesforce OAuth 2.0 endpoint
login_url = 'https://login.salesforce.com/services/oauth2/token'

# Payload for OAuth 2.0 authentication
payload = {
    'grant_type': 'password',
    'client_id': consumer_key,
    'client_secret': consumer_secret,
    'username': username,
    'password': password + security_token
}

# Authenticate
response = requests.post(login_url, data=payload)
auth_response = response.json()

# Extract access token and instance URL
access_token = auth_response['access_token']
instance_url = auth_response['instance_url']
id = auth_response['id']

print(f'Access Token: {access_token}')
print(f'Instance URL: {instance_url}')
print(f'Id: {id} ')


# Salesforce query endpoint
query_url = f'{instance_url}/services/data/v52.0/query/'

# SOQL query to retrieve data
soql_query = 'SELECT Id, Name FROM Account'

# Headers for the request
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Send query request
response = requests.get(query_url, headers=headers, params={'q': soql_query})
query_response = response.json()

# Print query results
for record in query_response['records']:
    print(f"ID: {record['Id']}, Name: {record['Name']}")

# Example of updating an account record
update_url = f'{instance_url}/services/data/v52.0/sobjects/Account/{record["Id"]}'
update_payload = {
    'Description': 'Updated by Python script'
}

# Send update request
update_response = requests.patch(update_url, headers=headers, json=update_payload)
if update_response.status_code == 204:
    print(f"Successfully updated account {record['Id']}")
else:
    print(f"Failed to update account {record['Id']}: {update_response.text}")

