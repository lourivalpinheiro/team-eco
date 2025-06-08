# Importing necessary libraries
import streamlit as st
import pandas as pd
from classes.ui.pages import Page
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.ui.headermenu import HeaderMenu
from classes.backend.authentication import Authentication
from classes.backend.data.googleapi.apicompaniesfollowup import companiesFollowup_spreadsheet_content
from streamlit_gsheets import GSheetsConnection
from model import df

# Page's main configuration
Page(name="Contábil", icon="📝", page_layout="wide")
HeaderMenu.hide_menu()
Logo("static/teamLogo.png")

# Login state
Authentication.authenticate()

# Page's content
st.markdown("# 📝 Contábil")
st.caption("Utilize as ferramentas desenvolvidas para o setor.")

# Notifications
AccountingsNotificationsSpreadSheet = st.connection("gsheets", type=GSheetsConnection)
AccountingsNotificationContent = AccountingsNotificationsSpreadSheet.read(
    spreadsheet=st.secrets['database']['accountingsSpreadSheet'],
    worksheet=st.secrets['database']['accountingsNotifications'],
)

notificationsAmount = AccountingsNotificationContent['Aviso'].count()
with st.expander(f"🔔 NOTIFICAÇÕES: {notificationsAmount}"):
    monthColumn, yearColumn = st.columns(2, gap='small')
    with monthColumn:
        monthSelection = st.selectbox(
            "Mês",
            options= sorted(AccountingsNotificationContent['Mês'].unique().tolist()),
            placeholder="Selecione um mês...",
            index=None
        )

    with yearColumn:
        yearSelection = st.selectbox(
            "Ano",
            options= sorted(AccountingsNotificationContent['Ano'].unique().tolist()),
            placeholder = "Selecione um ano...",
            index = None
        )

    filterArchiveNotifications = AccountingsNotificationContent[['Aviso', 'Data']].where(
        (AccountingsNotificationContent['Mês'] == monthSelection) &
        (AccountingsNotificationContent['Ano'] == yearSelection)
    )
    st.dataframe(filterArchiveNotifications)

tab1, tab2 = st.tabs(["PLANILHAS NFSE", "ACOMPANHAMENTO DE EMPRESAS"])

with tab1:

    # Creating session state
    if 'df' not in st.session_state:
        st.session_state['df'] = df


    # Form and Dataframe
    form, dataframe = st.columns(2, gap="small")

    with form:
        ## Form
        with st.form("nfseData", enter_to_submit=False, clear_on_submit=True):
            debitColumn, creditColumn = st.columns(2, gap="small")
            with debitColumn:
                debit = st.text_input(label="DÉBITO", type="default")

            with creditColumn:
                credit = st.text_input(label="CRÉDITO", type="default")

            dateColumn, amountColumn = st.columns(2, gap="small")
            with dateColumn:
                factDate = st.date_input(label='DATA', format="DD/MM/YYYY")

            with amountColumn:
                amount = st.number_input(label="VALOR")

            description = st.text_area(label="HISTÓRICO", value="Vlr. da Aquisicao de Serviços Conf. NF")

            matrixColumn, filialColumn = st.columns(2, gap="small")
            with matrixColumn:
                matrix = st.text_input(label="MATRIZ")

            with filialColumn:
                filial = st.text_input(label="FILIAL")

            submit = st.form_submit_button(label="ENVIAR")
            # Condition
            if submit:
                if debit == "" or credit == "" or factDate == "" or amount == "" or description == "" or matrix == "" or filial == "":
                    st.error("❌ Preencha todos os campos!")
                else:
                    new_data = {
                        'DEBITO': debit,
                        'CREDITO': credit,
                        'DATA': factDate,
                        'VALOR': amount,
                        'HISTORICO': description,
                        'MATRIZ': matrix,
                        'FILIAL': filial
                    }
                    # New line
                    new_row_df = pd.DataFrame([new_data])

                    # Concatenating
                    st.session_state['df'] = pd.concat([st.session_state['df'], new_row_df], ignore_index=True)
                    st.success("✅ Dados adicionados com sucesso!")

        # Updated datafrane for the user
        with dataframe:
            st.dataframe(st.session_state["df"])

with tab2:
    
    st.markdown('## Acompanhamento de empresas')
    st.caption('Fique por dentro do progresso das atividades para fechamento.')
    st.info('**OBS.:** todos os filtros precisam ter uma opção selecionada para funcionar.', icon='ℹ️')

    st.divider()

    # Spreadhseet
    companiesOptionsColumn, employeeOptionsColumn, statusOptions = st.columns(3, gap="medium")

    with st.popover('LEGENDA'):
        st.markdown("""
            **🏢 EMPRESA**: empresa a qual deseja acompanhar;
            
            **🙋🏽‍♀️ RESPONSÁVEL**: responsável pela empresa;
            
            **🏷️ STATUS**: situação da operação realizada.
        """)

    with companiesOptionsColumn:
        companiesOptions = sorted(companiesFollowup_spreadsheet_content['empresa'].str.strip().dropna().unique().tolist())
        selectedCompany = st.selectbox(
            label='Empresa',
            placeholder='Selecione uma opção...',
            options=companiesOptions,
            index=None,
            key='companiesFollowUpFilter'
        )

    with employeeOptionsColumn:
        employeeOptions = sorted(
        companiesFollowup_spreadsheet_content['responsavel'].str.strip().dropna().unique().tolist())
        selectedEmployee = st.selectbox(
            label='Responsável',
            placeholder='Selecione uma opção...',
            options=employeeOptions,
            index=None,
            key='employeesFollowUpFilter'
        )

    with statusOptions:
        statusOptions = sorted(companiesFollowup_spreadsheet_content['status'].str.strip().dropna().unique().tolist())
        selectedStatus = st.selectbox(
            label='Status',
            placeholder='Selecione uma opção...',
            options=statusOptions,
            index=None,
            key='statusFollowUpFilter'
        )

    companiesFollowup_spreadsheet_content = companiesFollowup_spreadsheet_content[
        (companiesFollowup_spreadsheet_content['empresa'] == selectedCompany) &
        (companiesFollowup_spreadsheet_content['responsavel'] == selectedEmployee) &
        (companiesFollowup_spreadsheet_content['status'] == selectedStatus)]
    st.dataframe(companiesFollowup_spreadsheet_content)

with st.sidebar:
    logout = st.button("SAIR")
    if logout:
        Authentication.logout()

Footer.footer()