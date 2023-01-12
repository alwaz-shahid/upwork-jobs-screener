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
        show_data()
    else:
        print(response.status_code)

get_data()

def show_data():
    skeleton_frame.destroy()
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

    for job in data['jobs']:
        tree.insert("", "end", values=(job['title'], job['client']['name'], job['budget'], job['url']))

    def open_job(event):
        item = tree.identify('item', event.x, event.y)
        job_url = tree.item(item, 'values')[3]
        webbrowser.open(job_url)

    tree.bind("<Double-1>", open_job)

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    tree.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)

search_var = StringVar()
search_entry = ttk.Entry(root, textvariable=search_var)
search_entry.pack()

def search():
    search_keyword = search_var.get()
    # update the params variable with the search keyword
    params['q'] = search_keyword
    loading_animation.start()
    loading_animation.pack()
    skeleton_frame.pack()
    get_data()


search_button = ttk.Button(root, text="Search", command=search)
search_button.pack()

root.mainloop()
