import streamlit as st 
import pandas as pd
from model import *

st.dataframe(apiConnect())