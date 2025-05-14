# Importing necessary libraries
import streamlit as st
import pandas as pd

st.logo("static/teamLogo.png")

# Setting up pages
## Planilhas NFse
news = st.Page(page="pages/news.py",
        title="Dev News",
        icon="📰")

planilhasNfse = st.Page(page="pages/planilhasNfse.py", 
        title="Planilhas NFSe",
        icon="🧾")


# Setting up the navigation bar 
pg = st.navigation(
    {
        "BLOG": [news],
        "CONTÁBIL   ": [planilhasNfse],
    }
)

pg.run()

with st.sidebar:
    st.link_button("DEV", url="https://netopinheiro.streamlit.app/", icon="👨🏻‍💻")

# Hiding humburguer menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            #header {visibility: hidden;}
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