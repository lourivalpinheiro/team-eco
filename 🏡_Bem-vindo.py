# Importing necessary libraries
import streamlit as st

# Page's main configuration
st.set_page_config(page_title="Bem-vindo", page_icon="🏠", layout="centered")

# Greeting message
st.markdown('''
    # 👋 Olá, sejam bem-vindos!
    ---
    É um prazer ter vocês aqui no nosso app desenvolvido com muito carinho para facilitar nosso dia a dia no escritório.

    Sabemos como as rotinas podem ser intensas, e foi justamente por isso que essa ferramenta surgiu: para nos ajudar a economizar tempo, evitar retrabalhos e ter mais controle sobre nossas tarefas.

    Aqui dentro, vocês irão encontrar recursos pensados para:

    ✅ Automatizar processos repetitivos
    
    ✅ Melhorar o fluxo de informações 
    
    ✅ Deixar nosso trabalho mais leve e eficiente

    Fiquem à vontade para explorar! Se houver dúvidas ou sugestões, estamos por aqui para ouvir vocês. Fiquem sempre por dentro das novidades e atualizações do projeto na guia "👨🏻‍💻 Desenvolvedores".
            ''')


st.logo("static/teamLogo.png")

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