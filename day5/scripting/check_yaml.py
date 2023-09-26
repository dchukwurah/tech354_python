# check if json is valid before running.

import os
import sys
import yaml

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")  # r stands for read
        yaml.safe_load(file)  # load lods json but doesnt turn into dictionary like loads
        file.close()
        print("YAML is VALID")
    else:
        print(f"Path '{sys.argv[1]}' is not found")
else:
    print("Usage: check_yaml.py <file>")
