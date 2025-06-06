# Importing necessary modules
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Companies follow up spreadsheet
companiesFollowUpConn = st.connection("gsheets", type=GSheetsConnection)
companiesFollowup_spreadsheet_content = companiesFollowUpConn.read(
    spreadsheet=st.secrets['database']['accountingsSpreadSheet'],
    worksheet=st.secrets['database']['companiesFollowUpSpreadsheet']
)