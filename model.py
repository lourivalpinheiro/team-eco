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

# Google sheets api connection
def apiConnect():
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=st.secrets['database']['spreadsheet'])
    return df  # ← Important!