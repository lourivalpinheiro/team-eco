# import pandas as pd
# import streamlit as st
#
# from classes.ui.pages import Page
# from classes.ui.logo import Logo
# from classes.ui.footer import Footer
# from classes.ui.headermenu import HeaderMenu
# from classes.backend.authentication import Authentication
# from classes.ui.textelement import TextElement
# from model import ApiConnection
#
# # Configura a página
# Page(name="Fiscal", icon="📃", page_layout="wide")
# HeaderMenu.hide_menu()
# Logo("static/teamLogo.png")
#
# # Autenticação
# Authentication.authenticate()
#
# if st.session_state.get("authenticated", False):
#     TextElement.write("# 📃 Fiscal")
#     TextElement.write_caption("Utilize as ferramentas desenvolvidas para o setor.")
#     TextElement.write("---")
#
#     TextElement.write("## 🔎 Consulta de NCMS")
#     TextElement.write_caption("Busca NCMS na base de dados.")
#     TextElement.write("---")
#
#     # Carrega os dados
#     with st.spinner("🔄 Carregando dados..."):
#         fiscal = ApiConnection.get_fiscal()
#
#     # Lista de códigos únicos
#     codigos_unicos = fiscal["Código"].dropna().astype(str).unique()
#     codigos_ordenados = sorted(codigos_unicos)
#
#     # Layout em colunas para os filtros
#     col1, col2 = st.columns(2)
#
#     with col1:
#         codigo_selecionado = st.selectbox(
#             "Código...",
#             options=["Todos"] + codigos_ordenados,
#             help="Selecione um código NCM ou 'Todos' para não filtrar por código."
#         )
#
#     with col2:
#         descricao_input = st.text_input(
#             "Descrição...",
#             help="Digite parte da descrição do NCM para buscar."
#         )
#
#     if st.button("CONSULTAR"):
#         with st.spinner("🔍 Buscando resultados..."):
#             filtered_fiscal = fiscal.copy()
#
#             # Filtro por código (se não for "Todos")
#             if codigo_selecionado != "Todos":
#                 filtered_fiscal = filtered_fiscal[
#                     filtered_fiscal["Código"].astype(str) == codigo_selecionado
#                 ]
#
#             # Filtro por descrição (se preenchido)
#             if descricao_input.strip():
#                 filtered_fiscal = filtered_fiscal[
#                     filtered_fiscal["Descrição"].str.contains(descricao_input, case=False, na=False)
#                 ]
#
#             # Resultado
#             if filtered_fiscal.empty:
#                 st.info("🔎 Nenhum NCM encontrado com os critérios informados.")
#             else:
#                 st.dataframe(filtered_fiscal)
#
# else:
#     st.warning("⚠️ Você precisa estar logado para acessar esta página.")
#
# # Sidebar com botão de logout
# with st.sidebar:
#     if st.button("SAIR"):
#         Authentication.logout()
#
# # Rodapé
# Footer.footer()

import asyncio
import streamlit as st
import pandas as pd
from classes.ui.pages import Page
from classes.ui.logo import Logo
from classes.ui.footer import Footer
from classes.ui.headermenu import HeaderMenu
from classes.backend.authentication import Authentication
from classes.ui.textelement import TextElement
from model import ApiConnection

Page(name="Fiscal", icon="📃", page_layout="wide")
HeaderMenu.hide_menu()
Logo("static/teamLogo.png")

Authentication.authenticate()

if st.session_state.get("authenticated", False):
    TextElement.write("# 📃 Fiscal")
    TextElement.write_caption("Utilize as ferramentas desenvolvidas para o setor.")
    TextElement.write("---")

    TextElement.write("## Consulta de NCMS")
    TextElement.write_caption("Busca NCMS na base de dados.")
    TextElement.write("---")

    with st.spinner("🔄 Carregando dados..."):
        fiscal = asyncio.run(ApiConnection.get_fiscal_async())

    codigos_unicos = fiscal["Código"].dropna().astype(str).unique()
    codigos_ordenados = sorted(codigos_unicos)

    col1, col2 = st.columns(2)

    with col1:
        codigo_selecionado = st.selectbox(
            "Código...",
            options=["⛔️ Nenhum filtro"] + codigos_ordenados,
            help="Selecione um código NCM ou '⛔️ Nenhum filtro' para não aplicar filtro por código."
        )

    with col2:
        descricao_input = st.text_input(
            "Descrição...",
            help="Digite parte da descrição do NCM para buscar."
        )

    if st.button("CONSULTAR"):
        filtered_fiscal = fiscal.copy()

        if codigo_selecionado != "⛔️ Nenhum filtro":
            filtered_fiscal = filtered_fiscal[
                filtered_fiscal["Código"].astype(str) == codigo_selecionado
            ]

        if descricao_input.strip():
            filtered_fiscal = filtered_fiscal[
                filtered_fiscal["Descrição"].str.contains(descricao_input, case=False, na=False)
            ]

        if filtered_fiscal.empty:
            st.info("🔎 Nenhum NCM encontrado com os critérios informados.")
        else:
            st.dataframe(filtered_fiscal)

else:
    st.warning("⚠️ Você precisa estar logado para acessar esta página.")

with st.sidebar:
    if st.button("SAIR"):
        Authentication.logout()

Footer.footer()
