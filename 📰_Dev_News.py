# Importing necessary libraries
import streamlit as st
    
# Page's main configuration
st.set_page_config(page_title="News", page_icon="📰", layout="centered")
st.markdown("# 📰 Dev News")
st.caption("Saiba quais as principais novidades e atualizações do projeto.")
st.divider()

# News
with st.expander(label="Barra de navegação"):
    st.write("09/05/2025")
            
    st.image("static/navigationBar.png")
    st.markdown('''
                Agora você pode navegar entre as páginas do sistema através da barra de navegação na parte superior da tela.
                Isso facilita a navegação e torna a experiência do usuário mais intuitiva. Que tal compartilhar essa novidade com a galera?
                ''')

st.logo("static/teamLogo.png")

with st.sidebar:
    st.link_button("DEV", url="https://netopinheiro.streamlit.app/", icon="👨🏻‍💻")

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