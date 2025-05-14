# Importing necessary libraries
import streamlit as st
from streamlit import switch_page
from model import archiveConnect

# Page's main configuration
st.set_page_config(page_title="Arquivo", page_icon="📂", layout="wide")
st.logo("static/teamLogo.png")

# Login state
if 'authenticated' not in st.session_state or not st.session_state['authenticated']:
    st.warning("Por favor, faça login para continuar.")
    st.stop()

# Page's content
st.markdown("# 📂 Arquivo")
st.caption("Acompanhe a movimentação dos documentos das empresas pelas quais é responsável.")
st.divider()

# Spreadsheet
st.dataframe(archiveConnect())

# Update button
def refreshArchiveData():
    '''
    Refreshes data from the Google API Spreadsheet
    '''
    st.cache_data.clear()
    
st.button(label="ATUALIZAR", on_click=refreshArchiveData)


with st.sidebar:
    logout = st.button("SAIR")
    if logout:
        st.session_state['authenticated'] = False
        switch_page("🏡_Bem-vindo.py")

# Hiding humburguer menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Footer
footer = """
<style>
/* Hide default Streamlit footer */
footer {visibility: hidden;}

.footer-custom {
    position: relative;
    bottom: 0;
    width: 100%;
    text-align: center;
    font-size: 14px;
    color: #ffff;
    padding: 10px 0;
    margin-top: auto;
}
</style>

<div class="footer-custom">
    © <strong>TEAM CONTABILIDADE<strong/>: Gente que inspira! 
</div>
"""

st.markdown(footer, unsafe_allow_html=True)