# Importing necessary modules
from classes.ui.pages import Page
from classes.ui.headermenu import HeaderMenu
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from model import ArchiveApiConnection
import streamlit as st
import plotly.express as px


if 'entreprenur' not in st.session_state or not st.session_state['entreprenur']:
    Page('Business Room Login', icon='👩🏽‍💼', page_layout='centered')
    HeaderMenu.hide_menu()
    Logo('static/teamLogo.png')

    st.markdown("# 👩🏽‍💼 Business Room")
    st.caption('Um espaço seguro e confiável para Empreendedores Team analisarem os dados de seus negócios.')
    st.divider()

    with st.form("entreprenurForm"):
        entreprenurUsername = st.text_input("USUÁRIO")
        entreprenurPassword = st.text_input("SENHA", type="password")
        isEntreprenurLoginSubmitted = st.form_submit_button('ENTRAR')

        if isEntreprenurLoginSubmitted:
            entrepreneursSpreadSheetCredentials = ArchiveApiConnection.get_entrepreneurs_credentials()
            if not entreprenurUsername or not entreprenurPassword:
                st.warning('Preencha todos os campos')
            else:
                user_row = entrepreneursSpreadSheetCredentials[entrepreneursSpreadSheetCredentials['username'] == entreprenurUsername]

                if not user_row.empty:
                    entered = entreprenurPassword.strip()
                    saved = str(user_row.iloc[0]['password']).strip()

                    if entered == saved:
                        st.session_state['entreprenur'] = True
                        st.rerun()
                    else:
                        st.error("❌ Senha incorreta.")
                else:
                    st.error("❌ Usuário não encontrado.")

    Footer.footer()
    st.stop()


Page(name='Business Room', icon='👩🏽‍💼', page_layout='wide')
HeaderMenu.hide_menu()
Logo('static/teamLogo.png')

st.markdown("# 👩🏽‍💼 Business Room")
st.caption('Um espaço seguro e confiável para Empreendedores Team analisarem os dados de seus negócios.')
st.divider()


if 'entrepreneurs' not in st.session_state:
    st.session_state['entrepreneurs'] = ArchiveApiConnection.get_entrepreneurs_content()

entrepreneurDataframe = st.session_state['entrepreneurs']

salespersonOptions = sorted(entrepreneurDataframe['vendedor'].str.strip().dropna().unique().tolist())
employeeOptions = sorted(entrepreneurDataframe['colaborador'].str.strip().dropna().unique().tolist())
periodOptions = entrepreneurDataframe['mes'].str.strip().dropna().unique().tolist()


@st.dialog('🧾 Relatório de vendas')
def get_employee_receipt():
    with st.form('confirmation', clear_on_submit=False):
        employeeName = st.selectbox("CLIENTE", options=employeeOptions, index=None, placeholder='Selecione um cliente...')
        entreprenurSelection = st.selectbox("EMPREENDEDOR", options=salespersonOptions, index=None, placeholder='Selecione o empreendedor...')
        month = st.selectbox("PERÍODO", options=periodOptions, index=None, placeholder='Selecione o período...')
        printReport = st.form_submit_button('EMITIR')

        if printReport:
            if not employeeName or not entreprenurSelection or not month:
                st.warning('⚠️ Preencha todos os campos')
            else:
                total = entrepreneurDataframe['valor'].where(
                    (entrepreneurDataframe['colaborador'] == employeeName) &
                    (entrepreneurDataframe['vendedor'] == entreprenurSelection) &
                    (entrepreneurDataframe['mes'] == month)
                ).sum()

                with st.expander('🧾 VENDAS DO MÊS'):
                    col1, col2, col3, col4 = st.columns(4)
                    col1.markdown(f"##### Cliente: {employeeName}")
                    col2.markdown(f"##### Empreendedor: {entreprenurSelection}")
                    col3.markdown(f"##### Período: {month}")
                    col4.markdown(f"##### Valor: R$ {total:.2f}")

                    filtered = entrepreneurDataframe[
                        (entrepreneurDataframe['colaborador'] == employeeName) &
                        (entrepreneurDataframe['vendedor'] == entreprenurSelection) &
                        (entrepreneurDataframe['mes'] == month)
                    ]
                    st.dataframe(filtered)

# Abas
tab1, tab2 = st.tabs(['Acompanhamento de vendas', 'Dashboard de vendas'])

with tab1:
    st.button('🧾 RELATÓRIO DE VENDAS', on_click=get_employee_receipt)
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
    col1, col2 = st.columns(2)
    with col1:
        grouped = filtered_df.groupby('colaborador', as_index=False)['valor'].sum()
        chart = px.bar(grouped, x='colaborador', y='valor', title='Total de vendas por colaborador (R$)', color_discrete_sequence=['red'], text_auto=True)
        st.plotly_chart(chart, use_container_width=True)

    with col2:
        grouped = filtered_df.groupby('produto', as_index=False)['quantidade'].sum()
        chart = px.bar(grouped, x='produto', y='quantidade', title='Produto mais vendido', color_discrete_sequence=['red'], text_auto=True)
        st.plotly_chart(chart, use_container_width=True)

    st.divider()

    with st.container(height=490):
        grouped = filtered_df.groupby('mes', as_index=False)['valor'].sum()
        meses_ordenados = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                           'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        chart = px.line(
            grouped,
            x='mes', y='valor',
            title='Vendas em 2025',
            color_discrete_sequence=['red'],
            category_orders={'mes': meses_ordenados}
        )
        st.plotly_chart(chart, use_container_width=True)


with st.sidebar:
    if st.button("SAIR"):
        st.session_state['entreprenur'] = False
        st.rerun()

Footer.footer()

