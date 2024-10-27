import requests
import json

# ServiceNow credentials and instance URL
instance_url = 'https://your_instance.service-now.com/api/now/table/incident'
user = 'your_username'
password = 'your_password'

# Incident data
incident_data = {
    "short_description": "Example incident created via Python",
    "description": "This is a detailed description of the incident.",
    "priority": "2"
}

# Set the headers for the request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Create incident
response = requests.post(instance_url, auth=(user, password), headers=headers, data=json.dumps(incident_data))

if response.status_code == 201:
    print("Incident created successfully.")
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
