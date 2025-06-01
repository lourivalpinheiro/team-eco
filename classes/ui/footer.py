# Importing necessary modules
import streamlit as st

# Footer class
class Footer:
    """
    Creates a customized Team Contabilidade's footer.
    :return: Footer.
    """

    # Constructor
    @classmethod
    def footer(cls):
        """
        Creates a customized Team Contabilidade's footer.
        """
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