# Importing necessary modules
from streamlit import switch_page
from classes.backend.data.googleapi.apiattributeconnection import ApiConnectionAttributeConnection
from classes.ui.pages import Page
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.ui.headermenu import HeaderMenu
from classes.ui.textelement import TextElement
import streamlit as st

# Page configuration
Page(name='Bem-vindos', icon='🏡', page_layout='centered')
Logo("static/teamLogo.png")

# Welcome message
TextElement.write("# 🚀 Team One")
TextElement.write_caption('Todos os setores, um só time.')

# Login form
with st.form(key='login_form', enter_to_submit=False):
    username = st.text_input("USUÁRIO", placeholder="Digite seu usuário")
    password = st.text_input("SENHA", type="password", placeholder="Digite sua senha")
    submitted = st.form_submit_button("ENTRAR")

    if submitted:
        if not username or not password:
            st.warning("⚠️ Preencha todos os campos.")
        else:
            credentials_df = ApiConnectionAttributeConnection.get_credentials()

            # Check if user exists
            user_row = credentials_df[credentials_df["username"] == username]

            if not user_row.empty:
                senha_digitada = password.strip()
                senha_salva = str(user_row.iloc[0]['password']).strip()

                if senha_digitada == senha_salva:
                    st.session_state['authenticated'] = True
                    switch_page("pages/2_Contábil.py")
                else:
                    st.error("❌ Senha incorreta.")
            else:
                st.error("❌ Usuário não encontrado.")

HeaderMenu.hide_menu()
Footer.footer()
