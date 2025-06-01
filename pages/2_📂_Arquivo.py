# Importing necessary libraries
import streamlit as st
from classes.ui.pages import Page
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.ui.headermenu import HeaderMenu
from classes.backend.authentication import Authentication
from classes.backend.data.googleapi.apidataretrieval import DataRetrieval

# Page's main configuration
Page(name="Arquivo", icon="📂", page_layout="wide")
Logo("static/teamLogo.png")

# Login state
Authentication.authenticate()

# Page's content
st.markdown("# 📂 Arquivo")
st.caption("Acompanhe a movimentação dos documentos das empresas pelas quais é responsável.")
st.divider()

# Archive Spreadsheet
archiveData = DataRetrieval(database='database', spreadsheet='spreadsheetArchive')
st.dataframe(archiveData.retrieve_data())

# Update button
def refresh_archive_data():
    """
    Refreshes data from the Google API Spreadsheet.
    """
    st.cache_data.clear()
    
st.button(label="ATUALIZAR", on_click=refresh_archive_data)


with st.sidebar:
    logout = st.button("SAIR")
    if logout:
        Authentication.logout()

HeaderMenu.hide_menu()
Footer.footer()