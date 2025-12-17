import requests
import json
import sys
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read webhook URL
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
if not WEBHOOK_URL:
    print("DISCORD_WEBHOOK_URL not found in .env file")
    sys.exit(1)


response = requests.get("https://zenquotes.io/api/random")
if response.status_code != 200:
    print("Error fetching quote")
    sys.exit(1)
data = response.json()
quote = data[0]['q']
author = data[0]['a']
quote_text = f'"{quote}" - {author}'
print(quote_text)
payload = {
"content": quote_text
}

requests.post(
WEBHOOK_URL,
data=json.dumps(payload),
headers={"Content-Type": "application/json"}
)
