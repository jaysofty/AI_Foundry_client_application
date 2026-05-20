import streamlit as st


def page_header(title, subtitle=None):
    st.title(title)

    if subtitle:
        st.caption(subtitle)


def section(title):
    st.markdown(f"## {title}")


def divider():
    st.markdown("---")


def info_box(text):
    st.info(text)


def warning_box(text):
    st.warning(text)