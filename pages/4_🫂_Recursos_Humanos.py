# Importing necessary modules
from classes.ui.pages import Page
from classes.ui.headermenu import HeaderMenu
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.backend.authentication import Authentication
import streamlit as st

from classes.ui.textelement import TextElement

# Page's instance
Page(name="Recursos Humanos", icon="🫂", page_layout="wide")
HeaderMenu.hide_menu()
Logo("static/teamLogo.png")
Authentication.authenticate()

# Page's header
TextElement.write("# 🫂 Recursos Humanos")
TextElement.write_caption("Encontre comunicados oficiais, informações sobre setores e mais.")
TextElement.write("---")

# Page's content
st.info("# 🚧 Em desenvolvimento")

with st.sidebar:
    logout = st.button("SAIR")
    if logout:
        Authentication.logout()

Footer.footer()