# core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# OPENAI
# -----------------------------
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_DEPLOYMENT = os.getenv("OPENAI_DEPLOYMENT_NAME")

# -----------------------------
# FOUNDRY
# -----------------------------
FOUNDRY_ENDPOINT = os.getenv("FOUNDRY_ENDPOINT") or OPENAI_API_BASE
FOUNDRY_KEY = os.getenv("FOUNDRY_KEY") or OPENAI_API_KEY

# -----------------------------
# AZURE LANGUAGE
# -----------------------------
AZURE_LANGUAGE_ENDPOINT = os.getenv("AZURE_LANGUAGE_ENDPOINT")
AZURE_LANGUAGE_KEY = os.getenv("AZURE_LANGUAGE_KEY")

# ------------------------------------
# AZURE CONTENT UNDERSTANDING
#-----------------------------------

AZURE_CONTENT_UNDERSTANDING_BASE = os.getenv("AZURE_CONTENT_UNDERSTANDING_BASE")
AZURE_CONTENT_UNDERSTANDING_KEY = os.getenv("CONTENT_KEY")

AZURE_DOCUMENT_CONTENT_UNDERSTANDING_BASE = os.getenv("AZURE_DOCUMENT_CONTENT_UNDERSTANDING_BASE")
AZURE_DOCUMENT_CONTENT_UNDERSTANDING_KEY = os.getenv("AZURE_DOCUMENT_CONTENT_UNDERSTANDING_KEY")