# Importing necessary modules
import streamlit as st
from sklearn.linear_model import LinearRegression

# Model Class
class Model:
    def __init__(self, model):
        self.model = LinearRegression()