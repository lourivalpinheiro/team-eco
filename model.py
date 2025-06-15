# Importing necessary libraries
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection
# Data logic 
## Dataframe data
data = {
    "DEBITO": [],
    "CREDITO": [],
    "DATA": [],
    "VALOR": [],
    "HISTORICO": [],
    "MATRIZ": [],
    "FILIAL": []
}

## Creating dataframe
df = pd.DataFrame(data)
    
# Users' amount
usersAmountData = {
    'Quantidade de usuários': [13],
    'Data': ['22/05/2025']
}
usersAmount = pd.DataFrame(usersAmountData)

class ArchiveApiConnection:
    @staticmethod
    @st.cache_data(ttl=600)
    def get_spreadsheet_notifications():
        conn = st.connection("gsheets", type=GSheetsConnection)
        spreadsheet_content = conn.read(
            spreadsheet=st.secrets['database']['spreadsheetArchive'],
            worksheet=st.secrets['database']['archiveNotifications'],
        )
        return spreadsheet_content

    @staticmethod
    @st.cache_data(ttl=600)
    def get_archive_spreadsheet_content():
        conn = st.connection("gsheets", type=GSheetsConnection)
        spreadsheet_content = conn.read(
            spreadsheet=st.secrets['database']['spreadsheetArchive']
        )
        return spreadsheet_content

    @staticmethod
    @st.cache_data(ttl=600)
    def get_accountings_notifications():
        conn = st.connection("gsheets", type=GSheetsConnection)
        notifications_content = conn.read(
            spreadsheet=st.secrets['database']['accountingsSpreadSheet'],
            worksheet=st.secrets['database']['accountingsNotifications'],
        )
        return notifications_content

    @staticmethod
    @st.cache_data(ttl=600)
    def get_companies_followup():
        companiesFollowUpConn = st.connection("gsheets", type=GSheetsConnection)
        companiesFollowUpContent = companiesFollowUpConn.read(
            spreadsheet=st.secrets['database']['accountingsSpreadSheet'],
            worksheet=st.secrets['database']['companiesFollowUpSpreadsheet']
        )
        return companiesFollowUpContent

    @staticmethod
    @st.cache_data(ttl=600)
    def get_entrepreneurs_credentials():
        # Entrepreneurs' spreadsheet credentials
        entrepreneursCredentialsConn = st.connection("gsheets", type=GSheetsConnection)
        entrepreneursSpreadSheetCredentials = entrepreneursCredentialsConn.read(
            spreadsheet=st.secrets['database']['mahinaSpreadsheet'],
            worksheet=st.secrets['database']['entrepreneursSpreadsheet']
        )
        return entrepreneursSpreadSheetCredentials

    @staticmethod
    @st.cache_data(ttl=600)
    def get_entrepreneurs_content():
        # Entrepreneurs' spreadsheet
        entrepreneursConn = st.connection("gsheets", type=GSheetsConnection)
        entrepreneursSpreadSheet = entrepreneursConn.read(
            spreadsheet=st.secrets['database']['mahinaSpreadsheet']
        )
        return entrepreneursSpreadSheet

    @staticmethod
    @st.cache_data(ttl=600)
    def get_documentation_followup_content():
        # Documentation's follow up
        documentation_followup_conn = st.connection("gsheets", type=GSheetsConnection)
        documentation_spreadsheet = documentation_followup_conn.read(
            spreadsheet=st.secrets['database']['documentationFollowUp']
        )
        return documentation_spreadsheet
