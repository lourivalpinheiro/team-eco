# Importing necessary modules
import streamlit as st
from classes.ui.pages import Page
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.ui.headermenu import HeaderMenu
from classes.ui.textelement import TextElement
from classes.backend.authentication import Authentication
from model import ArchiveApiConnection


Page(name="Arquivo", icon="📂", page_layout="wide")
HeaderMenu.hide_menu()
Logo("static/teamLogo.png")

Authentication.authenticate()

TextElement.write("# 📂 Arquivo")
TextElement.write_caption("Acompanhe a movimentação dos documentos das empresas pelas quais é responsável.")
st.write("---")


ArchiveNotificationContent = ArchiveApiConnection.get_spreadsheet_notifications()

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
            placeholder="Selecione um ano...",
            index=None
        )

    filterArchiveNotifications = ArchiveNotificationContent[['Aviso', 'Data']].where(
        (ArchiveNotificationContent['Mês'] == monthSelection) &
        (ArchiveNotificationContent['Ano'] == yearSelection)
    )
    st.dataframe(filterArchiveNotifications)


dataframeAPI = ArchiveApiConnection.get_archive_spreadsheet_content()  # ou outro df com base na planilha

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

filtered_df = dataframeAPI[dataframeAPI['COMPETÊNCIA'] == selected]
st.dataframe(filtered_df)

st.session_state['filtered_df'] = filtered_df

with st.sidebar:
    logout = st.button("SAIR")
    if logout:
        Authentication.logout()

Footer.footer()
