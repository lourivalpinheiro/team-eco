# Importing necessary modules
import streamlit as st

# Page class
class Page:
    """
    Creates a streamlit page.

    :param name: Name of the page (expected to be a string).
    :param icon: Icon of the page (expected to be a string).
    :param page_layout: Format of layout of the page (expected to be a string).
    :return: Streamlit page.
    """
    def __init__(self, name: str, icon: str, page_layout: str):
        st.set_page_config(page_title=name, page_icon=icon, layout=page_layout)