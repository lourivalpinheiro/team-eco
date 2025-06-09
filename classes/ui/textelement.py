# Importing necessary modules
import streamlit as st

# Class
class TextElement:
    @classmethod
    def write(cls, text: str):
        st.write(text)

    @classmethod
    def write_caption(cls, text: str):
        st.caption(text)