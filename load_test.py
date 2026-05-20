import os
from dotenv import load_dotenv

load_dotenv()

print("DEBUG KEY:", os.getenv("AZURE_LANGUAGE_KEY"))