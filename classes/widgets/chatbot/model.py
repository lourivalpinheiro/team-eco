# Importing necessary modules
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
import pandas as pd


# Model Class
class Model:
    def __init__(self, model='linear'):
        if model == 'linear':
            self.model = LinearRegression()
        elif model == 'tree':
            self.model = DecisionTreeRegressor()
        elif model == 'forest':
            self.model = RandomForestRegressor()
        else:
            raise ValueError(f"O modelo {model} não é suportado.")
        self.encoders = {}  # Initializes the encoders' dictionary

    def prepare_model(self, data: pd.DataFrame, target_column: str):
        """
        Prepares the model with categorical columns.
        """
        X = data.drop(columns=[target_column])
        y = data[target_column]
        self.encoders = {}

        for col in X.select_dtypes(include='object').columns:
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col])
            self.encoders[col] = le

        self.model.fit(X, y)
        return self.model

    def prepare_numerical_model(self, data: pd.DataFrame, target_column: str):
        """
        Prepares the model with numerical columns.
        """
        X = data.drop(columns=[target_column])
        y = data[target_column]

        self.model.fit(X, y)
        return self.model

    def predict_model(self, new_data: pd.DataFrame):
        """
        Makes predictions with encodedd categorical columns.
        """
        X = new_data.copy()
        for col, le in self.encoders.items():
            if col in X:
                X[col] = le.transform(X[col])
        return self.model.predict(X)

    def predict_numerical_model(self, new_data: pd.DataFrame):
        """
        Makes predictions with numerical columns.
        """
        return self.model.predict(new_data.copy())




