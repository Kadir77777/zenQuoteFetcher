# zenQuoteFetcher

**zenQuoteFetcher** is a simple Python script that fetches a random quote from the ZenQuotes API, displays it in the terminal, and sends it to a Discord channel using a webhook.

## How It Works
- Loads environment variables from a `.env` file
- Sends a request to the ZenQuotes API
- Parses the JSON response
- Prints the quote and author to the terminal
- Sends the quote to a Discord webhook

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Run the Program
```bash
python main.py
```

## project files 

- **main.py**  
  Contains the main logic. Fetches a random quote from the ZenQuotes API, prints it to the terminal, and sends it to a Discord webhook.

- **requirements.txt**  
  Lists the required Python packages (`requests`, `python-dotenv`).

- **.gitignore**  
  Prevents sensitive files (such as `.env`) and Python cache folders from being committed to GitHub.

- **.env.sample**  
  Template file showing the required environment variable for the Discord webhook (no real values included).

