# 📘 Documentação do Projeto: **Team Ecosystem**

---

## 🧾 Introdução

---
No dia 05/05/2025, eu, **Lourival Teixeira Pinheiro Neto**, Assistente Contábil Jr. e membro do Setor Contábil da Team Contabilidade, levei à produção o **Team Ecosystem**, um software desenvolvido com o objetivo de melhorar a **comunicação**, **acesso à informação** e a **automação de processos** em todos os setores da empresa.

---

## 🚀 Objetivos do Projeto

---
- Centralizar informações internas de forma acessível;
- Automatizar tarefas repetitivas e processos manuais;
- Melhorar a visualização de dados contábeis e administrativos;
- Facilitar a integração entre os setores da empresa.

---

## ⚙️ Tecnologias Utilizadas

---
O sistema foi desenvolvido com **Python** e utiliza as seguintes bibliotecas:

| Biblioteca               | Finalidade                                              |
|--------------------------|---------------------------------------------------------|
| `streamlit`              | Interface gráfica interativa e de fácil uso             |
| `pandas`                 | Manipulação e análise de dados                          |
| `plotly`                 | Criação de gráficos interativos                         |
| `st-gsheets-connection`  | Conexão segura com a API do Google Sheets (banco de dados) |

---


## 📊 Funcionalidades Principais

---

- Visualização de indicadores contábeis e financeiros;
- Painéis dinâmicos por setor;
- Atualização automática dos dados via Google Sheets;
- Interface amigável com foco no usuário interno;
- Modularização por áreas da empresa (financeiro, RH, fiscal, etc.).

---

## 🧪 Como Executar o Projeto

### Pré-requisitos

---

- Python 3.10+
- Conta no Google com acesso às planilhas utilizadas
- Ambiente virtual configurado

### Instalação
---

```bash 
Clone o repositório
git clone https://github.com/lourivalpinheiro/team-eco.git
cd team-ecosystem
````

```bash
# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
```

```bash
# Instale as dependências
pip install -r requirements.txt
```

```bash
# Execute o sistema
streamlit run 🏡_Bem-vindo.py
```

## 🔐 Segurança

### Autenticação com Google Sheets

---
A conexão com as planilhas do Google é feita por meio do st-gsheets-connection. É necessário:

Ter o link da planilha de credenciais do Google Account.

###  Secrets

---
- O Streamlit é uma biblioteca Python cujo funcionamento é baseado em sessões. À cada vez que um usuário entra conecta à URL de acesso ao app, uma nova sessão é criada;
- Existem **widgets** (itens interativos) do aplicativo que são compartilhados entre as sessões, enquanto outros não são, ficando de responsabilidade do desenvolvedor para aplicar lógica a isso;
- Para as funcionalidades persistentes entre as sessões, o Streamlit não permite que dados sensíveis, como as credenciais para autenticação no app, sejam expostos no código diretamente e, por isso, ele nos força a utilizar dos **Secrets**;
- A funcionalidade de **Secrets** funciona como uma variável ambiente na qual iremos colocar informações sensíveis, chamando-a no código quando necessário, mas sem fazer menção direta, deixando as varíaveis protegidas.

# Aspectos técnicos do código

---

- O aplicativo foi desenvolvido, inicialmente, em um Paradigma de Programação procedural, tendo em vista o meu nível técnico quando iniciei o desenvolvimento;
- No dia 01/09/2025, muitas das funcionalidades do aplicativo, principalmente as que dizem respeito ao **backend** sofreram refatoração usando o Paradigma de Programação Orientada a Objetos, além de conceitos dos princípios de desenvolvimento de Software SOLID.
- O prazo é que até 30/06/2025, todas as funcionalidades existentes no aplicativo utilizem POO e SOLID, estabelecendo-os como padrão na continuidade do projeto.

# Problemas a serem resolvidos

---

## Configurações de página

### Demanda

---
- As classes responsáveis por estabelecer a conexão com a Api do Google utilizam-se de funções que são executadas no momento em que o aplicativo é iniciado;
- Esse fato ocasiona um erro do método "**st.set_page_config**" do Streamlit, responsável por criar as configurações principais de uma página. Esse método deve sempre ser o primeiro trecho de código a ser executado em todas as aplicações.

### Solução

---

- O prazo é que até o dia 30/06/2025, a biblioteca **asyncio** seja utilizada para solucionar esse problema, fazendo com que a execução dos métodos de conexão com a Api só sejam executados uma vez que o aplicativo já tenha carregado as principais informações necessárias para renderizar a página.

# Conclusão

---

- Team Ecosystem é um projeto extremamente promissor à melhora dos processos da Team Contabilidade. Sinto-me honrado em estar desenvolvendo este projeto que possui um imenso potencial de expansão.

