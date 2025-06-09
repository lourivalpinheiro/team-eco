# Importing necessary modules
import streamlit as st

class FilterUI:
    @staticmethod
    def generate_filter(dataframe, filter_label: str, filter_column: str, filter_index=None):
        if filter_column not in dataframe:
            raise ValueError(f"Column {filter_column} not found in dataframe")

        options = sorted(dataframe[filter_column].dropna().unique().tolist())

        # Use filter_label as the key to avoid conflicts if using multiple filters
        key = f"filter_{filter_label}"

        # Initialize session state if not already set
        if key not in st.session_state:
            st.session_state[key] = options[filter_index] if filter_index is not None else options[0]

        # Create selectbox with the current session state value selected
        selected = st.selectbox(
            label=filter_label,
            options=options,
            index=options.index(st.session_state[key]),
            key=key
        )

        # DO NOT update session_state[key] here because widget already manages it

        return selected
