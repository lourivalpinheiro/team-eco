# Importing necessary libraries
import streamlit as st
from streamlit import switch_page
from model import *

# Page's main configuration
st.set_page_config("Bem-vindos", page_icon="🏡", layout="wide")
st.logo("static/teamLogo.png")

# Authentication
formLogin, textLogin = st.columns([1, 2])

with formLogin:
    with st.form(key='login_form'):
        username = st.text_input("USUÁRIO", placeholder="Digite seu usuário")
        password = st.text_input("SENHA", type="password", placeholder="Digite sua senha")
        submitted = st.form_submit_button("ENTRAR")

        if submitted:
            if not username or not password:
                st.warning("⚠️ Preencha todos os campos.")
            else:
                # Verifying if user exists within the spreadsheet
                user_row = credentialsAccountingsSpreadSheet[credentialsAccountingsSpreadSheet['username'] == username]
                
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

with textLogin:
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
    © <strong>TEAM CONTABILIDADE<strong/> - All rights reserved
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
