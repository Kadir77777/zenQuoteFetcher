import requests
import json
import sys
import os


response = requests.get("https://zenquotes.io/api/random")
if response.status_code != 200:
    print("Error fetching quote")
    sys.exit(1)
data = response.json()
quote = data[0]['q']
author = data[0]['a']
quote_text = f'"{quote}" - {author}'
print(quote_text)