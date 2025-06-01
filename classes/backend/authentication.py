# Importing necessary modules
import streamlit as st
from streamlit import switch_page

# Login class
class Authentication:
    """
    Validates user's credentials in order to render the application's pages.
    """

    # Login method
    @classmethod
    def authenticate(cls):
        """
        Stops all content from other pages from being displayed until the user inserts his credentials and logins successfully.
        """
        if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
            st.warning("Por favor, faça login para continuar.")
            st.stop()

    # Logout method
    @classmethod
    def logout(cls):
        """
        Updates the application's session state and goes back to blocking other pages' content rendering, requiring authentication once more.
        """
        st.session_state["authenticated"] = False
        switch_page("🏡_Bem-vindo.py")