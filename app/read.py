import pandas as pd
import streamlit as st
from database import view_all_data


def read():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['league_id', 'league_name', 'country', 'sponsors', 'current_champions', 'top_scorer'])
    with st.expander("View all leagues"):
        st.dataframe(df)