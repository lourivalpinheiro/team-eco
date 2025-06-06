# IMporting necessary libraries
import streamlit as st
from classes.ui.pages import Page
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.ui.headermenu import HeaderMenu
from classes.backend.authentication import Authentication

# Page's main configuration
Page(name="Desenvolvedores", icon="👨🏻‍💻", page_layout="wide")
HeaderMenu.hide_menu()
Logo("static/teamLogo.png")

# Login state
Authentication.authenticate()

# Page's content
st.markdown("# 👨🏻‍💻 Desenvolvedores")
st.caption("Conheça o time de desenvolvedores e fique por dentro das atualizações do projeto.")
st.divider()

# Tabs
tab1, tab2 = st.tabs(["👾 TIME", "📰 DEV NEWS"])

with tab1:
    st.caption("Conheça o time de desenvolvedores.")
    with st.expander(label="☕ NETO PINHEIRO"):
        netoPicture, netoText = st.columns([1, 2])
        with netoPicture:
            st.image("static/netopinheiro.jpeg", width=200, caption='Team One Founder')
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
            st.link_button("PORTFOLIO", url="https://ltpneto.streamlit.app/")

with tab2:
    st.caption("Novidades do sistema.")
    # News
    
    leftSide, rightSide = st.columns(2, gap="small")
    
    with leftSide:
        ## Navigation Bar
        with st.expander(label="Barra de navegação"):
            st.write("09/05/2025")
            st.image("static/navigationBar.png")
            st.markdown('''
                        Agora você pode navegar entre as páginas do sistema através da barra de navegação na parte superior da tela.
                        Isso facilita a navegação e torna a sua experiência mais intuitiva. Que tal compartilhar essa novidade com a galera?
                        ''')

        # Archive follow-up
        with st.expander(label="Acompanhamento do setor de Arquivo"):
                st.write("14/05/2025")
                st.image("static/archivespreadsheet.png")
                st.markdown('''
                            Agora você pode acompanhar a movimentação das suas empresas e ir ao setor de arquivo sabendo exatamente o que deseja coletar.
                            ''')

        # Archive filter
        with st.expander(label="Filtro do acompanhamento do setor de Arquivo"):
            st.write("02/06/2025")
            st.image("static/archiveFilter.png")
            st.markdown('''
                        Agora você pode filtrar o acompanhamento do setor de Arquivo por competência. 
                        ''')

        # Companies follow up
        with st.expander(label="Acompanhamento de empresas"):
            st.write("05/06/2025")
            st.image("static/companiesFollowUp.png")
            st.markdown('''
                            Fique por dentro do progresso das atividades para fechamento. 
                            ''')
   
    

    with rightSide:
        # Authentication
            with st.expander(label="Autenticação"):
                st.write("14/05/2025")
                st.image("static/authentication.png")
                st.markdown('''
                            A segurança agora é garantida! Autenticação foi inserida com sucesso.
                            ''')
    
            ## Analysis Dashboard
            with st.expander(label="Análises do app"):
                st.write("22/05/2025")
                st.image("static/analisesApp.png")
                st.markdown('''
                            Agora é possível obter dados a respeito da usabilidade do aplicativo.
                            ''')

            ## Entrepreneurs' area
            with st.expander(label="Empreendedores"):
                st.write("04/06/2025")
                st.image("static/employeeArea.png")
                st.markdown('''
                            Um espaço seguro e confiável para Empreendedores Team analisarem os dados de seus negócios.
                            ''')
            
      

with st.sidebar:
    logout = st.button("SAIR")
    if logout:
        Authentication.logout()

Footer.footer()
