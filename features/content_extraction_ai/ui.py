# type: ignore
import streamlit as st

from azure.ai.contentunderstanding.models import AnalysisInput
from core.client import get_content_client
from components.output import (
    show_json,
    show_markdown,
    show_fields,
    show_error,
    show_success
)


# -----------------------------
# UI
# -----------------------------
def render():
    st.title("📄 Document / Media Analyzer (Fixed)")

    client = get_content_client()

    if not client:
        show_error("Content Understanding client not configured")
        return

    analyzer = st.selectbox(
        "Choose Analyzer",
        [
            "prebuilt-read",
            "prebuilt-ocr",
            "prebuilt-invoice",
            "prebuilt-receipt",
            "prebuilt-contract"
        ]
    )

    file_input = st.file_uploader(
        "Upload File",
        type=["pdf", "docx", "txt", "png", "jpg", "mp3", "wav", "m4a"]
    )

    url_input = st.text_input("Or enter public URL")

    if st.button("Analyze"):

        try:
            # -----------------------------
            # INPUT HANDLING (FIXED)
            # -----------------------------
            if file_input:
                file_bytes = file_input.read()

                inputs = [
                    AnalysisInput(
                        data=file_bytes
                    )
                ]

            elif url_input:
                inputs = [
                    AnalysisInput(
                        url=url_input
                    )
                ]

            else:
                show_error("Provide file or URL")
                return

            # -----------------------------
            # ANALYZE
            # -----------------------------
            poller = client.begin_analyze(
                analyzer_id=analyzer,
                inputs=inputs
            )

            result = poller.result()

            # -----------------------------
            # OUTPUT
            # -----------------------------
            show_success("Analysis complete!")

            show_json("Full Result", result.as_dict())

            # -----------------------------
            # SMART EXTRACTION
            # -----------------------------
            for item in result.contents:

                if hasattr(item, "markdown") and item.markdown:
                    show_markdown("Extracted Text", item.markdown)

                if hasattr(item, "fields") and item.fields:
                    show_fields(item.fields)

        except Exception as e:
            show_error(str(e))