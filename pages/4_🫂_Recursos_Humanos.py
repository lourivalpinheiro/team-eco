# Importing necessary modules
from classes.ui.pages import Page
from classes.ui.headermenu import HeaderMenu
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.backend.authentication import Authentication
import streamlit as st

# Page's instance
Page(name="Recursos Humanos", icon="🫂", page_layout="wide")
HeaderMenu.hide_menu()
Logo("static/teamLogo.png")
Authentication.authenticate()

# Page's header
st.markdown("# 🫂 Recursos Humanos")
st.caption("Encontre comunicados oficiais, informações sobre setores e mais.")
st.divider()

# Page's content
st.info("# 🚧 Em desenvolvimento")

with st.sidebar:
    logout = st.button("SAIR")
    if logout:
        Authentication.logout()

Footer.footer()