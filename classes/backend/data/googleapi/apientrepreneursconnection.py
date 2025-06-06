# Importing necessary modules
from streamlit_gsheets import GSheetsConnection
import streamlit as st

# Entrepreneurs' spreadsheet credentials
entrepreneursCredentialsConn = st.connection("gsheets", type=GSheetsConnection)
entrepreneursSpreadSheetCredentials = entrepreneursCredentialsConn.read(
    spreadsheet=st.secrets['database']['mahinaSpreadsheet'],
    worksheet=st.secrets['database']['entrepreneursSpreadsheet']
)