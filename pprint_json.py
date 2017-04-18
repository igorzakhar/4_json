import json


def load_data(filepath):
    with open(filepath) as file:
        data = json.load(file)
    return data
    

def pretty_print_json(data):
    output = json.dumps(data, ensure_ascii=False, 
                        sort_key=True, indent=4)
    return output


if __name__ == '__main__':
    import sys
    import os


    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
        filepath = sys.argv[1]
        data = load_data(filepath)        
        output = pretty_print_json(data)
        print(output)
    else:
        print("Enter the filename.")
        print("Example: python pprint_json.py <filename>")