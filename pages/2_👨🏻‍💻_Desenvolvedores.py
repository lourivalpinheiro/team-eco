# IMporting necessary libraries
import streamlit as st

# Page's main configuration
st.set_page_config(page_title="Desenvolvedores", page_icon="👨🏻‍💻", layout="centered")
st.logo("static/teamLogo.png")

# Page's content
st.markdown("# 👨🏻‍💻 Desenvolvedores")
st.divider()

# Tabs
tab1, tab2 = st.tabs(["👾 TIME", "📰 DEV NEWS"])

with tab1:
    st.caption("Conheça o time de desenvolvedores.")
    with st.expander(label="☕ NETO PINHEIRO"):
        netoPicture, netoText = st.columns([1, 2])
        with netoPicture:
            st.image("static/netopinheiro.jpeg", width=200)
        with netoText:
            st.markdown("## 🤖 Cientista de Dados")
            st.caption("Apaixonado por transformar dados em soluções reais para negócios.")
            st.divider()
            st.write('''
                    Olá! Meu nome é Neto Pinheiro, tenho 25 anos e sou natural de Palmares, Pernambuco, Brasil.

                    Atualmente, estou construindo o caminho à minha carreira como Cientista de Dados, desenvolvendo meu Domínio de Negócio em Contabilidade com objetivo de projetar soluções robustas, escaláveis e orientadas a resultados, que contribuam diretamente para a resolução de problemas e a melhoria de processos nas empresas. Acredito no poder dos dados como ferramenta estratégica, capaz de gerar valor e inovação em diferentes setores.

                    Estou sempre em busca de novos aprendizados, desafios e conexões que me ajudem a crescer como profissional e a contribuir de forma significativa com a área de Ciência de Dados.

                    ## 📌 Principais interesses
                    ---
                    - Software Engineering;

                    - Machine Learning;

                    - Inteligência Artificial;

                    - Desenvolvimento de dashboards e relatórios interativos;

                    - Tomada de decisão orientada por dados;

                    - Automação de processos.
                    ''')
            st.link_button("PORTFOLIO", url="https://netopinheiro.streamlit.app")

with tab2:
    st.caption("Novidades do sistema.")
    # News
    with st.expander(label="Barra de navegação"):
        st.write("09/05/2025")
        st.image("static/navigationBar.png")
        st.markdown('''
                    Agora você pode navegar entre as páginas do sistema através da barra de navegação na parte superior da tela.
                    Isso facilita a navegação e torna a sua experiência mais intuitiva. Que tal compartilhar essa novidade com a galera?
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
    © <strong>TEAM CONTABILIDADE<strong/>: Gente que inspira! 
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
