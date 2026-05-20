# core/client.py
# type: ignore
import os
from openai import OpenAI
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput, AnalysisResult
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

from core.config import (
    OPENAI_API_BASE,
    OPENAI_API_KEY,
    OPENAI_DEPLOYMENT,
    # FOUNDRY_ENDPOINT,
    AZURE_LANGUAGE_ENDPOINT,
    AZURE_LANGUAGE_KEY,
    AZURE_CONTENT_UNDERSTANDING_BASE,
    AZURE_CONTENT_UNDERSTANDING_KEY,
    AZURE_DOCUMENT_CONTENT_UNDERSTANDING_BASE,
    AZURE_DOCUMENT_CONTENT_UNDERSTANDING_KEY,
)

from core.auth import get_credential


# -----------------------------
# OPENAI CLIENT
# -----------------------------
def get_openai_client():
    if not OPENAI_API_BASE or not OPENAI_API_KEY:
        raise ValueError("Missing OpenAI config")

    return OpenAI(
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_API_BASE
    )


# -----------------------------
# FOUNDRY CLIENT
# -----------------------------
# def get_foundry_client():
#     if not FOUNDRY_ENDPOINT:
#         raise ValueError("Missing Foundry endpoint")
#
#     return ContentUnderstandingClient(
#         endpoint=FOUNDRY_ENDPOINT,
#         credential=get_credential()
#     )


# -----------------------------
# LANGUAGE CLIENT
# -----------------------------
def get_language_client():
    if not AZURE_LANGUAGE_ENDPOINT or not AZURE_LANGUAGE_KEY:
        return None

    return TextAnalyticsClient(
        endpoint=AZURE_LANGUAGE_ENDPOINT,
        credential=AzureKeyCredential(AZURE_LANGUAGE_KEY)
    )

def get_content_client():
    if not AZURE_DOCUMENT_CONTENT_UNDERSTANDING_BASE:
        return None

    return ContentUnderstandingClient(
        endpoint=AZURE_DOCUMENT_CONTENT_UNDERSTANDING_BASE,
        credential=AzureKeyCredential(AZURE_DOCUMENT_CONTENT_UNDERSTANDING_KEY),
        api_version="2025-11-01"
    )