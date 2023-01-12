import requests
import json
import webbrowser
from tkinter import *
from tkinter import ttk
import os

data = []
API_KEY = os.environ.get('API_KEY')
root = Tk()
root.title("Upwork Job Screener")
loading_animation = ttk.Progressbar(root, mode='indeterminate')
loading_animation.start()
loading_animation.pack()
skeleton_frame = ttk.Frame(root)
skeleton_frame.pack()

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


def get_data():
    response = requests.get(endpoint_url, headers=headers, params=params)
    if response.status_code == 200:
        data = json.loads(response.text)
        # display data on the tree
        loading_animation.destroy()
    else:
        print(response.status_code)


get_data()


def show_data():
    skeleton_frame.destroy()
    tree = ttk.Treeview(root)
    # create columns and headers
    tree.pack()
    # insert rows
    for job in data['jobs']:
        tree.insert("", "end", values=(job['title'], job['client']['name'], job['budget'], job['url']))
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    tree.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)


# call show_data function after the data is loaded
show_data()

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
else:
print(response.status_code)
search_var = StringVar()
search_entry = ttk.Entry(root, textvariable=search_var)
search_entry.pack()

def search():
    search_keyword = search_var.get()
    # update the params variable with the search keyword
    params['q'] = search_keyword
    get_data()

search_button = ttk.Button(root, text="Search", command=search)
search_button.pack()

root.mainloop()
