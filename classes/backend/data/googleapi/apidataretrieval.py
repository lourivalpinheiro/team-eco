# Importing necessary modules
from classes.backend.data.googleapi.apiconnection import ApiConnection
from streamlit_gsheets import GSheetsConnection
import streamlit as st

# Data Retrieval Class
class DataRetrieval(ApiConnection):
    """
    Retrieves data from Google Sheets when given a database and spreadsheet name.

    :param database: Database name as in the st.secrets toml file.
    :param spreadsheet: Spreadsheet name as in the st.secrets toml file.
    :return: DataRetrieval object.
    """
    def __init__(self, database: str, spreadsheet: str):
        super().__init__(database, spreadsheet)

    def retrieve_data(self):
        """
        Retrieves data from a Google Spreadsheet.
        """
        conn = st.connection("gsheets", type=GSheetsConnection)
        spreadsheet_content = conn.read(
            spreadsheet=st.secrets[self.database][self.spreadsheet]
        )
        return spreadsheet_content

    @classmethod
    def clear_cache(cls):
        """
        Clear the cache from all data-retrieving functions, updating the dataset at real time.
        """
        st.cache_data.clear()