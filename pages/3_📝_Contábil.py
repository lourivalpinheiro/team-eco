# Importing necessary modules
import streamlit as st
import pandas as pd
from classes.ui.pages import Page
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.ui.headermenu import HeaderMenu
from classes.backend.authentication import Authentication
from model import ArchiveApiConnection
from model import df


Page(name="Contábil", icon="📝", page_layout="wide")
HeaderMenu.hide_menu()
Logo("static/teamLogo.png")

Authentication.authenticate()

if st.session_state.get("authenticated", False):

    st.markdown("# 📝 Contábil")
    st.caption("Utilize as ferramentas desenvolvidas para o setor.")


    if "accounting_notifications" not in st.session_state:
        ArchiveApiConnection.get_accountings_notifications()

    notification_df = st.session_state["accounting_notifications"]

    notificationsAmount = notification_df['Aviso'].count()
    with st.expander(f"🔔 NOTIFICAÇÕES: {notificationsAmount}"):
        monthColumn, yearColumn = st.columns(2, gap='small')
        with monthColumn:
            monthSelection = st.selectbox(
                "Mês",
                options=sorted(notification_df['Mês'].unique().tolist()),
                placeholder="Selecione um mês...",
                index=None
            )
        with yearColumn:
            yearSelection = st.selectbox(
                "Ano",
                options=sorted(notification_df['Ano'].unique().tolist()),
                placeholder="Selecione um ano...",
                index=None
            )

        filterArchiveNotifications = notification_df[['Aviso', 'Data']].where(
            (notification_df['Mês'] == monthSelection) & (notification_df['Ano'] == yearSelection)
        )
        st.dataframe(filterArchiveNotifications)


    tab1, tab2 = st.tabs(["PLANILHAS NFSE", "ACOMPANHAMENTO DE EMPRESAS"])

    with tab1:
        if 'df' not in st.session_state:
            st.session_state['df'] = df

        form, dataframe = st.columns(2, gap="small")
        with form:
            with st.form("nfseData", enter_to_submit=False, clear_on_submit=True):
                debitColumn, creditColumn = st.columns(2, gap="small")
                with debitColumn:
                    debit = st.text_input(label="DÉBITO")

                with creditColumn:
                    credit = st.text_input(label="CRÉDITO")

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

                if submit:
                    if not all([debit, credit, factDate, amount, description, matrix, filial]):
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
                        new_row_df = pd.DataFrame([new_data])
                        st.session_state['df'] = pd.concat([st.session_state['df'], new_row_df], ignore_index=True)
                        st.success("✅ Dados adicionados com sucesso!")

        with dataframe:
            st.dataframe(st.session_state["df"])

    with tab2:
        st.markdown('## Acompanhamento de empresas')
        st.caption('Fique por dentro do progresso das atividades para fechamento.')
        st.info('**OBS.:** todos os filtros precisam ter uma opção selecionada para funcionar.', icon='ℹ️')
        st.divider()

        companies_df = ArchiveApiConnection.get_companies_followup()

        companiesOptionsColumn, employeeOptionsColumn, statusOptions = st.columns(3, gap="medium")

        with st.popover('LEGENDA'):
            st.markdown("""
                **🏢 EMPRESA**: empresa a qual deseja acompanhar;  
                **🙋🏽‍♀️ RESPONSÁVEL**: responsável pela empresa;  
                **🏷️ STATUS**: situação da operação realizada.
            """)

        with companiesOptionsColumn:
            companiesOptions = sorted(companies_df['empresa'].str.strip().dropna().unique().tolist())
            selectedCompany = st.selectbox('Empresa', options=companiesOptions, placeholder="Selecione...", index=None)

        with employeeOptionsColumn:
            employeeOptions = sorted(companies_df['responsavel'].str.strip().dropna().unique().tolist())
            selectedEmployee = st.selectbox('Responsável', options=employeeOptions, placeholder="Selecione...", index=None)

        with statusOptions:
            statusOptions = sorted(companies_df['status'].str.strip().dropna().unique().tolist())
            selectedStatus = st.selectbox('Status', options=statusOptions, placeholder="Selecione...", index=None)

        filtered = companies_df[
            (companies_df['empresa'] == selectedCompany) &
            (companies_df['responsavel'] == selectedEmployee) &
            (companies_df['status'] == selectedStatus)
        ]
        st.dataframe(filtered)

else:
    st.warning("⚠️ Você precisa estar logado para acessar esta página.")


with st.sidebar:
    logout = st.button("SAIR")
    if logout:
        Authentication.logout()


Footer.footer()
