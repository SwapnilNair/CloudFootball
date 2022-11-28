import pandas as pd
import streamlit as st
from database import view_all_data


def read():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['player_id', 'player_name_surname', 'position', 'nationality', 'player_contract_start_date', 'player_contract_end_date', 'age', 'current_market_value', 'team_id'])
    with st.expander("View all players"):
        st.dataframe(df)