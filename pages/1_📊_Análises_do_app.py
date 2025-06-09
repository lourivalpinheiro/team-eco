# Importing necessary modules
import streamlit as st
from classes.ui.pages import Page
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.ui.headermenu import HeaderMenu
from classes.ui.textelement import TextElement
from classes.backend.authentication import Authentication
from classes.backend.data.analysis.plots import usersAmountFig

# Page's main configuration
Page("Análises do app", icon='📊', page_layout='wide')
HeaderMenu.hide_menu()
Logo("static/teamLogo.png")

# Login state
Authentication.authenticate()


if st.session_state.get("authenticated", False):
    # Page's content
    TextElement.write('# 📊 Análises do app')
    st.divider()
    with st.container(height=490):
        st.plotly_chart(usersAmountFig)
    with st.sidebar:
        logout = st.button("SAIR")
        if logout:
            Authentication.logout()
else:
    st.warning("⚠️ Você precisa estar logado para acessar esta página.")

Footer.footer()
