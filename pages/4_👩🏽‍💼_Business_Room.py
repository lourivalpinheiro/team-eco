# Importing necessary modules
from classes.ui.pages import Page
from classes.ui.headermenu import HeaderMenu
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.backend.authentication import Authentication
from classes.backend.data.googleapi.apiconnection import entrepreneursSpreadSheet
from classes.backend.data.googleapi.apientrepreneursconnection import entrepreneursSpreadSheetCredentials
import streamlit as st
import pandas as pd
import plotly.express as px

# Page's second auth
if 'entreprenur' not in st.session_state or not st.session_state['entreprenur']:
    Page('Business Room Login', icon='👩🏽‍💼', page_layout='centered')
    Authentication.authenticate()
    # Page's main configuration
    HeaderMenu.hide_menu()
    Logo('static/teamLogo.png')

    # Api connection
    credentialsConnection = entrepreneursSpreadSheetCredentials

    # Page's header
    st.markdown("# 👩🏽‍💼 Business Room")
    st.caption('Um espaço seguro e confiável para Empreendedores Team analisarem os dados de seus negócios.')
    st.divider()
    with st.form("entreprenurForm"):
        entreprenurUsername = st.text_input("USUÁRIO")
        entreprenurPassword = st.text_input("SENHA", type="password")
        isEntreprenurLoginSubmitted = st.form_submit_button('ENTRAR')

        if isEntreprenurLoginSubmitted:
            if not entreprenurUsername or not entreprenurPassword:
                st.warning('Preencha todos os campos')
            else:
                # Verifying if user exists within the spreadsheet
                user_row = credentialsConnection[credentialsConnection['username'] == entreprenurUsername]

                if not user_row.empty:
                    # Strip to remove extra spaces
                    entreprenurPassword = entreprenurPassword.strip()
                    entrepreneursavedPassword = str(user_row.iloc[0]['password']).strip()

                    # Now that I've minimized the potential errors, I validate it.
                    if entreprenurPassword == entrepreneursavedPassword:
                        st.session_state['entreprenur'] = True
                        st.rerun()
                    else:
                        st.error(" ❌ Senha incorreta.")
                else:
                    st.error("❌ Usuário não encontrado.")
    st.stop()

# Page's main configuration after logging in
Page(name='Business Room', icon='👩🏽‍💼', page_layout='wide')
HeaderMenu.hide_menu()
Logo('static/teamLogo.png')

# Page's header after logging in
st.markdown("# 👩🏽‍💼 Business Room")
st.caption('Um espaço seguro e confiável para Empreendedores Team analisarem os dados de seus negócios.')
st.divider()

# Dataframe
entrepreneurDataframe = pd.DataFrame(entrepreneursSpreadSheet)

# Page's content
if 'entrepreneurs' not in st.session_state:
    st.session_state['entrepreneurs'] = entrepreneurDataframe

salespersonOptions = sorted(entrepreneurDataframe['vendedor'].str.strip().dropna().unique().tolist())
employeeOptions = sorted(entrepreneurDataframe['colaborador'].str.strip().dropna().unique().tolist())
periodOptions = (entrepreneurDataframe['mes'].str.strip().dropna().unique().tolist())

@st.dialog('🧾 Relatório de vendas')
def get_employee_receipt():
    if 'isPrinted' not in st.session_state or not st.session_state['isPrinted']:
        with (st.form('confirmation', enter_to_submit=False)):
            employeeName = st.selectbox("CLIENTE", options=employeeOptions, index=None, placeholder='Selecione um cliente...')
            entreprenurSelection = st.selectbox("EMPREENDEDOR", options=salespersonOptions, index=None, placeholder='Selecione o empreendedor...')
            month = st.selectbox("PERÍODO", options=periodOptions, index=None, placeholder='Selecione o período...')
            printReport = st.form_submit_button('EMITIR')

            if printReport:
                if not employeeName or not month:
                    st.warning('⚠️ Preencha todos os campos')
                else:
                    total_ordering_sum = entrepreneurDataframe['valor'].where(
                        (entrepreneurDataframe['colaborador'] == employeeName) &
                        (entrepreneurDataframe['vendedor'] == entreprenurSelection) &
                        (entrepreneurDataframe['mes'] == month)
                    ).sum()

                    with st.expander('🧾 VENDAS DO MÊS'):
                        employeesColumn, entreprenursColumn, monthColumn, totalOrderingColumn = st.columns(4, gap='large')
                        with employeesColumn:
                            st.markdown(f"##### Cliente: {employeeName}")

                        with entreprenursColumn:
                            st.markdown(f"##### Empreendedor: {entreprenurSelection}")

                        with monthColumn:
                            st.markdown(f"##### Período: {month}")

                        with totalOrderingColumn:
                            st.markdown(f"##### Valor: R$  {total_ordering_sum:.2f}")

                        spreashsheetEmployee = entrepreneurDataframe[
                        (entrepreneurDataframe['colaborador'] == employeeName) &
                        (entrepreneurDataframe['vendedor'] == entreprenurSelection) &
                        (entrepreneurDataframe['mes'] == month)]
                        st.dataframe(spreashsheetEmployee)


# Archive Spreadsheet
tab1, tab2 = st.tabs(['Acompanhamento de vendas', 'Dashboard de vendas'])
with tab1:
    get_employee_receipt_button = st.button('🧾 RELATÓRIO DE VENDAS', on_click=get_employee_receipt)
    selectedSalesperson = st.selectbox(
        label='VENDEDOR',
        placeholder='Selecione uma opção...',
        options=salespersonOptions,
        index=None,
        key='entrepreneursFilter'
    )
    filtered_df = entrepreneurDataframe[entrepreneurDataframe['vendedor'] == selectedSalesperson]
    st.dataframe(filtered_df)

with tab2:
    employeeColumn, productColumn = st.columns(2, gap='medium')
    with employeeColumn:
        groupedfiltereddf = filtered_df.groupby('colaborador', as_index=False)['valor'].sum()
        employeeChart = px.bar(groupedfiltereddf, x='colaborador', y='valor', color_discrete_sequence=['red'], title='Total de vendas por colaborador (R$)')
        with st.container(height=490):
            st.plotly_chart(employeeChart)

    with productColumn:
        productGroupedFilteredDf = filtered_df.groupby('produto', as_index=False)['quantidade'].sum()
        productChart = px.bar(productGroupedFilteredDf, x='produto', y='quantidade', color_discrete_sequence=['red'], title='Produto mais vendido')
        with st.container(height=490):
            st.plotly_chart(productChart)

    st.divider()

    with st.container(height=490):
        salesOverTimeGrouped = filtered_df.groupby('mes', as_index=False)['valor'].sum()
        meses_ordenados = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                           'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        salesOvertimeChart = px.line(
            salesOverTimeGrouped,
            x='mes',
            y='valor',
            title='Vendas em 2025',
            color_discrete_sequence=['red'],
            category_orders={'mes': meses_ordenados}
        )
        st.plotly_chart(salesOvertimeChart)



with st.sidebar:
    logout = st.button("SAIR")
    if logout:
        st.session_state['entreprenur'] = False
        st.rerun()

Footer.footer()
