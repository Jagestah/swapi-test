#!/usr/bin/env python
import requests

response = requests.get("https://swapi.co/api/people/79/")
data = response.json()
print(data["name"])