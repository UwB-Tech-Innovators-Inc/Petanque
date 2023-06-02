
import json

def alorytm_turniej():
    pass

def tmp():
    # https://www.geeksforgeeks.org/read-json-file-using-python/
    # Opening JSON file
    f = open('data.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    for i in data['emp_details']:
        print(i)

    # Closing file
    f.close()
    pass
