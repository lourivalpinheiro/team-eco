# Importing necessary modules
import streamlit as st

# Chatbot box class
class ChatBotBox:
    def __init__(self, place_holder: str):
        st.chat_input(placeholder=place_holder)
        self.place_holder = place_holder


    def display_chat(self, messages):
        """
        Display the chat messages and inputbox.

        Parameters
        ---
        messages: List of tuples.

        Returns
        ---
        messages: List of tuples.
        """

        # Display chat messages
        for role, msg in messages:
            with st.chat_message(role):
                st.write(msg)

        # Get user input
        user_input = st.chat_input(self.place_holder)
        return user_input