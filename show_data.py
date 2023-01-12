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
