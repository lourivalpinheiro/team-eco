# Importing necessary modules
from streamlit import switch_page
from classes.backend.data.googleapi.apiattributeconnection import ApiConnectionAttributeConnection
from classes.ui.pages import Page
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.ui.headermenu import HeaderMenu
import streamlit as st

# Page's main configuration
Page(name='Bem-vindos', icon='🏡', page_layout='centered')
Logo("static/teamLogo.png")

# Api connection
credentialsConnection = ApiConnectionAttributeConnection.spreadsheet_content

# Welcome text
st.markdown("# 🚀 Team One")
st.caption('Todos os setores, um só time.')

# Authentication
with st.form(key='login_form', enter_to_submit=False):
    username = st.text_input("USUÁRIO", placeholder="Digite seu usuário")
    password = st.text_input("SENHA", type="password", placeholder="Digite sua senha")
    submitted = st.form_submit_button("ENTRAR")

    if submitted:
        if not username or not password:
            st.warning("⚠️ Preencha todos os campos.")
        else:
            # Verifying if user exists within the spreadsheet
            user_row = credentialsConnection[credentialsConnection["username"] == username]

            if not user_row.empty:
                # Strip to remove extra spaces
                senha_digitada = password.strip()
                senha_salva = str(user_row.iloc[0]['password']).strip()

                # Now that I've minimized the potential errors, I validate it.
                if senha_digitada == senha_salva:
                    st.session_state['authenticated'] = True
                    switch_page("pages/3_📝_Contábil.py")
                else:
                    st.error(" ❌ Senha incorreta.")
            else:
                st.error("❌ Usuário não encontrado.")

HeaderMenu.hide_menu()
Footer.footer()