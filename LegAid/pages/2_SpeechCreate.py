import streamlit as st
from utils.shared_functions import example_helper
from utils.navigation import render_sidebar, render_logo


st.set_page_config(layout="centered", initial_sidebar_state="expanded")
render_sidebar()
render_logo()
st.title("🗣️ SpeechCreate")


def render_speech_writer():
    st.write("Compose speeches with AI assistance.")

    st.text_area("Speech Topic", height=100)
    st.button("Draft Speech")


if __name__ == "__main__":
    render_speech_writer()
