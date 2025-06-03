# Importing necessary modules
import pandas as pd
from model import conn

# Filter Class
class Filter:
    @classmethod
    def filter(cls, dataframe, colum_name: str, value):
        if colum_name not in dataframe:
            raise ValueError(f"Column {colum_name} not found in dataframe")
        return dataframe[dataframe[colum_name] == value][colum_name]
