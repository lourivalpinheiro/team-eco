# Importing necessary modules
from streamlit_gsheets import GSheetsConnection
import streamlit as st

#
# class ApiConnectionAttributeConnection:
#     conn = st.connection("gsheets", type=GSheetsConnection)
#     spreadsheet_content = conn.read(
#         spreadsheet=st.secrets['database']['accountingsSpreadSheet'],
#         worksheet=st.secrets['database']['accountingsCredentials']
#     )

class ApiConnectionAttributeConnection:
    @staticmethod
    @st.cache_data(show_spinner=False)
    def get_credentials():
        conn = st.connection("gsheets", type=GSheetsConnection)
        return conn.read(
            spreadsheet=st.secrets['database']['accountingsSpreadSheet'],
            worksheet=st.secrets['database']['accountingsCredentials']
        )
