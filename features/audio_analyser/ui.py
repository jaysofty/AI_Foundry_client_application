# type: ignore
import streamlit as st
from components.uploader import media_uploader
from components.output import (
    show_json,
    show_markdown,
    show_fields,
    show_error,
    show_success
)


def render():
    st.title("🎧 Audio / Video Analyzer")

    input_type, value, mime_type = media_uploader()

    analyzer_id = "prebuilt-audioSearch"

    if st.button("Analyze"):

        try:
            if not value:
                st.warning("Please upload a file or enter a URL")
                return

            client = get

            if input_type == "file":
                inputs = [{
                    "data": value.read(),
                    "mimeType": mime_type
                }]
            else:
                inputs = [{"url": value}]

            with st.spinner("Analyzing..."):
                result = client.begin_analyze(
                    analyzer_id=analyzer_id,
                    inputs=inputs
                ).result()

            # ✅ SUCCESS OUTPUT
            show_success("Analysis complete!")

            # ✅ FULL RAW OUTPUT (optional but useful for portfolio)
            show_json("Full Response", result.as_dict())

            # ✅ PROCESSED OUTPUT
            for content in result.contents:
                show_markdown("Transcript / Summary", getattr(content, "markdown", None))
                show_fields(getattr(content, "fields", None))

        except Exception as e:
            show_error(str(e))   # FIXED (you passed dict before ❌)