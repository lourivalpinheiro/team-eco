# Importing necessary modules
from classes.ui.pages import Page
from classes.ui.headermenu import HeaderMenu
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.backend.authentication import Authentication
from classes.backend.data.googleapi.apiconnection import entrepreneursSpreadSheet
import streamlit as st
import pandas as pd
import plotly.express as px

# Page's second auth
if 'entreprenur' not in st.session_state or not st.session_state['entreprenur']:
    entrepreneurPage = Page('Empreendedores', icon='👩🏽‍💼', page_layout='centered')
    Authentication.authenticate()
    # Page's main configuration
    HeaderMenu.hide_menu()
    Logo('static/teamLogo.png')

    # Page's first auth
    username = 'admin'
    password = '123'
    # Page's header
    st.markdown("# 👩🏽‍💼 Empreendedores")
    st.caption('Um espaço seguro e confiável para empreendedores analisarem os dados de seus negócios.')
    st.divider()
    with st.form("entreprenurForm"):
        entreprenurUsername = st.text_input("USUÁRIO")
        entreprenurPassword = st.text_input("SENHA", type="password")
        isEntreprenurLoginSubmitted = st.form_submit_button('ENTRAR')

        if isEntreprenurLoginSubmitted:
            if not entreprenurUsername or not entreprenurPassword:
                st.warning('Preencha todos os campos')
            else:
                if entreprenurUsername == username and entreprenurPassword == password:
                    st.session_state['entreprenur'] = True
                    st.rerun()

    st.stop()

entrepreneurPage = Page('Empreendedores', icon='👩🏽‍💼', page_layout='wide')
HeaderMenu.hide_menu()
st.markdown("# 👩🏽‍💼 Empreendedores")
st.caption('Um espaço seguro e confiável para empreendedores analisarem os dados de seus negócios.')
st.divider()

# Dataframe
entrepreneurDataframe = pd.DataFrame(entrepreneursSpreadSheet)

# Page's content
if 'entrepreneurs' not in st.session_state:
    st.session_state['entrepreneurs'] = entrepreneurDataframe

salespersonOptions = sorted(entrepreneurDataframe['vendedor'].str.strip().dropna().unique().tolist())

# @st.dialog('Verificação do empreendedor.')
# def verify_entreprenur_selection():
#     with st.form('confirmation', enter_to_submit=False):
#         entreprenurAuthUsername = st.text_input("USUÁRIO")
#         entreprenurAuthPassword = st.text_input("SENHA", type="password")
#         isEntreprenurAuthLoginSubmitted = st.form_submit_button('VERIRIFCAR')
#
#         if isEntreprenurAuthLoginSubmitted:
#             if not entreprenurAuthPassword:
#                 st.warning('Preencha todos os campos')
#             else:
#                 if entreprenurAuthUsername == 'Mahina' and  entreprenurAuthPassword == '123':
#                     st.rerun()
#
#     st.stop()

# Archive Spreadsheet
tab1, tab2 = st.tabs(['Acompanhamento de vendas', 'Dashboard de vendas'])
with tab1:
    selectedSalesperson = st.selectbox(
        label='VENDEDOR',
        placeholder='Selecione uma opção...',
        options=salespersonOptions,
        index=None,
        key='entrepreneursFilter',
        # on_change=verify_entreprenur_selection
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
