# Importing necessary modules
from streamlit_gsheets import GSheetsConnection
import streamlit as st

# Notifications' spreadsheet
HumanResourcesConn = st.connection("gsheets", type=GSheetsConnection)
HumanResourcesSpreadsheet = HumanResourcesConn.read(
    spreadsheet=st.secrets['database']['humanResources']
)