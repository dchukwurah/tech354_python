# api requests

import requests as req



post_codes_req = req.get("https://api.postcodes.io/postcodes/SW74ND")

print(post_codes_req)  # 200
print(post_codes_req.headers)  # Retrieves the headers for the request
print(post_codes_req.content)  # Gives json body as bytes
print(post_codes_req.json()) # inbuilt method in the request library to turn it into a dictionary

