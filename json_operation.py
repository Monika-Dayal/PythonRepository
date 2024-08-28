#  1. check it is a proper json or not
#  2. Add 'state' in the address field if at all state is not present.
#  3. replace the hiking in the hobbies with any other hobbie

import json

json_data = input('Insert json data: ')


def check_json(data):
    try:
        parsed_data = json.loads(data)
        return parsed_data
    except ValueError:
        print('Invalid JSON')
        return None


def json_operations():
    parsed_data = check_json(json_data)
    if parsed_data is not None:
        print('Valid JSON')
        if 'address' in parsed_data and 'state' not in parsed_data['address']:
            parsed_data["address"]["state"] = 'Karnataka'
        else:
            print('State is already present.')
        if 'hobbies' in parsed_data:
            hobbies = parsed_data['hobbies']
            if 'hiking' in hobbies:
                index = hobbies.index('hiking')
                hobbies[index] = 'biking'
            else:
                print('hiking is not present in hobbies.')
        else:
            print('hobbies key not present in json.')
        final_json = json.dumps(parsed_data)
        print(f"Updated JSON is: {final_json}")


json_operations()
