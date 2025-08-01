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

    # Carregando notificações com spinner e asyncio
    with st.spinner("🔄 Carregando notificações..."):
        ArchiveNotificationContent = asyncio.run(ApiConnection.get_fiscal_notifications_async())

    notificationsAmount = ArchiveNotificationContent['Aviso'].count()
    with st.expander(f"🔔 NOTIFICAÇÕES: {notificationsAmount}"):
        monthColumn, yearColumn = st.columns(2, gap='small')
        with monthColumn:
            monthSelection = st.selectbox(
                "Mês",
                options=sorted(ArchiveNotificationContent['Mês'].unique().tolist()),
                placeholder="Selecione um mês..."
            )

        with yearColumn:
            yearSelection = st.selectbox(
                "Ano",
                options=sorted(ArchiveNotificationContent['Ano'].unique().tolist()),
                placeholder="Selecione um ano..."
            )

        filterArchiveNotifications = ArchiveNotificationContent[
            (ArchiveNotificationContent['Mês'] == monthSelection) &
            (ArchiveNotificationContent['Ano'] == yearSelection)
            ][['Aviso', 'Data']]

        st.dataframe(filterArchiveNotifications)

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
