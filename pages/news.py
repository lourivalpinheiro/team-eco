# Importing necessary libraries
import streamlit as st

# Dialog for feedback
@st.dialog("FEEDBACK")
def navigationFeedback():
            with st.form("navigationFeedback", enter_to_submit=False):
                name = st.text_input("Nome")
                surname = st.text_input("Sobrenome")
                sector = st.selectbox("Setor", ["Contábil", "Fiscal", "Financeiro", "RH", "TI"])
                opnion = st.text_area("O que achou da nova barra de navegação?")
                submited = st.form_submit_button("Enviar")
                if submited:
                    if name == "":
                        st.warning("Preencha o campo Nome")
                    elif surname == "":
                        st.warning("Preencha o campo Sobrenome")
                    elif sector == "":
                        st.warning("Preencha o campo Setor")
                    elif opnion == "":
                        st.warning("Preencha o campo Opinião")
                    else:
                        st.info("Obrigado pelo feedback! Sua opinião é muito importante.", icon="🙏🏼")
    
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
