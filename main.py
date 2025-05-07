# Importing necessary libraries
import streamlit as st
import pandas as pd
from model import df

# Page's main configuration
st.set_page_config(page_title="Team Eco", page_icon="static/favicon.ico", layout="wide")
st.markdown("# 🧾 Planilhas NFSe")
st.divider()

# Tabs
tab1, tab2 = st.tabs(["MANUAL", "FERRAMENTA"])

with tab1:
    st.markdown("# Descrição do projeto")
    st.divider()

with tab2:
    # Creating session state
    if 'df' not in st.session_state:
        st.session_state['df'] = df


    # Form and Dataframe 
    form, dataframe = st.columns(2, gap="small")

    with form:
        ## Form
        with st.form("nfseData", enter_to_submit=False, clear_on_submit=True):
            debitColumn, creditColumn = st.columns(2, gap="small")
            with debitColumn:
                debit = st.text_input(label="DÉBITO", type="default")
            
            with creditColumn:
                credit = st.text_input(label="CRÉDITO", type="default")
            
            dateColumn, amountColumn = st.columns(2, gap="small")
            with dateColumn:
                factDate = st.date_input(label='DATA', format="DD/MM/YYYY")

            with amountColumn:
                amount = st.number_input(label="VALOR")
            
            description = st.text_area(label="HISTÓRICO", value="Vlr. da Aquisicao de Serviços Conf. NF")
            
            matrixColumn, filialColumn = st.columns(2, gap="small")
            with matrixColumn:
                matrix = st.text_input(label="MATRIZ")
            
            with filialColumn:
                filial = st.text_input(label="FILIAL")

            submit = st.form_submit_button(label="ENVIAR")
            # Condition
            if submit:
                new_data = {
                    'DEBITO': debit,
                    'CREDITO': credit,
                    'DATA': factDate,
                    'VALOR': amount,
                    'HISTORICO': description,
                    'MATRIZ': matrix,
                    'FILIAL': filial
                }
                # New line
                new_row_df = pd.DataFrame([new_data])

                # Concatenating
                st.session_state['df'] = pd.concat([st.session_state['df'], new_row_df], ignore_index=True)
                st.success("✅ Dados adicionados com sucesso!")
            
    # Updated datafrane for the user  
    with dataframe:
        st.dataframe(st.session_state["df"])