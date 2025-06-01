# Importing necessary modules
import streamlit as st

# Logo class
class Logo:
    """
    Generates a logo from an image's location path.

    :param image_path: Path to the image's location path.
    :return: Logo.
    """
    def __init__(self, image_path: str):
        st.logo(image_path)
        self.image_path = image_path