# Importing necessary libraries
import asyncio
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

class ApiConnection:
    @staticmethod
    async def get_spreadsheet_notifications_async() -> pd.DataFrame:
        def sync_read():
            conn = st.connection("gsheets", type=GSheetsConnection)
            return conn.read(
                spreadsheet=st.secrets['database']['spreadsheetArchive'],
                worksheet=st.secrets['database']['archiveNotifications'],
            )
        content = await asyncio.to_thread(sync_read)
        return pd.DataFrame(content)

    @staticmethod
    async def get_archive_spreadsheet_content_async() -> pd.DataFrame:
        def sync_read():
            conn = st.connection("gsheets", type=GSheetsConnection)
            return conn.read(
                spreadsheet=st.secrets['database']['spreadsheetArchive']
            )
        content = await asyncio.to_thread(sync_read)
        return pd.DataFrame(content)

    @staticmethod
    async def get_accountings_notifications_async() -> pd.DataFrame:
        spreadsheet = st.secrets['database']['accountingsSpreadSheet']
        worksheet = st.secrets['database']['accountingsNotifications']
        conn = st.connection("gsheets", type=GSheetsConnection)

        def sync_read(spreadsheet, worksheet):
            return conn.read(spreadsheet=spreadsheet, worksheet=worksheet)

        content = await asyncio.to_thread(sync_read, spreadsheet, worksheet)
        return pd.DataFrame(content)

    @staticmethod
    def get_companies_followup() -> pd.DataFrame:
        conn = st.connection("gsheets", type=GSheetsConnection)
        content = conn.read(
            spreadsheet=st.secrets['database']['accountingsSpreadSheet'],
            worksheet=st.secrets['database']['companiesFollowUpSpreadsheet']
        )
        return pd.DataFrame(content)

    @staticmethod
    def get_documentation_followup_content() -> pd.DataFrame:
        conn = st.connection("gsheets", type=GSheetsConnection)
        content = conn.read(
            spreadsheet=st.secrets['database']['documentationFollowUp']
        )
        return pd.DataFrame(content)

    @staticmethod
    async def get_entrepreneurs_credentials_async() -> pd.DataFrame:
        def sync_read():
            conn = st.connection("gsheets", type=GSheetsConnection)
            return conn.read(
                spreadsheet=st.secrets['database']['mahinaSpreadsheet'],
                worksheet=st.secrets['database']['entrepreneursSpreadsheet']
            )
        content = await asyncio.to_thread(sync_read)
        return pd.DataFrame(content)

    @staticmethod
    async def get_entrepreneurs_content_async() -> pd.DataFrame:
        def sync_read():
            conn = st.connection("gsheets", type=GSheetsConnection)
            return conn.read(
                spreadsheet=st.secrets['database']['mahinaSpreadsheet']
            )
        content = await asyncio.to_thread(sync_read)
        return pd.DataFrame(content)

    @staticmethod
    async def get_documentation_followup_content_async() -> pd.DataFrame:
        def sync_read():
            conn = st.connection("gsheets", type=GSheetsConnection)
            return conn.read(
                spreadsheet=st.secrets['database']['documentationFollowUp']
            )
        content = await asyncio.to_thread(sync_read)
        return pd.DataFrame(content)

    @staticmethod
    async def get_fiscal_async() -> pd.DataFrame:
        def sync_read():
            conn = st.connection("gsheets", type=GSheetsConnection)
            return conn.read(
                spreadsheet=st.secrets['database']['fiscal']
            )
        content = await asyncio.to_thread(sync_read)
        return pd.DataFrame(content)