# type: ignore
import streamlit as st
from core.client import get_openai_client
from core.config import OPENAI_DEPLOYMENT
from components.output import show_error


def render():

    st.title("🤖 Azure AI Chat Studio")

    if not OPENAI_DEPLOYMENT:
        show_error("Missing OPENAI_DEPLOYMENT")
        return

    try:
        client = get_openai_client()
    except Exception as e:
        show_error(str(e))
        return

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "helpful assistant ready to go!"}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    user_input = st.chat_input("Ask something...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        try:
            response = client.chat.completions.create(
                model=OPENAI_DEPLOYMENT,
                messages=st.session_state.messages
            )

            answer = response.choices[0].message.content

            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

            st.chat_message("assistant").write(answer)

        except Exception as e:
            show_error(str(e))