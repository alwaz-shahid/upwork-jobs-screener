import requests
import json
import webbrowser
from tkinter import *
from tkinter import ttk
import os

API_KEY = os.environ.get('API_KEY')
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

    # Create a Treeview widget to display the job listings
    tree = ttk.Treeview(root)
    tree["columns"] = ("title", "client", "budget", "url")
    tree.column("#0", width=0, stretch=NO)
    tree.column("title", width=150, stretch=NO)
    tree.column("client", width=100, stretch=NO)
    tree.column("budget", width=100, stretch=NO)
    tree.column("url", width=0, stretch=NO)
    tree.heading("title", text="Title")
    tree.heading("client", text="Client")
    tree.heading("budget", text="Budget")
    tree.heading("url", text="URL")
    tree.pack()

    # Loop through the job listings
    for job in data['jobs']:
        tree.insert("", "end", values=(job['title'], job['client']['name'], job['budget'], job['url']))


# Define a function to open the job URL in a browser when the user double clicks on a row in the Treeview
def open_job(event):
    item = tree.identify('item', event.x, event.y)
    job_url = tree.item(item, 'values')[3]
    webbrowser.open(job_url)


# Bind the function to the Treeview widget
tree.bind("<Double-1>", open_job)

# Create a scrollbar for the Treeview widget
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Set the scrollbar to control the Treeview widget
tree.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tree.yview)
