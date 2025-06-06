# Importing necessary modules
from classes.ui.pages import Page
from classes.ui.headermenu import HeaderMenu
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.backend.data.googleapi.apihumanresourcesnotifications import HumanResourcesSpreadsheet
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

# # Notifications
# notificationsAmount = HumanResourcesSpreadsheet['Aviso'].count()
# with st.expander(f"🔔 NOTIFICAÇÕES: {notificationsAmount}"):
#     monthColumn, yearColumn = st.columns(2, gap='small')
#     with monthColumn:
#         monthSelection = st.selectbox(
#             "Mês",
#             options= sorted(HumanResourcesSpreadsheet['Mês'].unique().tolist()),
#             placeholder="Selecione um mês...",
#             index=None
#         )
#
#     with yearColumn:
#         yearSelection = st.selectbox(
#             "Ano",
#             options= sorted(HumanResourcesSpreadsheet['Ano'].unique().tolist()),
#             placeholder = "Selecione um ano...",
#             index = None
#         )
#
#     filterHumanResourcesNotifications = HumanResourcesSpreadsheet[['Aviso', 'Data']].where(
#         (HumanResourcesSpreadsheet['Mês'] == monthSelection) &
#         (HumanResourcesSpreadsheet['Ano'] == yearSelection)
#     )
#     st.dataframe(filterHumanResourcesNotifications)

# tab1, tab2 = st.tabs(["TEAM", "FERRAMENTAS"])
# with tab1:
#     st.markdown("# Corpo de colaboradores")
#     st.divider()
#
#     with st.expander("Neto Pinheiro", icon='☕'):
#         imageColumn, textColumn = st.columns(2, gap='small')
#         with imageColumn:
#             st.image("static/netopinheiro.jpeg", width=500)
#
#         with textColumn:
#             st.markdown("## 🤖 Cientista de Dados")
#             st.caption("Apaixonado por transformar dados em soluções reais para negócios.")
#             st.divider()
#             st.write('''
#                     Olá! Meu nome é Neto Pinheiro, tenho 25 anos e sou natural de Palmares, Pernambuco, Brasil.
#
#                     Atualmente, estou construindo o caminho à minha carreira como Cientista de Dados, desenvolvendo meu Domínio de Negócio em Contabilidade com objetivo de projetar soluções robustas, escaláveis e orientadas a resultados, que contribuam diretamente para a resolução de problemas e a melhoria de processos nas empresas. Acredito no poder dos dados como ferramenta estratégica, capaz de gerar valor e inovação em diferentes setores.
#
#                     Estou sempre em busca de novos aprendizados, desafios e conexões que me ajudem a crescer como profissional e a contribuir de forma significativa com a área de Ciência de Dados.
#
#                     ## 📌 Principais interesses
#                     ---
#                     - Software Engineering;
#
#                     - Machine Learning;
#
#                     - Inteligência Artificial;
#
#                     - Desenvolvimento de dashboards e relatórios interativos;
#
#                     - Tomada de decisão orientada por dados;
#
#                     - Automação de processos.
#                     ''')
#             st.link_button(
#                 label="LINKEDIN",
#                 url="https://www.linkedin.com/in/lourival-pinheiro-7a8744254?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BTA0WPmJVRV%2BjYt8Fi0ALJw%3D%3D",
#                 icon=":material/badge:",
#             )
#     st.divider()
#
#     st.markdown("# Análises")
#     st.divider()
#
#     # Winner
#     with st.expander("🏆 VENCEDOR"):
#         imageColumn, textColumn = st.columns(2, gap='small')
#         with imageColumn:
#             st.image("static/netopinheiro.jpeg", width=500)
#
#         with textColumn:
#             st.markdown("## 🤖 Cientista de Dados")
#             st.caption("Apaixonado por transformar dados em soluções reais para negócios.")
#             st.divider()
#             st.write('''
#                             Olá! Meu nome é Neto Pinheiro, tenho 25 anos e sou natural de Palmares, Pernambuco, Brasil.
#
#                             Atualmente, estou construindo o caminho à minha carreira como Cientista de Dados, desenvolvendo meu Domínio de Negócio em Contabilidade com objetivo de projetar soluções robustas, escaláveis e orientadas a resultados, que contribuam diretamente para a resolução de problemas e a melhoria de processos nas empresas. Acredito no poder dos dados como ferramenta estratégica, capaz de gerar valor e inovação em diferentes setores.
#
#                             Estou sempre em busca de novos aprendizados, desafios e conexões que me ajudem a crescer como profissional e a contribuir de forma significativa com a área de Ciência de Dados.
#
#                             ## 📌 Principais interesses
#                             ---
#                             - Software Engineering;
#
#                             - Machine Learning;
#
#                             - Inteligência Artificial;
#
#                             - Desenvolvimento de dashboards e relatórios interativos;
#
#                             - Tomada de decisão orientada por dados;
#
#                             - Automação de processos.
#                             ''')
#
#     # Charts
#
# with tab2:
#     st.markdown("🙁 Não há ferramentas para este setor no momento.")

Footer.footer()