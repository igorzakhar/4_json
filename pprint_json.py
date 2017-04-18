import json
import sys
import os


def load_data(filepath):
    with open(filepath) as file:
        json_data = json.load(file)
    return json_data
    

def pretty_print_json(data):
    formatted_json = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4)

    return formatted_json


if __name__ == '__main__':

    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
        filepath = sys.argv[1]
        json_data = load_data(filepath)        
        formatted_json = pretty_print_json(json_data)
        print(formatted_json)
    else:
        print("Enter the filename.")
        print("Example: python pprint_json.py <filename>")