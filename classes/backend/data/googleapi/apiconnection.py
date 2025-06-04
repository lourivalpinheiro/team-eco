# Importing necessary modules
from streamlit_gsheets import GSheetsConnection
from classes.backend.data.googleapi.apidata import ApiData
import streamlit as st

class ApiConnection(ApiData):
    """
    Connects to a given Google Spreadsheet when given a database and spreadsheet name.

    :param database: Database name as in the st.secrets toml file.
    :param spreadsheet: Spreadsheet name as in the st.secrets toml file.
    """

    def __init__(self, database: str, spreadsheet: str):
        super().__init__(database, spreadsheet)

        """
        Connects to Google API and displays content from a Google Spreadsheet.
        """

    def api_connect(self):
        conn = st.connection("gsheets", type=GSheetsConnection)
        spreadsheet_content = conn.read(
            spreadsheet=st.secrets[self.database][self.spreadsheet]
        )
        return spreadsheet_content

# Entrepreneurs' spreadsheet
entrepreneursConn = st.connection("gsheets", type=GSheetsConnection)
entrepreneursSpreadSheet = entrepreneursConn.read(
    spreadsheet=st.secrets['database']['mahinaSpreadsheet']
)