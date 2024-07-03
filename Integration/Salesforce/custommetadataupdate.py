from simple_salesforce import Salesforce, SalesforceLogin
import os

# Salesforce credentials
username = 'your_salesforce_username'
password = 'your_salesforce_password'
security_token = 'your_salesforce_security_token'
domain = 'login'  # Use 'test' for sandbox, 'login' for production

# Login to Salesforce
session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)
sf = Salesforce(instance=instance, session_id=session_id)

# Query custom metadata type
metadata_type = 'Your_Custom_Metadata__mdt'
query = f"SELECT Id, DeveloperName, Your_Field__c FROM {metadata_type}"
metadata_records = sf.query_all(query)

# Print the metadata records
for record in metadata_records['records']:
    print(record)

# Update a custom metadata record
record_id = 'your_record_id'  # Replace with the actual record Id
updated_fields = {
    'Your_Field__c': 'New Value'
}
sf.CustomMetadataType(metadata_type).update(record_id, updated_fields)

print(f"Record {record_id} updated successfully!")
