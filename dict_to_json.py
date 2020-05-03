import json

def from_dict_to_json(dict,file_name):
    with open('json_data/' + file_name + '.json', 'w') as jf:
        json.dump(dict, jf)
