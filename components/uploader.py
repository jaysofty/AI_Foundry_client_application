import streamlit as st


def media_uploader(label="📥 Input", allowed_types=None):
    """
    Reusable uploader for files or URLs.

    Returns:
        input_type: "file" | "url" | None
        value: Uploaded file object or URL string
        mime_type: file MIME type or None
    """

    st.subheader(label)

    # -----------------------------
    # FILE INPUT
    # -----------------------------
    file = st.file_uploader(
        "Upload file",
        type=allowed_types or ["mp3", "wav", "mp4", "pdf", "docx", "txt"]
    )

    # -----------------------------
    # URL INPUT
    # -----------------------------
    url = st.text_input("Or enter URL")

    # -----------------------------
    # RETURN LOGIC
    # -----------------------------
    if file is not None:
        return "file", file, file.type

    if url and url.strip() != "":
        return "url", url.strip(), None

    return None, None, None