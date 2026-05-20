import streamlit as st


def show_json(title, data):
    if data is not None:
        st.subheader(f"📄 {title}")
        st.json(data)


def show_markdown(title, content):
    if content:
        st.subheader(f"🧠 {title}")
        st.markdown(content)


def show_fields(fields):
    if fields:
        st.subheader("📊 Extracted Fields")
        st.json(fields)


def show_error(error):
    if error:
        # normalize error types
        if isinstance(error, Exception):
            error = str(error)

        st.error(f"❌ Error: {error}")


def show_success(message):
    if message:
        st.success(message)