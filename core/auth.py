# core/auth.py
from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential
from core.config import FOUNDRY_KEY


def get_credential():
    if FOUNDRY_KEY:
        return AzureKeyCredential(FOUNDRY_KEY)

    return DefaultAzureCredential()