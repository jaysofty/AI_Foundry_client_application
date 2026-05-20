# type: ignore
import streamlit as st

from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput
from azure.core.credentials import AzureKeyCredential

from core.config import (
    AZURE_CONTENT_UNDERSTANDING_BASE,
    AZURE_CONTENT_UNDERSTANDING_KEY,
    OPENAI_API_KEY,
    OPENAI_API_BASE
)

from openai import OpenAI

from components.output import (
    show_json,
    show_error,
    show_success,
    show_markdown
)

# -----------------------------
# CLIENTS
# -----------------------------
def get_video_client():
    if not AZURE_CONTENT_UNDERSTANDING_BASE or not AZURE_CONTENT_UNDERSTANDING_KEY:
        return None

    return ContentUnderstandingClient(
        endpoint=AZURE_CONTENT_UNDERSTANDING_BASE,
        credential=AzureKeyCredential(AZURE_CONTENT_UNDERSTANDING_KEY),
        api_version="2025-11-01"
    )


def get_openai_client():
    return OpenAI(
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_API_BASE
    )

# -----------------------------
# GPT ANALYSIS
# -----------------------------
def analyze_with_gpt(transcript: str):

    client = get_openai_client()

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
You are a video intelligence system.

Return:
1. Summary
2. Key insights
3. Key moments (bullet timeline)
4. Topics discussed
"""
            },
            {"role": "user", "content": transcript}
        ],
        temperature=0.3,
        max_tokens=800
    )

    return res.choices[0].message.content


# -----------------------------
# TRANSCRIPT EXTRACTOR
# -----------------------------
def extract_transcript(result):

    text_parts = []

    if not result.contents:
        return ""

    for item in result.contents:

        if hasattr(item, "markdown") and item.markdown:
            text_parts.append(item.markdown)

        if hasattr(item, "text") and item.text:
            text_parts.append(item.text)

    return "\n\n".join(text_parts)


# -----------------------------
# UI
# -----------------------------
def render():

    st.title("🎬 FULL Video Intelligence System")

    client = get_video_client()

    if not client:
        show_error("Missing Content Understanding config")
        return

    video_file = st.file_uploader(
        "Upload Video",
        type=["mp4", "mov", "avi", "m4v"]
    )

    video_url = st.text_input("Or paste video URL")

    if st.button("Analyze Video"):

        try:

            # -----------------------------
            # INPUT FIX (IMPORTANT)
            # -----------------------------
            if video_file:

                file_bytes = video_file.read()

                inputs = [
                    AnalysisInput(data=file_bytes)
                ]

            elif video_url:

                inputs = [
                    AnalysisInput(url=video_url)
                ]

            else:
                show_error("Upload a video or provide a URL")
                return

            # -----------------------------
            # ANALYSIS CALL
            # -----------------------------
            poller = client.begin_analyze(
                analyzer_id="prebuilt-videoSearch",
                inputs=inputs
            )

            result = poller.result()

            show_success("Video analysis complete!")

            show_json("Raw Output", result.as_dict())

            # -----------------------------
            # TRANSCRIPT
            # -----------------------------
            transcript = extract_transcript(result)

            if not transcript:
                st.warning("No transcript found (video may not contain readable audio/text)")
                return

            st.subheader("📝 Transcript")
            show_markdown("Transcript", transcript)

            # -----------------------------
            # GPT ANALYSIS
            # -----------------------------
            st.subheader("🧠 AI Intelligence")

            analysis = analyze_with_gpt(transcript)
            st.write(analysis)

            # -----------------------------
            # SIMPLE TIMELINE (SIMULATED)
            # -----------------------------
            st.subheader("⏱️ Key Moments")

            sentences = transcript.split(".")
            for i, s in enumerate(sentences[:10]):
                if s.strip():
                    st.markdown(f"**{i*5}s → {(i+1)*5}s**: {s.strip()}")

        except Exception as e:
            show_error(str(e))