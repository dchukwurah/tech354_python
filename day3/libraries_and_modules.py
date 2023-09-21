# Libraries and modules

# Python has very extensive libraries and modules, this is great for us as DevOps engineers!


# Module = Selection of pre-built functions, classes, variables etc. That you can bring in and use.
# Library =  collection made up of many modules may need to install with pip. Saves time and energy

import math
import random
import requests

# num_float = 23.6625678
#
# print(math.ceil(num_float))
#
# randomList = [1, 2, 3, 4, 5, 6, ]
#
# print(random.choice(randomList))
#
# randomNum = random.randint(1,10)

request_bbc = requests.get("https://www.bbc.co.uk/")
print(request_bbc.status_code)
print(request_bbc.content)

pokemon_request = requests.get("https://pokeapi.co/apo/v2/pokemon/pikachu")