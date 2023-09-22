# Parsing is making something more understandable

import json
parsed_json = json.loads(open("example_json.json").read())  # loads data as a dictionary

for value in parsed_json:
    print(value, parsed_json[value])

