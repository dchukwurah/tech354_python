# api requests
import json
import requests as req

json_body = json.dumps({"postcodes": ["CM1 4AQ", "IG11 5HA", "CM1 4AQ"]})  # changes dictionary into valid json

headers = {"Content-Type": "application/json"}

post_multiple_postcodes = req.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)


print(post_multiple_postcodes.json())  # 200