# Importing necessary libraries
import streamlit as st
    
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
