# Importing necessary libraries
import streamlit as st
from streamlit import switch_page
import pandas as pd
from model import df

# Page's main configuration
st.set_page_config(page_title="Contábil", page_icon="📝", layout="wide")
st.logo("static/teamLogo.png")

# Login state
if 'authenticated' not in st.session_state or not st.session_state['authenticated']:
    st.warning("Por favor, faça login para continuar.")
    st.stop()

st.markdown("# 📝 Contábil")
st.caption("Utilize as ferramentas desenvolvidas para o setor.")
tab1 = st.tabs(["🧾 PLANILHAS NFSE"])

# Tabs
tab1, tab2 = st.tabs(["MANUAL", "FERRAMENTA"])

with tab1:
    # Title
    st.markdown("# 🔎 Manual do usuário")
    st.caption("Aprenda a tirar o melhor proveito possível da ferramenta.")
    st.divider()

    # Describing the tool's objective
    st.markdown("# 🎯 Objetivo")
    st.divider()
    st.markdown('''
    "Planilhas Nfse" foi desenvolvido como um projeto piloto, tendo o intuito de ajudar o processo de lançamento de notas fiscais de serviço no setor Contábil, com margem para ter suas funcionalidades expandidas.
''')
    
    # Describing how the process worked before
    st.markdown("## Como o processo funcionava antes?")
    st.divider()
    st.markdown('''
    1. Criar uma planilha no excel;
    2. Criar o cabeçalho com colunas portadoras dos seguintes campos: 
        - DÉBITO;
        - CRÉDITO;
        - DATA;
        - VALOR;
        - HISTÓRICO;
        - NF;
        - MATRIZ;
        - FILIAL.
    3. Preencher as linhas de acordo com cada variável (coluna);
    4. Concatenar as colunas "HISTÓRICO" e "NF" a fim de formar uma única célula;
    5. Salvar em formato .CSV;
    6. Importar no sistema.
''')
    
    # Describing how the process can work now
    st.markdown("## O processo agora")
    st.divider()
    firstTwoSteps, lastTwoSteps = st.columns(2, gap="medium")

    with firstTwoSteps:
        st.markdown("Planilhas NFSe")
        with st.container(border=True, height=400, key="firstContainer"):
            # Picture and text - Step 1
            firstPicture, firstCaption = st.columns(2, gap="small")
            with firstPicture:
                st.image(image="static/screenshot_teamecosystem.png", caption="PASSO 1")
            
            with firstCaption:
                st.markdown('''
                Por meio do formulário, conseguimos inserir os dados de uma forma mais rápida, além de não precisarmos perder tempo para primeiro criar a estrutura aceita pelo sistema, nem aplicar fórmula de concatenação.
            ''')

            # Picture and text
            secondPicture, secondCaption = st.columns(2, gap="small")
            with secondPicture:
                st.image(image="static/screenshot_downloadbutton.png", caption="PASSO 2")
            
            with secondCaption:
                st.markdown('''
                    Após a inserção dos dados, podemos clicar no botão de **"download"**, que aparece ao passarmos o "mouse" em cima da tabela, e baixá-la em formato **.CSV**, formato de importação aceito pelo sistema.
                ''')

    with lastTwoSteps:
        st.markdown("Excel")
        with st.container(border=True, height=400, key="secondContainer"):
            # Picture and text
            thirdPicture, thirdCaption = st.columns(2, gap="small")
            with thirdPicture:
                st.image(image="static/screenshot_texto-para-colunas.png", caption="PASSO 3")
            
            with thirdCaption:
                st.markdown('''
                    Ao abrirmos o arquivo, nos   deparamos com todos os dados agrupados em uma única coluna, tendo como solução a opção nativa do excel de "Texto para colunas". Para ter acesso à essa funcionalidade, **basta navegar até a aba dados, e selecionar a opção "Texto para colunas"**.
                ''')

            # Picture and text
            fourthPicture, fourthCaption = st.columns(2, gap="small")
            with fourthPicture:
                st.image(image="static/screenshot_textoparacolunas_tiposdedados.png", caption="PASSO 4")
            
            with fourthCaption:
                st.markdown('''
                    Selecionamos "DELIMITADO" como a nossa opção de **"TIPOS DE DADOS ORIGINAIS"** e clicamos em **AVANÇAR**.
                ''')

    # End of the process
    st.markdown("Excel")
    with st.container(border=True, height=350, key="thirdContainer"):
        # Picture and text
        fifthPicture, fifthCaption = st.columns(2, gap="small")
        with fifthPicture:
            st.image(image="static/screenshot_delimitadores.png", caption="PASSO 5")
        
        with fifthCaption:
            st.markdown('''Selecionamos a opção **"OUTROS"** como delimitador e clicamos em avançar e, depois, em **"CONCLUIR"**. ''')
            with st.expander(label="OBS.:"):
                indexImage, indexText = st.columns(2, gap="small")
                with indexImage:
                    st.image("static/removerindex.png")
                
                with indexText:
                    st.markdown('''Para baixar a planilha sem a coluna de index, basta colocar o "mouse" em cima da coluna, apertar os três pontos e clicar na opção ***"Hide column"*** (esconder coluna).''')
                st.markdown("Faz-se necessário removermos o cabeçalho antes de importar.")
                st.markdown("Em caso de dúvidas, você pode sempre contar com um líder.")

    st.success("🥳 **Parabéns!** Você concluiu o processo. Agora é só salvar a planilha e importá-la no sistema.")

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
                if debit == "" or credit == "" or factDate == "" or amount == "" or description == "" or matrix == "" or filial == "":
                    st.error("❌ Preencha todos os campos!")
                else:
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

with st.sidebar:
    logout = st.button("SAIR")
    if logout:
        st.session_state['authenticated'] = False
        switch_page("🏡_Bem-vindo.py")

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