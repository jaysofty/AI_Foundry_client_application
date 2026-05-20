# main.py

import streamlit as st

# Import feature UIs
from features.chat_client.ui import render as chat_ui
from features.audio_analyser.ui import render as audio_ui
from features.video_analyzer.ui import render as video_ui
from features.content_extraction_ai.ui import render as document_ui
from features.language_detector.ui import render as text_analyzer_ui

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Azure AI Portfolio",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# SIDEBAR (NAVIGATION)
# -----------------------------
st.sidebar.title("🚀 AI Portfolio")

st.sidebar.markdown("### Models")

page = st.sidebar.radio(
    "Select Demo",
    [
        "🏠 Home",
        "🤖 AI Chatbot",
        # "🎧 Audio Analyzer",
        "🎬 Video/ 🎧Audio Analyzer",
        "📄 Content Extraction AI",
        "🌍 Language Detection"
    ]
)


# -----------------------------
# HOME PAGE
# -----------------------------
def home():
    st.title("🤖 Azure AI Portfolio")

    st.markdown("""
    Welcome to my **Azure AI Foundry Portfolio**.

    This platform demonstrates real-world AI applications built using:

    - Azure Content Understanding
    - Streamlit UI
    - Python modular architecture

    ### 🔥 Available Demos:
    - 🤖 AI Chatbot
    - 🎬 Video/ 🎧Audio Intelligence
    - 📄 Document Extractor
    - 🌍 Language Detection

    ---
    Select a demo from the sidebar to get started.
    """)


# -----------------------------
# ROUTING
# -----------------------------
if page == "🏠 Home":
    home()

elif page == "🤖 AI Chatbot":
     chat_ui()

# elif page == "🎧 Audio Analyzer":
#     audio_ui()

elif page == "🎬 Video/ 🎧Audio Analyzer":
    video_ui()

elif page == "📄 Content Extraction AI":
    document_ui()


elif page == "🌍 Language Detection":
     text_analyzer_ui()