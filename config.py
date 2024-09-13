import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Store your Genius API token here
GENIUS_API_TOKEN = os.getenv("GENIUS_API_TOKEN")

if not GENIUS_API_TOKEN:
    raise ValueError("No GENIUS_API_TOKEN found. Please set the environment variable or add it to a .env file.")