import requests
import json
import webbrowser
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Upwork Job Screener")

# Set the endpoint URL
endpoint_url = 'https://www.upwork.com/api/jobs/v3/search/jobs'

# Set the parameters for the query
params = {
    'q': 'Python',
    'sort': 'create_time',
    'desc': 'true'
}

# Add the developer key to the headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_DEVELOPER_KEY'
}

# Send the GET request
response = requests.get(endpoint_url, headers=headers, params=params)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON data
    data = json.loads(response.text)

