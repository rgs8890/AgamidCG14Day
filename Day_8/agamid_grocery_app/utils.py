import json


def save_data(file_path, data):

    if not data:
        data = []
    
    # Save the list of dictionaries to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent = 4)
    
def load_data(file_path):
    data = []

    try:
        with open(file_path, 'r') as file:
            data = json.loads(file)
            return data
    
    except FileNotFoundError:
        return data

