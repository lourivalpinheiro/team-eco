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

# Credentials 
conn = st.connection("gsheets", type=GSheetsConnection)
credentialsAccountingsSpreadSheet = conn.read(
    spreadsheet= st.secrets['database']['accountingsSpreadSheet']
)

# Google API
@st.cache_data
def archiveConnect():
    '''
    Connects to Google API and displays content from a Google Spreadsheet.
    '''
    conn = st.connection("gsheets", type=GSheetsConnection)
    archiveSpreadSheet = conn.read(
        spreadsheet= st.secrets['database']['spreadsheetArchive']
    )
    return archiveSpreadSheet
