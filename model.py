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

conn = st.connection("gsheets", type=GSheetsConnection)
spreadsheet_content = conn.read(
    spreadsheet=st.secrets['database']['spreadsheetArchive']
)

