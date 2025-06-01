# Importing necessary modules
from streamlit_gsheets import GSheetsConnection
import streamlit as st

class ApiConnectionAttributeConnection:
    conn = st.connection("gsheets", type=GSheetsConnection)
    spreadsheet_content = conn.read(
        spreadsheet=st.secrets['database']['accountingsSpreadSheet']
    )