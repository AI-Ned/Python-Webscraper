import json
import os


DATA_FILENAME = "sites.json"
site = input("Site HomePage URL: ")
site_search = input("Site URL search parameter: ")
target = input("The target HMTL tag / block: ")
title = input("The title HTML tags. e.g h3.result-title: ")
price = input("The price HTML tags e.g div.price: ")
url = input("The HTML attribute tag that contains the URL to the actual game page: ")

seed = {"site_to_compare" : []}

if not os.path.isfile(DATA_FILENAME):
    with open(DATA_FILENAME, mode='w', encoding='utf-8') as f:
        json.dump(seed, f)

# function to add to JSON
def write_json(new_data, filename=DATA_FILENAME):
    with open(filename,'r+') as file:
         # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["site_to_compare"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

    # python object to be appended
entry = {'site':site,
        'site_search':site_search,
        'target':target,
        'title':title,
        'price':price,
        'url':url
        }


write_json(entry)
