# Importing necessary libraries
import pandas as pd
import streamlit as st
from classes.ui.pages import Page
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.ui.headermenu import HeaderMenu
from classes.backend.authentication import Authentication
from streamlit_gsheets import GSheetsConnection
from model import spreadsheet_content


# Page's main configuration
Page(name="Arquivo", icon="📂", page_layout="wide")
HeaderMenu.hide_menu()
Logo("static/teamLogo.png")

# Login state
Authentication.authenticate()

# Page's content
st.markdown("# 📂 Arquivo")
st.caption("Acompanhe a movimentação dos documentos das empresas pelas quais é responsável.")
st.divider()

# Notifications
ArchiveNotificationsSpreadSheet = st.connection("gsheets", type=GSheetsConnection)
ArchiveNotificationContent = ArchiveNotificationsSpreadSheet.read(
    spreadsheet=st.secrets['database']['spreadsheetArchive'],
    worksheet=st.secrets['database']['archiveNotifications'],
)

notificationsAmount = ArchiveNotificationContent['Aviso'].count()
with st.expander(f"🔔 NOTIFICAÇÕES: {notificationsAmount}"):
    monthColumn, yearColumn = st.columns(2, gap='small')
    with monthColumn:
        monthSelection = st.selectbox(
            "Mês",
            options= sorted(ArchiveNotificationContent['Mês'].unique().tolist()),
            placeholder="Selecione um mês...",
            index=None
        )

    with yearColumn:
        yearSelection = st.selectbox(
            "Ano",
            options= sorted(ArchiveNotificationContent['Ano'].unique().tolist()),
            placeholder = "Selecione um ano...",
            index = None
        )

    filterArchiveNotifications = ArchiveNotificationContent[['Aviso', 'Data']].where(
        (ArchiveNotificationContent['Mês'] == monthSelection) &
        (ArchiveNotificationContent['Ano'] == yearSelection)
    )
    st.dataframe(filterArchiveNotifications)

dataframeAPI = pd.DataFrame(spreadsheet_content)

if 'dataframeAPI' not in st.session_state:
    st.session_state['dataframeAPI'] = dataframeAPI

options = sorted(dataframeAPI['COMPETÊNCIA'].str.strip().dropna().unique().tolist())

selected = st.selectbox(
    label='COMPETÊNCIA',
    placeholder='Selecione uma opção...',
    options=options,
    index=None,
    key='archiveSelect'
)

# Archive Spreadsheet
filtered_df = dataframeAPI[dataframeAPI['COMPETÊNCIA'] == selected]
st.dataframe(filtered_df)

if 'filtered_df' not in st.session_state:
    st.session_state['filtered_df'] = filtered_df

if st.session_state['archiveSelect'] == options:
    st.session_state['dataframeAPI'] = options

with st.sidebar:
    logout = st.button("SAIR")
    if logout:
        Authentication.logout()

Footer.footer()