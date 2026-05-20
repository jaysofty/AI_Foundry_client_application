# type: ignore
import os
import streamlit as st

from core.client import get_openai_client
from components.output import show_json, show_error, show_success


def render():

    st.title("🌍 GPT Language Detector")

    client = get_openai_client()

    st.write("Client loaded:", bool(client))

    text = st.text_area("Enter text")

    if st.button("Detect Language"):

        if not text.strip():
            show_error("Enter text first")
            return

        if not client:
            show_error("Missing OpenAI credentials")
            return

        try:
            response = client.chat.completions.create(
                model=os.getenv("OPENAI_DEPLOYMENT_NAME"),
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a language detection system. "
                            "Return ONLY valid JSON in this format:\n"
                            "{"
                            "\"language\": \"...\", "
                            "\"iso_code\": \"...\", "
                            "\"confidence\": 0.0-1.0"
                            "}"
                        )
                    },
                    {
                        "role": "user",
                        "content": text
                    }
                ],
                temperature=0
            )

            # ✅ correct GPT extraction
            result_text = response.choices[0].message.content

            show_success("Detected successfully")
            show_json("Result", result_text)

        except Exception as e:
            show_error(str(e))