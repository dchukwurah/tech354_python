# Scripting

# There are seven modules that we can consider "core" in Python for scripting.

import sys
import os
import subprocess
import math
import random
import datetime
import json
# import options from something import something as ST
# sys - system information

print(sys.version)

# os - used to interact with the operating system, usually used for file/folder maniplulation

print(os.getcwd())

# os.mkdir("test_dir")

# subprocess - can do subprocesses
subprocess.run(["python", "helloWorld.py"])

# math - covered

# random - covered

# datetime - used often, can be used to specify date time

what_is_the_date = datetime.datetime.now()
print(what_is_the_date)

# json - usually the data format things are sent around in

x = {
    "name": "John",
    "age": 30,
    "city": "London"
}

print(type(x))

y = json.dumps(x)
print(type(y))
